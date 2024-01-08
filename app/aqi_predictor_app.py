### import libraries
import numpy as np
import pandas as pd
import xgboost as xgb
import streamlit as st
import joblib

# Load the XGBoost model using joblib
model_path = "model/xgb_aqi_model____no_rolling_window_data.pkl"
xgb_model = joblib.load(model_path)

# Function to make prediction
def make_prediction(user_input):
    # Make user input as np array
    user_input_as_np_array = np.array(user_input).reshape(1, -1)

    # Convert user input np array to a DMatrix
    dmatrix_input = xgb.DMatrix(user_input_as_np_array)

    # Use the XGBoost model to predict
    prediction = xgb_model.predict(dmatrix_input)

    return prediction[0]

st.title("Live AQI Predictor App")

##############################################################################################################################
st.markdown("***")  # Horizontal line
##############################################################################################################################

st.subheader('A sample dataframe collected from test data')

# Sample data loading
df = pd.read_csv("model/sample_test.csv")
selected_row_index = st.dataframe(df) # Display the data in a table

# Display the data in a table and get the selected row index
selected_row_index = st.table(df).number_input("Select a row index", min_value=0, max_value=len(df)-1, step=1)
selected_row_data = df.iloc[selected_row_index] # Get the selected row's data

##############################################################################################################################
st.markdown("***")  # Horizontal line
##############################################################################################################################

st.subheader('AQI Predictor Tool')

# Input fields for user, organized into left and right sections
input_values_left = []
input_values_right = []

left_params = ['PM2.5 (ug/m3)', 'PM10 (ug/m3)', 'NOx (ug/m3)', 'NH3 (ug/m3)', 'SO2 (ug/m3)', 'CO (ug/m3)', 'Ozone (ug/m3)']
right_params = ['RH (%)', 'WS (m/s)', 'WD (degree)', 'BP (mmHg)', 'AT (degree C)', 'RF (mm)', 'SR (W/mt2)']

col1, col2 = st.columns(2)

for param in left_params:
    input_value = col1.number_input(f"Enter {param}", value=selected_row_data[param], min_value=0.0, step=0.1, format="%f")
    input_values_left.append(input_value)

for param in right_params:
    input_value = col2.number_input(f"Enter {param}", value=selected_row_data[param], min_value=0.0, step=0.1, format="%f")
    input_values_right.append(input_value)

# Combine the left and right input values
input_values = input_values_left + input_values_right

# Make prediction button
if st.button("Make Prediction"):
    # Make prediction using the entered values
    predicted_value = make_prediction(input_values)
    actual_value = df.loc[selected_row_index, 'y_AQI']

    # Display the predicted value
    st.success(f"Predicted Air Quality Index: **{predicted_value:.2f}**")
    st.markdown(f"[Actual AQI: <span style='color:orange'>{actual_value}</span>]", unsafe_allow_html=True)
