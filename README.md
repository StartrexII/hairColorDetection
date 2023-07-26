# <center> Development of a model that determines the hair color (for girls) by photo

## Table of contents
1. [Project Description](#project-description)
2. [Data description](#data-description)
3. [Libraries](#libraries)
4. [Project Installation](#project-Installation)
5. [Using the project](#using)
6. [Authors](#authors)

## Project Description

At the request of the application, it is necessary to determine the girl's hair color in 5 categories:
* **blond**
* **brown-haired**
* **light brown**
* **red hair**
* **black hair**

The request is presented in json format and contains links to images for which it is necessary to make a prediction. The idea is to highlight a face with hair, and determine the number of pixels (in fractions) for each color from 5 categories. After obtaining the quantitative content of pixels of each color, the classifier makes a prediction of hair color.

**This project** is aimed at building a hair color classifier and includes:

* creating an untagged dataset from a **complex query** (consisting of 1000 one-time queries), represented by a list of **simple queries** using the scripts(`/hairColorDetection.py`, `/parsing.py`)
* clearing data
* data markup
* modeling
* saving a trained model
* deploy(ready-made project for containerization [here](https://github.com/StartrexII/ClassificationStudy 'GitHub'))

example of **complex query** - `/data/tinderData.json`

example of  **simple query** - `/data/tinderSimpleData.json`


**Project structure:**
* [data](./data) - a folder containing all the data used in the project, a script for creating a training dataframe and a trained model
* [data/creationOfDataFrame.py](./data/creationOfDataFrame.py) - script for creating training data from a complex query
* [classifier.ipynb](./classifier.ipynb) - jupyter-notebook containing the code with the construction of the model and all the necessary steps
* [Curves.py](./Curves.py) - the script contains the Curve class, which contains methods for visualizing the selection processes and building models
* [facesClassifier.xml](./facesClassifier.xml) - cascade classifier
* [hairColorDetection.py](./hairColorDetection.py) - the main code that converts the image into the ratio of the number of pixels in color for the face and hair(the code contains a description of all methods)
* [parsing.py](./parsing.py) - the script contains a Downloader class containing methods for uploading photos to the directory, as well as getting photos to work in [OpenCV]()
* [requirements.txt](./requirements.txt) - a file with the versions of the modules used, for reproducibility of the code

:arrow_up:[To the table of contents](#table-of-contents)

## Data description

Request structure from the app(simple query):
```json
{
    "photos": [
        {
            "photo": [
                {
                    "height": 800,
                    "url": "url",
                    "width": 640
                },
                {
                    "height": 400,
                    "url": "url",
                    "width": 320
                },
                {
                    "height": 216,
                    "url": "url",
                    "width": 172
                },
                {
                    "height": 106,
                    "url": "url",
                    "width": 84
                }
            ]
        },
        {
            /// photo 2
        },
        {
            /// photo ...
        },
        {
            /// photo n
        }
    ]
}
```

A complex query for creating a dataframe consists of a list of simple queries, the structure of which is analyzed above.

Шmages are loaded in 400x320 format by default.

The dataframe is created from a complex query processed using creationOfDataFrame.py, and contains 5 columns, each of which contains the ratio ([0, 1]) of pixels close to the color of this category in the photo for a specific girl with the corresponding index (indexes are assigned to each girl in turn when parsing the query and also contain information about the photo number).

:arrow_up:[To the table of contents](#table-of-contents)

## Libraries

* Python (3.11.1):
    * [pandas (2.0.1)](https://pandas.pydata.org)
    * [numpy (1.24.3)](https://numpy.org)
    * [matplotlib (3.7.1)](https://matplotlib.org)
    * [seaborn (0.12.2)](https://seaborn.pydata.org)
    * [scikit-learn (1.2.2)](https://scikit-learn.org/stable/)
    * [optuna (3.2.0)](https://optuna.readthedocs.io/en/stable/index.html)
    * [httplib2 (0.22.0)](https://github.com/httplib2/httplib2)
    * [OpenCV (4.8.0.74)](https://opencv.org)


:arrow_up:[To the table of contents](#table-of-contents)

## Project Installation

```
    git clone https://github.com/StartrexII/hairColorDetection
```

:arrow_up:[To the table of contents](#table-of-contents)                        

## Using

To use the model, you need to install a ready-made assembly for docker [here]('GitHub').

To improve the model, it is necessary to clone this repository, a new dataframe based on better transformed data can be created by obtaining a new json file with images and running the file `data/creationOfDataFrame.py` after that, you can work on improving the classifier or use an already loaded dataframe(`data/hairColorTrainingData.csv`).

:arrow_up:[To the table of contents](#table-of-contents)

## Authors

* [Егор Орлов](https://vk.com/liquidlogic)

:arrow_up:[To the table of contents](#table-of-contents)

If the information on this project seems interesting or useful to you, then I will be very grateful to you if you mark the repository and profile with ⭐️⭐️⭐️:)