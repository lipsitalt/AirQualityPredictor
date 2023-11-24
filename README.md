<h1 align="center">Forecasting Air Quality Trends in Delhi, India: A Comprehensive Analysis</h1>
<p align="center">
  <br>
  <em>Understanding and Predicting Air Quality Dynamics Using Machine Learning and Historical Data</em>
  <br>
</p>

## **Abstract**
The survival of mankind is intricately linked to the quality of air. However, consistent developments in various sectors of modern human society have adversely affected air quality. Daily industrial, transport, and domestic activities release hazardous pollutants into the environment. Monitoring and predicting air quality have become essential, especially in developing countries like India. This project investigates air quality data from 20 stations in Delhi for the years 2018 and 2019, employing machine learning techniques for efficient analysis and prediction.

Energy consumption and its consequences are unavoidable in modern human activities, leading to anthropogenic sources of air pollution. Various pollutants, such as CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, etc., are released into the environment, posing health risks to humans, animals, and plants. Air pollution can result in severe diseases and contribute to environmental issues like global warming, acid rain, and climate change. Poor air quality is a significant challenge in Delhi, India, affecting public health and economic growth.

## Introduction

Energy consumption and its consequences are unavoidable in modern human activities, leading to anthropogenic sources of air pollution. Various pollutants, such as CO, CO2, Particulate Matter (PM), NO2, SO2, O3, NH3, Pb, etc., are released into the environment, posing health risks to humans, animals, and plants. Air pollution can result in severe diseases and contribute to environmental issues like global warming, acid rain, and climate change. Poor air quality is a significant challenge in Delhi, India, affecting public health and economic growth.

The air quality data utilized in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india). Specifically, the dataset includes information from 20 monitoring stations in Delhi for the years 2018 and 2019. This dataset, provides detailed measurements of various pollutants and air quality parameters, contributing to a comprehensive analysis of air quality trends in the region.


## Objectives
Analyze air quality data from 20 stations in Delhi for the years 2018 and 2019.
Identify key pollutants affecting the Air Quality Index (AQI).
Address data imbalance issues using resampling techniques.
Utilize machine learning models for air quality prediction.
Compare and evaluate the performance of different machine learning models.

## Data Dictionary
The project utilizes air quality data extracted from 20 stations in Delhi for the years 2018 and 2019. The dataset comprises 12 features with instances recorded at each station.

- `StationId`: Unique identifier for each monitoring station.
- `Datetime`: Timestamp indicating the date and time of the recorded data.
- `PM2.5`: Particulate Matter with a diameter of 2.5 microns or less.
- `PM10`: Particulate Matter with a diameter of 10 microns or less.
- `NO`: Nitric Oxide concentration.
- `NO2`: Nitrogen Dioxide concentration.
- `NOx`: Sum of Nitric Oxide and Nitrogen Dioxide concentrations.
- `NH3`: Ammonia concentration.
- `CO`: Carbon Monoxide concentration.
- `SO2`: Sulfur Dioxide concentration.
- `O3`: Ozone concentration.
- `Benzene`: Concentration of Benzene in the air.
- `Toluene`: Concentration of Toluene in the air.
- `Xylene`: Concentration of Xylene in the air.

## Methodology

#### Data Preprocessing:

- Clean and preprocess the dataset.
- Select key features through correlation analysis.

#### Exploratory Data Analysis (EDA):

- Gain insights into hidden patterns in the dataset.
- Identify pollutants directly affecting the AQI.

#### Data Resampling:

- Address data imbalance using resampling techniques.

#### Machine Learning Models:

- Employ five machine learning models for air quality prediction.
- Compare results using standard metrics.
- Results and Conclusion:

#### Evaluate and compare model performances:

- Determine the most effective model for AQI prediction.

## Conclusion

This project aims to contribute to the analysis and prediction of air quality in Delhi. The utilization of machine learning techniques and comprehensive data analysis provides valuable insights into the factors influencing air pollution. The comparison of different models aids in identifying the most effective approach for AQI prediction, offering a potential solution to address air quality challenges.

Feel free to explore the code and datasets in this repository to gain a deeper understanding of the methodologies and findings. Contributions and suggestions are welcome. Together, we can work towards a cleaner and healthier environment.

## References
