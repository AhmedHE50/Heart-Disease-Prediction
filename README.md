# Heart-Disease-Prediction

An AI model that predicts the presence of heart disease in patients based on clinical and demographic data. This repository contains a Jupyter notebook that walks through data preprocessing, exploratory analysis, model training, evaluation, and comparison of multiple machine learning algorithms.

## Project Overview

Cardiovascular disease is a leading cause of death worldwide. Early detection can significantly improve patient outcomes. This project applies supervised learning techniques to predict the presence of heart disease using clinical and demographic features.

## Dataset

* Source: UCI Machine Learning Repository ("Heart Disease" dataset)
* File: `heart.csv`
* Samples: 310
* Features (14):

  * `age`: Age in years
  * `sex`: Sex (1 = male; 0 = female)
  * `cp`: Chest pain type (4 values)
  * `trestbps`: Resting blood pressure (in mm Hg)
  * `chol`: Serum cholesterol in mg/dl
  * `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
  * `restecg`: Resting electrocardiographic results (values 0,1,2)
  * `thalach`: Maximum heart rate achieved
  * `exang`: Exercise-induced angina (1 = yes; 0 = no)
  * `oldpeak`: ST depression induced by exercise relative to rest
  * `slope`: The slope of the peak exercise ST segment
  * `ca`: Number of major vessels (0-3) colored by fluoroscopy
  * `thal`: 3 = normal; 6 = fixed defect; 7 = reversible defect
  * `target`: Diagnosis of heart disease (1 = disease; 0 = no disease)

## Modeling

Models implemented and compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)

Each model is trained on a 70/30 train-test split with hyperparameter tuning via `GridSearchCV` where applicable.

## Results

| Model                  | Train Accuracy | Test Accuracy |
| ---------------------- | -------------: | ------------: |
| Logistic Regression    |         86.73% |        85.53% |
| Decision Tree          |         86.73% |        85.53% |
| Random Forest          |         95.58% |        86.84% |
| K-Nearest Neighbors    |         86.28% |        89.47% |
| Support Vector Machine |         87.61% |        84.21% |

The KNN classifier performed best on the test set with **89.47%** accuracy.