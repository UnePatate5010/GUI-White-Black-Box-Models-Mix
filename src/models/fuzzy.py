import ex_fuzzy.evolutionary_fit as GA
import ex_fuzzy.utils as  utils
import ex_fuzzy.fuzzy_sets as fs
import ex_fuzzy.maintenance as mnt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class fuzzyClassifier():

    def __init__(self, nrules, tolerance, n_gen, pop_size):
        
        self.n_gen = n_gen
        self.pop_size = pop_size

        self.classifier = GA.BaseFuzzyRulesClassifier(nRules=nrules, tolerance=tolerance, fuzzy_type=fs.FUZZY_SETS.t1)

    def fit(self, X, y):
        self.classifier.nAnts = len(X[0])
        self.classifier.n_class = len(np.unique(y))
        self.classifier.lvs = utils.construct_partitions(X, fs.FUZZY_SETS.t1)
        self.classifier.n_linguist_variables = [len(lv.linguistic_variable_names()) for lv in self.classifier.lvs]
        self.classifier.domain = None
        self.classifier.fit(X, y, n_gen=self.n_gen, pop_size=self.pop_size)
        return self

    def predict(self, X):
        return self.classifier.predict(X)

    def plot_fuzzy_variable(self, fuzzy_variable: fs.fuzzyVariable):
        '''
        Plots a fuzzy variable using trapezoidal membership functions.

        :param fuzzy_variable: a fuzzy variable from the fuzzyVariable class in fuzzy_set module.
        :return: (fig, ax)
        '''
        if mnt.save_usage_flag:
            mnt.usage_data[mnt.usage_categories.Visualization]['plot_fuzzy_variable'] += 1

        if fuzzy_variable.linguistic_variables[0].type() != fs.FUZZY_SETS.gt2:
            fig, ax = plt.subplots()
        else:
            fig = plt.figure()
            ax = plt.axes(projection='3d')

        memberships = [0, 1, 1, 0]

        colors = ['b', 'r', 'g', 'orange', 'y']
        for ix, fuzzy_set in enumerate(fuzzy_variable.linguistic_variables):
            name = fuzzy_set.name
            initiated = False
            fz_studied =  fuzzy_set.type()

            if  fz_studied == fs.FUZZY_SETS.t1:
                ax.plot(fuzzy_set.membership_parameters,
                        memberships, colors[ix], label=name)
            elif fz_studied == fs.FUZZY_SETS.t2:
                ax.plot(fuzzy_set.secondMF_lower, np.array(memberships) * fuzzy_set.lower_height, 'black')
                ax.plot(fuzzy_set.secondMF_upper, np.array(memberships), 'black')

                # Compute the memberships for the lower/upper membership points. We do it in this way because non-exact 0/1s give problems.
                x_lower = fuzzy_set.secondMF_lower
                x_lower_lmemberships = [0.0 ,fuzzy_set.lower_height ,fuzzy_set.lower_height, 0.0] 
                x_lower_umemberships = [fuzzy_set(x_lower[0])[1] , 1.0, 1.0 , fuzzy_set(x_lower[3])[1]]

                x_upper = fuzzy_set.secondMF_upper
                x_upper_lmemberships  = [0.0 , fuzzy_set(x_upper[1])[0], fuzzy_set(x_upper[2])[0], 0.0] 
                x_upper_umemberships  = [0.0 ,1.0 ,1.0, 0.0] 

                x_values = list(x_lower) + list(x_upper)
                lmembership_values = list(x_lower_lmemberships) + list(x_upper_lmemberships)
                umembership_values = list(x_lower_umemberships) + list(x_upper_umemberships)
                aux_df = pd.DataFrame(zip(x_values, lmembership_values, umembership_values),  columns=['x', 'l', 'u'])
                

                if len(aux_df['x']) != len(set(aux_df['x'])): # There are repeated elements, so we use an order that should work in this case
                    # u0 l0 u1 l1 l2 u2 l3 u3
                    x = list((x_upper[0], x_lower[0], x_upper[1], x_lower[1], x_lower[2], x_upper[2], x_lower[3], x_upper[3]))
                    l_memberships = list((x_upper_lmemberships[0], x_lower_lmemberships[0], x_upper_lmemberships[1], x_lower_lmemberships[1], x_lower_lmemberships[2], x_upper_lmemberships[2], x_lower_lmemberships[3], x_upper_lmemberships[3]))
                    u_memberships = list((x_upper_umemberships[0], x_lower_umemberships[0], x_upper_umemberships[1], x_lower_umemberships[1], x_lower_umemberships[2], x_upper_umemberships[2], x_lower_umemberships[3], x_upper_umemberships[3]))

                    ax.fill_between(x, l_memberships, u_memberships, color=colors[ix], alpha=0.5, label=name)
                else:
                    aux_df.sort_values('x', inplace=True)
                    ax.fill_between(aux_df['x'], aux_df['l'], aux_df['u'], color=colors[ix], alpha=0.5, label=name)

            elif fz_studied == fs.FUZZY_SETS.gt2:
                for key, value in fuzzy_set.secondary_memberships.items():
                    
                    gt2_memberships = value(fuzzy_set.sample_unit_domain)
                    key_plot = [float(key)]*sum(gt2_memberships > 0)
                    if initiated:
                        ax.plot(key_plot, fuzzy_set.sample_unit_domain[gt2_memberships > 0], gt2_memberships[gt2_memberships > 0], color=colors[ix])
                    else:
                        ax.plot(key_plot,  fuzzy_set.sample_unit_domain[gt2_memberships > 0], gt2_memberships[gt2_memberships > 0], color=colors[ix], label=name)
                        initiated = True

        ax.legend(loc='upper right', shadow=True)
        plt.title(fuzzy_variable.name)
        return (fig, ax)
    
    def plot_rules(self):
        """Plot rules as "IF 1 High with..."

        :return: fig, ax
        """
        text = self.classifier.print_rules(True)
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.text(0.5, 0.5, text, ha='center', va='center')
        return (fig, ax)

    def plot_fuzzy(self):
        '''
        Plot the fuzzy partitions in each fuzzy variable, as well as rules (text).
        '''
        fuzzy_variables = self.classifier.rule_base.rule_bases[0].antecedents
        l = []
        for ix, fv in enumerate(fuzzy_variables):
            l.append(self.plot_fuzzy_variable(fv))
        l.append(self.plot_rules())
        return l