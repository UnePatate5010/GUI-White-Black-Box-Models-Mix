.. _extending:

Extending the GUI
=================

This section gives an overview of the GUI architecture and explain how it can be extended. The application is organized as the following::

    .
    └── GUI/
        ├── datasets/
        ├── docs/
        ├── src/
        │   ├── datasets/
        │   │   ├── dimReduction/
        │   │   └── ...
        │   ├── experiment/
        │   ├── models/
        │   ├── resamplingMethods/
        │   ├── widgets/
        │   └── ...
        ├── tst/
        ├── LICENSE
        ├── READMED.md
        └── requirements.txt




Adding Datasets
---------------

Datasets can be simply added to the `datasets/` directory. They must be `csv` files with separated by commas (`,`). The first columns are
values of the different features and the last column is the label. The label must be an integer. Each line corresponds to a different data point. For instance, files must
look like this::

    1.7226817454900973,0.615281065045062,1
    -1.0868413308404024,8.150410733829125,3
    1.075686805692181,-0.04299697464713548,1
    2.764094682205849,0.5185214051348365,1
    ...

If you wish to manipulate other types of files, you should change the `loadDAtaset` function located in `src/datasets/loadDataset.py`.


Adding Dimensionality Reduction Techniques
------------------------------------------

Dimensionality reduction techniques are in `src/datasets/dimReduction/`. You can create a new file for the new technique. A corresponding frame
should also be added in `src/widgets/datasets/dimReduction/`. This frame should have one entry for each parameter of the newly added technique. Then,
the `DIM_REDUCTION` dictionnary in `src/constants.py` has to be modified. That dictionnary links dimensionality reduction techniques names to the 
corresponding frame.

The techique mst be an object. The corresponding file either contains a function that returns the object or simply the object itself. Each technique must provide
the `fit_transform` method that takes the dataset and labels and returns the new dataset with less features. Moreover, the frame instantiates the technique and returns it
with its `get` method.

You can look at the the other techniques to figure out how to implements new ones.

Adding Classifiers
------------------

Classifier are added the same way as Dimensionality reduction techniques:

* Add a new file with the classifier in `src/models/`;
* Add the corresponding frame with the right parameters in `src/widgets/modelFrames`;
* Linking the classifier and its frame through the `MODEL_FRAMES` dictionnary in `src/constants.py`.

All classifiers must have a `fit` method to train it and a `predict` method to make predictions. Moreover, the frame instantiates the classifier and returns it
with its `get` method.

If you had a white box model, it should also have a way to visualize it through a schema. That visualization should be added in the schema output frame located
in `src/widgets/outputFrames/schemaFrame.py`. 

You can look at the the other classifiers to figure out how to implements new ones.


Adding Data Resampling Methods
------------------------------

Exactly as classifiers and dimensionality reduction techniques, data resampling methods are added through dedicated files and frames:

* Add a new file with the method in `src/resamplingMethods/`;
* Add the corresponding frame with the right parameters in `src/widgets/resamplingFrames`;
* Linking the classifier and its frame through the `RESAMPLING_FRAMES` dictionnary in `src/constants.py`.

Those methods must have a `fit_resample` method. Any error related to a too low amount of data in the small class must be dealt with in the resampling method. 
Moreover, the frame instantiates the method and returns it with its `get` method.

You can look at the the other methods to figure out how to implements new ones.



Modifying Outputs
-----------------

ALl output frames are in `src/widgets/outputFrames/`. Each one makes its own graphs and schemas from given parameters.