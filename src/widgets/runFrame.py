import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from translation import translate


class RunFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.run_button = ctk.CTkButton(self, text="RUN", command=self.button_callback, fg_color="#6aa51f")
        self.run_button.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    
    def button_callback(self):
        # Get methods and hyperparameters
        try:
            input = self.master.get()
            # print(input)
        except KeyError:
            print("At least one field was not filled")
            return

        # Format them correctly (convert dicts to reflect real arguments names)

        r = input["grader"]
        dic, func = translate(r[0], r[1])
        print(dic)
        model = func(**dic)
        print(model)


        # Call the main function
        # Update output frames with results


        # Example placeholder
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig = Figure(figsize = (5, 5), dpi = 100) 
        plot1 = fig.add_subplot(111)        
        t = np.linspace(0.01, 5, 500)
        b = np.log(t)
        plot1.plot(t, b)
        canvas = FigureCanvasTkAgg(fig, master = self.master.graph)
        canvas.draw()
        canvas.get_tk_widget().grid(sticky="ewsn")


    def freeze(self):
        self.run_button.configure(state="disabled")

    def unfreeze(self):
        self.run_button.configure(state="normal")

canvas = None