# Churn Prediction Model and Analysis

## Project Background
A California-based telecommunications company is interested in gathering churn and retention insights from their customer data, with various identity, behavioral, and engagement data during the third quarter of the fiscal year. This project aims to analyze and synthesize this data to provide critical customer churn insights that will improve retention and overall business success, with a dashboard and report that communicates the most significant findings. 

Insights and recommendations provided within the following key domains:
- **Customer Retention Trends**: Evaluated historical customer retention patterns, with a focus on Churn and Retention Rate, Customer Lifetime Value (CLV), and Revenue.
- **Service Performance**: Analyzed services' impact on overall revenue and churn
- **Offer Success**: Assessed success of five offers put out in Q3, gathering insights on their influence on customer churn
- **City Comparisons**: Evaluation of metrics by city

Interactive Tableau dashboard [here](link)

## Dataset and Data Structure
Data taken from [IBM's Telecommunications Industry Sample Data](https://accelerator.ca.analytics.ibm.com/bi/?perspective=authoring&pathRef=.public_folders%2FIBM%2BAccelerator%2BCatalog%2FContent%2FDAT00148&id=i9710CF25EF75468D95FFFC7D57D45204&objRef=i9710CF25EF75468D95FFFC7D57D45204&action=run&format=HTML&cmPropStr=%7B%22id%22%3A%22i9710CF25EF75468D95FFFC7D57D45204%22%2C%22type%22%3A%22reportView%22%2C%22defaultName%22%3A%22DAT00148%22%2C%22permissions%22%3A%5B%22execute%22%2C%22read%22%2C%22traverse%22%5D%7D). Overall dataset structure can be seen below, consisting of five tables: *demographics, location, population, services, and status* data with 7k+ records. The raw data includes numerous features of both categorical and numerical values. For this analysis, our target variable will be the *status*'s churn value attribute.

## Overview
This project builds a churn prediction model using SQL, Python (pandas, scikit-learn, matplotlib, seaborn), and Tableau.  
It demonstrates an end-to-end workflow: data wrangling and modeling - data analysis - visualizations + dashboard - insights.

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
- models/ → stored pipelines
- notebooks/ → data exploration + analysis
- reports/ → screenshots, docs
- sql/ → SQL scripts
- src/ → Python scripts
- tableau/ → Tableau dashboard
