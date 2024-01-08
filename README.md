<h1 align="center">Forecasting Air Quality Trends in Delhi, India: A Comprehensive Analysis</h1>
<p align="center">
  <br>
  <em>Understanding and Predicting Air Quality Dynamics Using Machine Learning and Historical Data</em>
  <br>
</p>

## Abstract
The quality of air directly impacts the survival of mankind, and with the continuous developments in various sectors, air quality has been adversely affected. This project focuses on investigating air quality data from 25 stations in Delhi for the years 2021 to 2023, employing machine learning techniques for efficient analysis and prediction.

## Introduction
Energy consumption in modern human activities results in anthropogenic sources of air pollution. Various pollutants, including CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, are released into the environment, posing health risks and contributing to environmental issues. Delhi faces significant air quality challenges, impacting public health and economic growth.

The air quality data utilized in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/abhisheksjha/time-series-air-quality-data-of-india-2010-2023), focusing on  monitoring stations in Delhi for the years 2021 to 2023. This dataset provides detailed measurements of pollutants, weather data, and air quality parameters, contributing to a comprehensive analysis of air quality trends in the region.

=============================================================

Project Organization

=============================================================

├── README.md                           <- The main README document for Data Scientists/ Analysts utilizing this project.
|
├── delhi_all_stations_hourly_2010_2023  <- Kaggle link
|
├── Presentation_Sprint1_EDA.pdf                <- Initial presentation of the project including Cleaning & EDA
├── presentation_Sprint2_baseline_models.pdf    <- Second presentation of the project including baseline models
├── Presentation_Sprint2_final.pdf              <- Final presentation of the project 
|
├── notebooks
|   ├── 1_data_preparation.ipynb              <- Project notebook 1 - data preparation 
|   ├── 2_data_exploration.ipynb              <- Project notebook 2 - data exploration
|   ├── 3_baselinemodelling.ipynb             <- Project notebook 3 - baseline modeling
|   ├── 4.1_model_randomforest.ipynb          <- Project notebook 4.1 - randomforest modeling
|   ├── 4.2_model_xgboost.ipynb               <- Project notebook 4.2 - xgboost modeling
|   ├── 4.3_model_ARIMA.ipynb                 <- Project notebook 4.3 - ARIMA modeling
|   ├── 4.4_model_fb_prophet.ipynb            <- Project notebook 4.4 - prophet modeling
|   ├── 4.5_model_LSTM.ipynb                  <- Project notebook 4.5 - LSTM modeling
|
├── app
|   ├── xgb_aqi_model____no_rolling_window_data.pkl    <- XGBoost model
|   ├── aqi_predictor_app.py                           <- Streamlit python code

## Objectives
- Analyze air quality data from 25 stations in Delhi (2021-2023).
- Identify key pollutants affecting the Air Quality Index (AQI).
- Address data imbalance using resampling techniques.
- Utilize machine learning models for air quality prediction.
- Compare and evaluate the performance of different machine learning models.

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
| y_AQI                     | Target variable indicating the Air Quality Index forecast for the next 24 hours| Numeric    |

## Methodology
### Data Preprocessing:
- Clean and preprocess the dataset.
- Select key features through correlation analysis.
### Exploratory Data Analysis (EDA):
- Gain insights into hidden patterns in the dataset.
- Identify pollutants directly affecting the AQI.
### Data Resampling:
- Address data imbalance using resampling techniques.
### Machine Learning Models:
- Initiated with a foundational linear regression model (R-squared: 0.79).
- Explored a baseline decision tree with a max depth of 3 (R-squared: 0.71).
- Employed five machine learning models for air quality prediction.
- Compared results using standard metrics.

## Results and Conclusion
- Evaluated and compared model performances.
- Determined the most effective model for AQI prediction.

## Next Steps
- Optimize missing value handling by collecting data from nearby stations.
- Implement Time Series Modeling with ARIMA.
- Explore advanced techniques like XGBoost and LSTM.
- Conduct rigorous Model Evaluation.
- Apply Principal Component Analysis (PCA) to streamline features.
- Perform a detailed Feature Importance Analysis.

## Conclusion
This project aims to contribute to the analysis and prediction of air quality in Delhi. The utilization of machine learning techniques and comprehensive data analysis provides valuable insights into the factors influencing air pollution. The comparison of different models aids in identifying the most effective approach for AQI prediction, offering a potential solution to address air quality challenges.

Feel free to explore the code and datasets in this repository to gain a deeper understanding of the methodologies and findings. Contributions and suggestions are welcome. Together, we can work towards a cleaner and healthier environment.


Feel free to explore the code and datasets in this repository to gain a deeper understanding of the methodologies and findings. Contributions and suggestions are welcome. Together, we can work towards a cleaner and healthier environment.

