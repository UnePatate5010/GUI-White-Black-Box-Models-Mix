# I will no longer maintain this project. It will now be hosted by the Computational Intelligence Laboratory of Osaka Metropolitan University. [Click here for their newer version](https://github.com/ci-labo-omu/GUI-White-Black-Box-Models-Mix)

# GUI-White-Black-Box-Models-Mix

This repository contains the code of a GUI developed during a 3-month internship in the Computer Intelligence Laboratory of Osaka Metropolitan University under the supervision of Professor Yusuke Nojima.

It consists in a simple GUI where the user can select different classifiers and their hyperparameters and run experiments. Results are then displayed in the form of graphs, 
schemas and statistics. The goal was to help understanding the “Integrating White and Black Box Techniques for Interpretable Machine Learning” research paper written by Eric Vernon, Naoki Masuyama and Yusuke Nojima (all from Osaka Metropolitan University).


## Project Structure
The main code is located in `src/` which is divided in different categories. For instance, all code files directly related to the graphic interface (frames...) are inside `src/widgets/`. Moreover, tests can be found in `tst/`. Finally, new datasets can be added in `datasets/` (they must respect a specific format and currently only 2D datasets are supported).
```
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
The file must be run from the root of the project.

 It will open a window with different scrollable menus. Models, datasets and resampling method can be selected using the said menus. Some parameters will then be displayed and can be tweaked to tune the experiment. When everything is set, press the `run` button to launch the experiment. Results will then be displayed in dedicated frames.

## Documentation
The documentation is located in `docs/source`. It can be compiled by using `./make html` (windows) or `make html` (linux). The compiled documentation
will be in `docs/build/html` (open the `index.html` file in your web browser). Please be sure to install Sphinx by running the following commad:

```console
pip install -r ./requirements_docs.txt
```

## Issues & Warnings

Please refer to the [github issues section](https://github.com/UnePatate5010/GUI-White-Black-Box-Models-Mix/issues).

## Expansions
Different expansions are currently being considered. All of them might not be implemented though.
- ~~Documentation (user and developer)~~
- Support for different datasets file types (currently only CSV files with a specific format are supported)
- More data resampling methods and classifiers ~~(especially fuzzy classifiers)~~
- More QoL features ?

## Research
This project led to the writing of a research paper entitled "Enhancing Machine Learning Interpretability Through a Graphical User Interface". It was accepted at the
[SCIS&ISIS2024](http://soft-cr.org/scis/2024/) conference in Himeji, Japan. It will be presented between Nov. 9th and 12th.

## Gallery

![](GUI_dark.png)
![](GUI_light.png)
