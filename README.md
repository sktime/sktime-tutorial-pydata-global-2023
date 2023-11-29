Welcome to the sktime workshop at pydata global 2023
====================================================

This tutorial is about [sktime] - a unified framework for machine learning with time series. sktime contains algorithms and tools for building, applying, evaluating modular pipelines and composites for a variety of time series learning tasks, including forecasting, classification, regression.

`sktime` is easily extensible by anyone, and interoperable with the python data science stack.

This tutorial gives a walkthrough of new `sktime` features in 2022-2023,together with an updated general introduction.

[sktime]: https://www.sktime.net

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2023/main?filepath=notebooks) [![!discord](https://img.shields.io/static/v1?logo=discord&label=discord&message=chat&color=lightgreen)](https://discord.com/invite/54ACzaFsn7) [![!slack](https://img.shields.io/static/v1?logo=linkedin&label=LinkedIn&message=news&color=lightblue)](https://www.linkedin.com/company/scikit-time/)

## :rocket: How to get started

In the tutorial, we will move through notebooks section by section.

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages (`sktime`, `seaborn`, `jupyter`) in an environment, and open the notebooks with that environment. For detail instructions, see below. For troubleshooting, see sktime's more detailed [installation instructions].
* or, use python venv, and/or an editable install of this repo as a package. Instructions below.

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2023/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.net/en/latest/installation.html

Please let us know on the [sktime discord](https://discord.com/invite/54ACzaFsn7) if you have any issues during the conference, or join to ask for help anytime.

## :bulb: Description

The tutorial gives an updated 30 minute introduction to sktime base features with a focus on forecasting, and then proceeds with a vignette slideshow introducing the most important features added since pydata global 2022:

* Upgraded base interface using scikit-base
* Rework of the forecasting pipeline interface
* fully distributional probabilistic forecasts and metrics
* extended parallelism, including parallel broadcasting to hierarchical data
* composable time series classifiers, regressors, distances, time series aligners
* reproducibility features such as blueprint and fitted estimator serialization
* benchmarking frameworks for replicating studies such as M4/M5

Each feature vignette will come with links to further, extended tutorials where applicable.

`sktime` not just a package, but also an active community which aims to be welcoming to new joiners.

sktime is developed by an open community, with aims of ecosystem integration in a neutral, charitable space. We welcome contributions and seek to provides opportunity for anyone worldwide.

We invite anyone to get involved as a developer, user, supporter (or any combination of these).


## :movie_camera: Other Tutorials:

- [Europython 2023 - General sktime introduction, half-day workshop](https://github.com/sktime/sktime-tutorial-europython-2023)

- [PyCon Prague 2023 - Forecasting, Advanced Pipelines, Benchmarking](https://github.com/sktime/sktime-tutorial-pydata-global-2023)

- [Pydata Amsterdam 2023 - Probabilistic prediction, forecasting, evaluation](https://github.com/sktime/sktime-tutorial-pydata-Amsterdam-2023)

- [ODSC Europe 2023 - Forecasting, Pipelines, and ML Engineering](https://github.com/sktime/sktime-tutorial-ODSC-Europe-2023/tree/main)

- [Pydata London 2023 - Time Series Classification, Regression, Distances & Kernels](https://github.com/sktime/sktime-tutorial-pydata-london-2023)

- [Pydata Berlin 2022 - Advanced Forecasting Tutorial](https://www.youtube.com/watch?v=4Rf9euAhjNc)

- [Pydata London 2022 - How to implement your own estimator in sktime](https://www.youtube.com/watch?v=S_3ewcvs_pg)

- [Pydata Global 2022 - Feature extraction, Pipelines, Tuning](https://github.com/sktime/sktime-tutorial-pydata-global-2022)


## :wave: How to contribute

If you're interested in contributing to sktime, you can find out more how to get involved [here](https://www.sktime.net/en/latest/get_involved.html).

Any contributions are welcome, not just code!

## Installation instructions for local use

To run the notebooks locally, you will need:

* a local repository clone
* a python environment with required packages installed

### Cloning the repository

To clone the repository locally:

`git clone https://github.com/sktime/sktime-tutorial-pydata-global-2023`

### Using conda env

1. Create a python virtual environment:
`conda create -y -n pycon_prague python=3.9`
2. Install required packages:
`conda install -y -n pycon_prague pip sktime seaborn jupyter pmdarima statsmodels dtw-python`
3. Activate your environment:
`conda activate pycon_prague`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=pycon_prague`

### Using python venv

1. Create a python virtual environment:
`python -m venv pycon_prague`
2. Activate your environment:
 - `source pycon_prague/bin/activate` for Linux
 - `pycon_prague/Scripts/activate` for Windows
3. Install the requirements:
`pip install -r requirements`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=pycon_prague`
