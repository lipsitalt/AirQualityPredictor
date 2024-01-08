# aqi_engine.py

import numpy as np
import pandas as pd


"""
Algorith to calculate AQI and filling missing data:
---------------------------------------------------
1. Calculate AQI without filling any missing data
2. Iteratively fill missing data of pollutants in the order of pollutant importance, and invoke calculate_aqi for those filled missing records
3. Iteratively fill missing data for rest of the pollutants
4. Fill missing data for remaining records with higher rolling hours data
"""

"""
Fill Missing Values with Rolling Average:

* The function `fill_missing_with_average` is designed to address missing values in specified columns by filling them with the past 'x' hours' rolling average across all stations. Here's a breakdown of the code:
* This function takes a DataFrame (df), the number of rolling hours, and a list of columns for which we need to fill the missing values as parameters. 
* It then calculates the rolling average for each specified column and fills missing values with the computed averages, effectively imputing missing data points based on past observations.
"""
# Function to fill missing values with the past 'x' hours average
def fill_missing_with_average(df, rolling_hours, columns):
    # Sort the DataFrame by 'Datetime' to apply rolling window across stations, and finally Reset the index
    df = df.sort_values(by=['Datetime'])
    df = df.reset_index(drop=True)

    distinct_station_count = 1
    rolling_window = rolling_hours * distinct_station_count

    for column in columns:
        # Create a new column with the past "rolling_window" hours' average
        df[column+'_avg'] = df[column].rolling(window=rolling_window, min_periods=1).mean()
        # Fill missing values in the given "column" from "column_avg" if "column" value is missing
        # df[column].fillna(df[column+'_avg'], inplace=True)
        mask = df[column+'_avg'] > 0
        df.loc[mask, column] = df.loc[mask, column+'_avg']

        # Drop the temporary average column
        df = df.drop(columns=[column+'_avg'])

    return df


"""
We calculate the AQI, taking into account rolling averages, sub-indices, and data availability checks for various air quality parameters. The sub-indices are then used to determine the overall AQI, providing a single metric for air quality assessment.

Air Quality Index (AQI) Calculation
We define a function calculate_aqi(df) that calculates the Air Quality Index (AQI) based on given air quality parameters. Here's an explanation of the main components:

Sorting and Resetting Index:
The input DataFrame (df) is first sorted by 'StationId' and 'Datetime' to ensure the correct order for AQI calculation. The index is then reset for further processing.

Rolling Window Average:
Rolling window averages are calculated for specific air quality parameters, such as PM2.5, PM10, SO2, NOx, NH3, CO, and O3. These rolling averages are essential for determining the sub-indices.

Sub-Index Calculation:
Sub-indices are calculated for each air quality parameter based on its 24-hour or 8-hour rolling average. Different sub-index functions (get_PM25_subindex, get_PM10_subindex, etc.) are used for each parameter, mapping concentrations to corresponding sub-indices.

Data Availability Checks:
A series of checks are performed to ensure sufficient data availability for each parameter. If the checks fail, the AQI is set to NaN.

Temporary Columns Cleanup:
Temporary columns created during the AQI calculation are dropped to clean up the DataFrame.

AQI Column Update:
The 'AQI' column is created in the DataFrame based on the calculated AQI values.
"""
def calculate_aqi(df):
    """
    Calculate AQI (Air Quality Index).

    Parameters:
    - df (DataFrame): Input DataFrame.

    Returns:
    - DataFrame: The input DataFrame.
    """

    # Sort the DataFrame by 'StationId' first and then 'Datetime' for AQI calculation, and finally Reset the index
    df = df.sort_values(by=['Datetime'])
    df = df.reset_index(drop=True)

    # ====================================================================
    # 1. Calculate rolling window average values
    # ====================================================================
    df["PM2.5_24hr_avg"] = df["PM2.5 (ug/m3)"].rolling(window=24, min_periods=16).mean().values
    df["PM10_24hr_avg"] = df["PM10 (ug/m3)"].rolling(window=24, min_periods=16).mean().values
    df["SO2_24hr_avg"] = df["SO2 (ug/m3)"].rolling(window=24, min_periods=16).mean().values
    df["NOx_24hr_avg"] = df["NOx (ug/m3)"].rolling(window=24, min_periods=16).mean().values
    df["NH3_24hr_avg"] = df["NH3 (ug/m3)"].rolling(window=24, min_periods=16).mean().values
    df["CO_8hr_max"] = df["CO (ug/m3)"].rolling(window=8, min_periods=1).max().values
    df["O3_8hr_max"] = df["Ozone (ug/m3)"].rolling(window=8, min_periods=1).max().values

    # ====================================================================
    # 2. Sub-Index calculation
    # ====================================================================
    df["PM2.5_SubIndex"] = df["PM2.5_24hr_avg"].apply(lambda x: get_PM25_subindex(x))
    df["PM10_SubIndex"] = df["PM10_24hr_avg"].apply(lambda x: get_PM10_subindex(x))
    df["SO2_SubIndex"] = df["SO2_24hr_avg"].apply(lambda x: get_SO2_subindex(x))
    df["NOx_SubIndex"] = df["NOx_24hr_avg"].apply(lambda x: get_NOx_subindex(x))
    df["NH3_SubIndex"] = df["NH3_24hr_avg"].apply(lambda x: get_NH3_subindex(x))
    df["CO_SubIndex"] = df["CO_8hr_max"].apply(lambda x: get_CO_subindex(x))
    df["O3_SubIndex"] = df["O3_8hr_max"].apply(lambda x: get_O3_subindex(x))

    # ====================================================================
    # 3. Check for minimum data avaialbility
    # ====================================================================
    df["Checks"] = (df["PM2.5_SubIndex"] > 0).astype(int) + \
                (df["PM10_SubIndex"] > 0).astype(int) + \
                (df["SO2_SubIndex"] > 0).astype(int) + \
                (df["NOx_SubIndex"] > 0).astype(int) + \
                (df["NH3_SubIndex"] > 0).astype(int) + \
                (df["CO_SubIndex"] > 0).astype(int) + \
                (df["O3_SubIndex"] > 0).astype(int)

    df["AQI_temp"] = round(df[["PM2.5_SubIndex", "PM10_SubIndex", "SO2_SubIndex", "NOx_SubIndex",
                                    "NH3_SubIndex", "CO_SubIndex", "O3_SubIndex"]].max(axis = 1))

    df.loc[df["PM2.5_SubIndex"] + df["PM10_SubIndex"] <= 0, "AQI_temp"] = np.NaN
    df.loc[df.Checks < 3, "AQI_temp"] = np.NaN
    
    # If 'AQI' column not exists, then create 'AQI' column and initialize with NaN values
    if 'AQI' not in df.columns:
        df['AQI'] = np.nan

    # Update missing "AQI" value from "AQI_temp"
    df['AQI'] = df['AQI'].fillna(df['AQI_temp'])

    # Drop temporary columns created in AQI calculation
    temp_columns = [
        "PM2.5_24hr_avg", "PM10_24hr_avg", "SO2_24hr_avg", "NOx_24hr_avg", "NH3_24hr_avg", "CO_8hr_max", "O3_8hr_max",
        "PM2.5_SubIndex", "PM10_SubIndex", "SO2_SubIndex", "NOx_SubIndex", "NH3_SubIndex", "CO_SubIndex", "O3_SubIndex",
        "Checks", "AQI_temp"
        ]
    df = df.drop(columns=temp_columns)

    return df


