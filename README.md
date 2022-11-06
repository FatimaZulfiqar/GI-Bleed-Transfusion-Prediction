# GI-Bleed-Transfusion-Prediction

The project calculates units of blood required for patient's tramsfusion based on several inputs such as

- Gender
- Age
- Systolic BP
- Weight
- Height
- BMI
- Symptoms
- Melena
- hematochezia
- Initial Hb
- BUN/Cr
- aPTT
- INR
- NSAIDS
- Anticoag
- Antiplatelet
- PPI

Several Machine Learning Regressor models are applied to the dataset for model training and testing. 

# Obtained Results:

Detailed Performance of all Models
==================================

+--------------------------+------+------+------+-------+
|          Model           | MSE  | MAE  | RMSE |   R2  |
+--------------------------+------+------+------+-------+
|    Linear Regression     | 4.92 | 1.34 | 2.22 | -0.11 |
|     Ridge Regression     | 4.49 | 1.25 | 2.12 | -0.01 |
|     Lasso Regression     | 2.38 | 1.31 | 1.54 |  0.0  |
| Random Forest Regression | 3.99 | 1.13 | 2.0  |  0.1  |
| Decision Tree Regression | 5.53 | 1.28 | 2.35 | -0.25 |
|     Extra Regression     | 4.35 | 1.23 | 2.09 |  0.02 |
|    Bagging Regressor     | 4.05 | 1.09 | 2.01 |  0.09 |
+--------------------------+------+------+------+-------+

Best Model
============

+--------------------------+------+------+------+-----+
|          Model           | MSE  | MAE  | RMSE |  R2 |
+--------------------------+------+------+------+-----+
| Random Forest Regression | 3.99 | 1.13 | 2.0  | 0.1 |
+--------------------------+------+------+------+-----+


# Deployment
The project is developed using Python, Flask web-based API, and deployed to Heroku.

Project URL 👇
https://gibleedtransfusioncalculator.herokuapp.com/
