# Educational Data Mining Project

<p align="center">
  <img width=440px src="https://user-images.githubusercontent.com/56659549/167325692-bfe74a7e-02a1-4fdc-8bb1-508194fa3dd9.jpg">
</p>

## Introduction

Annualy, a brazillian exam called ENEM(Exame Nacional do Ensino Médio), translated as High school national exam, enrolls high school students into college. This exam have math, portuguese, science, geography and history tests. Finishing the test the candidate will receive a grade that will be used for entering college.

About 10 million people with diferente cultures and socioeconomic conditions register annually for this exam, making it the main entrance into college life in Brazil.

## Objective
Apply Data Analysis and Machine Learning techniques to figure out which variables influence a candidate's performance on the high school national exam.

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── tableau        <- Used to visualize the final data.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py
     


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