## PM2.5 Sub-Index calculation
def get_PM25_subindex(x):
    if x <= 30:
        return x * 50 / 30
    elif x <= 60:
        return 50 + (x - 30) * 50 / 30
    elif x <= 90:
        return 100 + (x - 60) * 100 / 30
    elif x <= 120:
        return 200 + (x - 90) * 100 / 30
    elif x <= 250:
        return 300 + (x - 120) * 100 / 130
    elif x > 250:
        return 400 + (x - 250) * 100 / 130
    else:
        return 0

## PM10 Sub-Index calculation
def get_PM10_subindex(x):
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0

## SO2 Sub-Index calculation
def get_SO2_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0

## NOx Sub-Index calculation
def get_NOx_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0

## NH3 Sub-Index calculation
def get_NH3_subindex(x):
    if x <= 200:
        return x * 50 / 200
    elif x <= 400:
        return 50 + (x - 200) * 50 / 200
    elif x <= 800:
        return 100 + (x - 400) * 100 / 400
    elif x <= 1200:
        return 200 + (x - 800) * 100 / 400
    elif x <= 1800:
        return 300 + (x - 1200) * 100 / 600
    elif x > 1800:
        return 400 + (x - 1800) * 100 / 600
    else:
        return 0

## CO Sub-Index calculation
def get_CO_subindex(x):
    if x <= 1:
        return x * 50 / 1
    elif x <= 2:
        return 50 + (x - 1) * 50 / 1
    elif x <= 10:
        return 100 + (x - 2) * 100 / 8
    elif x <= 17:
        return 200 + (x - 10) * 100 / 7
    elif x <= 34:
        return 300 + (x - 17) * 100 / 17
    elif x > 34:
        return 400 + (x - 34) * 100 / 17
    else:
        return 0

## O3 Sub-Index calculation
def get_O3_subindex(x):
    if x <= 50:
        return x * 50 / 50
    elif x <= 100:
        return 50 + (x - 50) * 50 / 50
    elif x <= 168:
        return 100 + (x - 100) * 100 / 68
    elif x <= 208:
        return 200 + (x - 168) * 100 / 40
    elif x <= 748:
        return 300 + (x - 208) * 100 / 539
    elif x > 748:
        return 400 + (x - 400) * 100 / 539
    else:
        return 0





