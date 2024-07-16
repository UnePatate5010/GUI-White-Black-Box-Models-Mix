# GUI-White-Black-Box-Models-Mix

This repository contains the code of a GUI developped during a 3-month intership in the Computer Intelligence Laboratory of Osaka Metropolitan University.

It consists in a simple GUI where the user can select differents classifiers and their hyperparameters and run experiments. Results are then displayed in the form of graphs, 
schemas and statistics.


## Project Structure
The main code is located in `src/` which is divided in different categories. For instance, all code files directly related to the graphic interface (frames...) are inside `src/widgets/`. Moreover, tests can be found in `tst/`. Finally, new datasets can be added in `datasets/` (more tweaks are needed though).
```
.
└── GUI/
    ├── datasets/
    ├── src/
    │   ├── datasets/
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
I recommend you to download the latest release [here](https://github.com/UnePatate5010/GUI-White-Black-Box-Models-Mix/releases).

The first step is to install the required packages:
```console
pip install -r ./requirements.txt
```
My advice is to create beforehand a virtual environment.

Currently, the app can be launched by running the `main.py` file using the following command:
```console
python3 ./src/main.py
```
 It will open a window with different scrollable menus. Models, datasets and resampling method can be selected using the said menus. Some parameters will then be displayed and can be tweaked to tune the experiment. When everything is set, press the `run` button to launch the experiment. Results will then be displayed in dedicated frames.


## Issues & Warnings

Entry fields accept every kind of string but only int should be put inside. A wrong input results in a error which is currently caught.


## Expansions
Different expansions are currently being considered. All of them might no be implemented though.
- Documentation (user and developer)
- Dimensionality reduction techniques to handle datasets with more than two features
- Support for different datasets file types (currently only CSV files with a specific format are supported)
- More QoL features ?

## Gallery

![](Example.png)