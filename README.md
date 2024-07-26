# GUI-White-Black-Box-Models-Mix

This repository contains the code of a GUI developped during a 3-month intership in the Computer Intelligence Laboratory of Osaka Metropolitan University under the supervision of Professor Yusuke Nojima.

It consists in a simple GUI where the user can select differents classifiers and their hyperparameters and run experiments. Results are then displayed in the form of graphs, 
schemas and statistics. The goal was to help understanding the “Integrating White and Black Box Techniques for Interpretable Machine Learning” research paper written by Eric Vernon, Naoki Masuyama and Yusuke Nojima (all from Osaka Metropolitan University).


## Project Structure
The main code is located in `src/` which is divided in different categories. For instance, all code files directly related to the graphic interface (frames...) are inside `src/widgets/`. Moreover, tests can be found in `tst/`. Finally, new datasets can be added in `datasets/` (they must respect a specific format and currently only 2D datasets are supported).
```
.
└── GUI/
    ├── datasets/
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
```

## Getting Started
I recommend you to download the latest release [here](https://github.com/UnePatate5010/GUI-White-Black-Box-Models-Mix/releases) or the code from the [main branch](https://github.com/UnePatate5010/GUI-White-Black-Box-Models-Mix/tree/main).

The first step is to install the required packages:
```console
pip install -r ./requirements.txt
```
My advice is to create beforehand a virtual environment.

Currently, the app can be launched by running the `main.py` file using the following command:
```console
python3 ./src/main.py
```
The file must be runned from the root of the project.

 It will open a window with different scrollable menus. Models, datasets and resampling method can be selected using the said menus. Some parameters will then be displayed and can be tweaked to tune the experiment. When everything is set, press the `run` button to launch the experiment. Results will then be displayed in dedicated frames.


## Issues & Warnings

Please refer to the [github issues section](https://github.com/UnePatate5010/GUI-White-Black-Box-Models-Mix/issues).

## Expansions
Different expansions are currently being considered. All of them might no be implemented though.
- Documentation (user and developer)
- Support for different datasets file types (currently only CSV files with a specific format are supported)
- More data resampling methods and classifier (especially fuzzy classifiers)
- More QoL features ?

## Gallery

![](GUI.png)
