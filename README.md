# 2021-DSA5101-Machine-Learning-Project
## Description

Codes and slides of Machine Learning Project in DSA 5101

## Prerequisite

**IDE**

+ Jupyter Notebook
+ Spyder

**Package**

+ pandas
+ numpy
+ matplotlib
+ seaborn
+ smote
+ scikit-learn
+ xgboost

**Extension**

+ jupyter_contrib_nbextensions (not required, but strongly recommended)

## Contact

HUANG XIJIE: e0732626@u.nus.edu

LI ZITIAN: lizitian@u.nus.edu

WANG SHUHUI: e0202983@u.nus.edu

## Folder and File
bank-full.csv : Data of marketing campaign of a Portuguese banking institution

bank-full-add_timestamp.csv : Data with new columns: "timestamp", "year"

Machine Learning Project.pdf : Descripition of the data and the requirement of this project

bank_name.txt : Description for the features of data, the reference and some details regarding to where the data from are also included.

"Data Exploration and Preprocssing":

+ Data Exploration.ipynb: The notebook that is used to carry on data exploration
+ Data_Exploration_sweetviz.html: Output result of the module sweetviz 
+ bank-full-add_timestamp.csv : Data with new columns: "timestamp", "year"
+ Preprocessing_Add_Year_Timestamp.py : Add year and timestamp based on the sequential order of bank-full.csv, and then export to bank-full-add_timestamp.csv

"LI ZITIAN-Random Forest-Decision Tree":

+ Random Forest Forward Selection.ipynb: The notebook that carry on feature forward selection process after the comparison of models  
+ Model_Selcetion_Random-Forest_vs_Decision-Tree.ipynb:  The notebook that is used to carry on the comparison between random forest and decision tree.
+ "temp": This folder contains part of the data that are generated during the backward selection of feature. If someone is interested in the full version, you can run the codes in Model_Selcetion_Random-Forest_vs_Decision-Tree.ipynb.

"HUANG XIJIE-XGBoost-SVM":

+ File1: ...
+ File2: ...

"WANG SHUHUI-Logistic Regression-KNN":

+ File1: ...
+ File2: ...
