# Churn Prediction Model

## Overview
This project builds a churn prediction model using SQL, Python (pandas, scikit-learn, matplotlib, seaborn), and Tableau.  
It demonstrates an end-to-end workflow: data extraction - modeling - visualizations + dashboard - insights.

## Local Setup
1. Cloning Repository
```
git clone https://github.com/YOUR-USERNAME/churn-prediction.git
cd churn-prediction
```

2. Setting Up Virtual Environment + Dependencies
* Ensure Python 3 is installed
```
python3 -m venv venv
source venv/bin/activate
# Windows : venv\Scripts\activate 
pip install -r requirements.txt
```

## Repo Structure
- data/ → raw + processed datasets
- sql/ → SQL scripts
- src/ → Python scripts
- notebooks/ → exploratory analysis
- tableau/ → Tableau dashboard
- reports/ → screenshots, docs

## Dataset
Data taken from [IBM's Telecommunications Industry Sample Data](https://accelerator.ca.analytics.ibm.com/bi/?perspective=authoring&pathRef=.public_folders%2FIBM%2BAccelerator%2BCatalog%2FContent%2FDAT00148&id=i9710CF25EF75468D95FFFC7D57D45204&objRef=i9710CF25EF75468D95FFFC7D57D45204&action=run&format=HTML&cmPropStr=%7B%22id%22%3A%22i9710CF25EF75468D95FFFC7D57D45204%22%2C%22type%22%3A%22reportView%22%2C%22defaultName%22%3A%22DAT00148%22%2C%22permissions%22%3A%5B%22execute%22%2C%22read%22%2C%22traverse%22%5D%7D). It is a sample set of data providing information on a fictional telco company, including five tables: *demographics, location, population, services, and status* data. The raw data includes numerous features of both categorical and numerical values. For this analysis, our target variable will be the *status*'s churn value attribute.