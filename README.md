<h1 align="center">Forecasting Air Quality Trends in Delhi, India: A Comprehensive Analysis</h1>
<p align="center">
  <br>
  <em>Understanding and Predicting Air Quality Dynamics Using Machine Learning and Historical Data</em>
  <br>
</p>

## Abstract
The quality of air directly impacts the survival of mankind, and with the continuous developments in various sectors, air quality has been adversely affected. This project focuses on investigating air quality data from 40 recording stations in Delhi for the years 2013 to 2023, employing machine learning techniques for efficient analysis and prediction.

**************************************************************

## Introduction

**************************************************************

Energy consumption in modern human activities results in anthropogenic sources of air pollution. Various pollutants, including CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, are released into the environment, posing health risks and contributing to environmental issues. Delhi faces significant air quality challenges, impacting public health and economic growth.

The air quality data utilized in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/abhisheksjha/time-series-air-quality-data-of-india-2010-2023), focusing on  monitoring stations in Delhi for the years 2021 to 2023. This dataset provides detailed measurements of pollutants, weather data, and air quality parameters, contributing to a comprehensive analysis of air quality trends in the region.

**************************************************************

## Project Organization

**************************************************************

- README.md <- The main README document for Data Scientists/Analysts utilizing this project.
- presentations <- Directory for project presentations
  - Sprint1_Presentation.pdf <- Initial presentation of the project including Cleaning & EDA
  - Sprint2_Presentation.pdf <- Second presentation of the project including baseline models
  - Sprint2_Presentation.pdf <- Final presentation of the project
- notebooks <- Directory for project notebooks
  - 1_data_preparation.ipynb <- Project notebook 1 - data preparation
  - 2_data_exploration.ipynb <- Project notebook 2 - data exploration
  - 3_baselinemodelling.ipynb <- Project notebook 3 - baseline modeling
  - 4.1_model_randomforest.ipynb <- Project notebook 4.1 - randomforest modeling
  - 4.2_model_xgboost.ipynb <- Project notebook 4.2 - xgboost modeling
  - 4.3_model_ARIMA.ipynb <- Project notebook 4.3 - ARIMA modeling
  - 4.4_model_fb_prophet.ipynb <- Project notebook 4.4 - prophet modeling
  - 4.5_model_LSTM.ipynb <- Project notebook 4.5 - LSTM modeling
- app <- Directory for the app and model files
  - xgb_aqi_model.pkl <- XGBoost model
  - aqi_predictor_app.py <- Streamlit python code

**************************************************************

## Table of contents

**************************************************************
- Air Quality Dataset
- Data Download, Preprocessing & EDA
- Modelling
- Conclusions

**************************************************************

## Air Quality Dataset

**************************************************************

## Data Dictionary
The project utilizes air quality data extracted from 20 stations in Delhi for the years 2018 and 2019. The dataset comprises 12 features with instances recorded at each station.
| **Features**              | **Description**                                             | **Type**   |
|---------------------------|-------------------------------------------------------------|------------|
| Datetime                  | Timestamp indicating the date and time of the recorded data | -          |
| StationId                 | Unique identifier for each monitoring station               | Numeric    |
| PM2.5 (ug/m3)             | Particulate Matter with a diameter of 2.5 microns or less   | Numeric    |
| PM10 (ug/m3)              | Particulate Matter with a diameter of 10 microns or less   | Numeric    |
| NO (ug/m3)                | Nitric Oxide concentration                                  | Numeric    |
| NO2 (ug/m3)               | Nitrogen Dioxide concentration                               | Numeric    |
| NOx (ug/m3)               | Sum of Nitric Oxide and Nitrogen Dioxide concentrations     | Numeric    |
| NH3 (ug/m3)               | Ammonia concentration                                       | Numeric    |
| SO2 (ug/m3)               | Sulfur Dioxide concentration                                | Numeric    |
| CO (ug/m3)                | Carbon Monoxide concentration                               | Numeric    |
| Ozone (ug/m3)             | Ozone concentration                                         | Numeric    |
| Benzene (ug/m3)           | Concentration of Benzene in the air                          | Numeric    |
| Toluene (ug/m3)           | Concentration of Toluene in the air                          | Numeric    |
| RH (%)                    | Relative Humidity in percentage                             | Numeric    |
| WS (m/s)                  | Wind Speed in meters per second                              | Numeric    |
| WD (degree)               | Wind Direction in degrees                                   | Numeric    |
| BP (mmHg)                 | Barometric Pressure in millimeters of mercury               | Numeric    |
| AT (degree C)             | Ambient Temperature in degrees Celsius                      | Numeric    |
| RF (mm)                   | Rainfall in millimeters                                     | Numeric    |
| SR (W/mt2)                | Solar Radiation in Watts per square meter                    | Numeric    |
| Xylene (ug/m3)           | Concentration of Xylene in the air                            | Numeric    |

| **Trget**              | **Description**                                             | **Type**   |
|---------------------------|-------------------------------------------------------------|------------|
| <span style="color: #FF0000;">y_AQI</span>     | Target variable indicating the Air Quality Index forecast for the next 24 hours| Numeric    |

**************************************************************

## Data Preparation & Exploratory Data Analysis

**************************************************************

### Data Preprocessing:
- Clean and preprocess the dataset.
- Select key features through correlation analysis.
- Remove outliere
- Handle missing values
  
### Exploratory Data Analysis (EDA):
- Gain insights into hidden patterns(Hourly, Daily, and Yearly seasonalities) in the dataset.
- Identify pollutants directly affecting the AQI by looking at correlation and hypothesis testing
- Feature Engineering
- Data filtering
- Skewness handling

These insights will guide our subsequent modeling and analysis efforts, helping us make informed decisions based on the patterns and relationships identified during the EDA process.

**************************************************************

## Modeling

**************************************************************

### Machine Learning Models:
- Baseline linear regression model (PMAE: 20.04%)
- Decision Tree (PMAE: 26.06%)
- Random Forest (PMAE: 20.25%)
- XGBoost (PMAE: 15.25%)
- Prophet (PMAE: 31.79%)
- ARIMA (PMAE: 185.00%)
- SARIMA (PMAE: 186.00%)

## Results and Conclusion
- Evaluated and compared model performances.
- Determined the most effective model for AQI prediction as XGBoost with the least Percentage Mean Absolute Error(PMAE: 15.25%)
**************************************************************

## Conclusion

**************************************************************

This project aims to contribute to the analysis and prediction of air quality in Delhi. The utilization of machine learning techniques and comprehensive data analysis provides valuable insights into the factors influencing air pollution. The comparison of different models aids in identifying the most effective approach for AQI prediction, offering a potential solution to address air quality challenges.

Feel free to explore the code and datasets in this repository to gain a deeper understanding of the methodologies and findings. Contributions and suggestions are welcome. Together, we can work towards a cleaner and healthier environment.
