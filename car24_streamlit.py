import streamlit as st
import pandas as pd 
import numpy as np
import joblib

st.title('Car Prediction App')

encode_dict={
    'Fuel' :{'DIESEL':1,'PETROL':2,'CNG':3,'LPG':4,'ELECTRIC':5},
    'Drive' : {'Manual':1,'Automatic':2},
    'Type':{'HatchBack':1,'Sedan':2,'SUV':3,'Lux_SUV':4,'Lux_sedan':5}
}

model=joblib.load('car24-car-price-model.joblib')

year=st.slider('Manufacturing Year',min_value=1990,max_value=2023,value=2015,step=1)
Fuel_type=st.selectbox('Fuel_Type',['DIESEL','PETROL','CNG','LPG','ELECTRIC'])
Drive_Type=st.selectbox('Drive_Type',['Manual','Automatic'])
Type=st.selectbox('Type',['HatchBack','Sedan','SUV','Lux_SUV','Lux_sedan'])
Owner=st.selectbox('Owner',['1','2','3','4'])
Distance=st.number_input('Kilometer_Driven',min_value=0,max_value=1000000,value=50000,step=1000)

scaler=joblib.load('scaler.pkl')

def model_pred(year,Fuel_type,Drive_Type,Type,Owner,Distance):
    Fuel_type_encode=encode_dict['Fuel'][Fuel_type]
    Drive_Type_encode=encode_dict['Drive'][Drive_Type]
    Type_encode=encode_dict['Type'][Type]
    data=[[float(year),float(Distance),float(Owner),Fuel_type_encode,Drive_Type_encode,Type_encode]]
    data=scaler.transform(data)
    prediction=model.predict(data)
    return(round(prediction[0],2))


if st.button('Predict'):
    price=model_pred(year,Fuel_type,Drive_Type,Type,Owner,Distance)
    st.write(f'Predicted card price is {price} Lakhs(approx)')
else:
    st.write('Click on predict button for prediction price !!')
