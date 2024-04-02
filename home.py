import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image
#from ydata_profiling import ProfileReport
#from streamlit_pandas_profiling import st_profile_report 
df = pd.read_csv("apartments_rent_pl_2024_01.csv")
df.drop(columns=['condition' , 'id' , 'buildingMaterial' , 'collegeDistance' , 'restaurantDistance' , 'longitude', 'latitude'], inplace=True)
df.dropna(subset=[ 'schoolDistance' , 'hasElevator','pharmacyDistance',
                  'kindergartenDistance', 'postOfficeDistance' , 'floorCount' , 'clinicDistance',  
                   'poiCount']
          , inplace=True)
df['type'].fillna(df['type'].mode()[0] , inplace=True)
df['floor'].fillna(df['floor'].mode()[0] ,inplace = True)
df['floorCount'].fillna(df['floorCount'].mode()[0] ,inplace = True)
df['buildYear'].fillna(df['buildYear'].mode()[0] , inplace=True)
st.title('Welcome to the Home Page 🤓')

st.image(r"city-paris-france-building-wallpaper-preview.jpg" , width=900)
st.snow()
st.subheader('This EDA App is for appartments in poland' )
st.write("<span style='color: red; font-family: Arial, sans-serif; font-size: 20px;'>Data link <a href='https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland/data'>here</a></span>", unsafe_allow_html=True)
sample = st.checkbox("show sample of data")  
if sample :
    st.write(df.sample())
head = st.checkbox("show head of data ")
if head :
    st.write(df.head())    



# Display information about the dataset
st.write("<span style='font-size: 24px;color: red;'>About Dataset:</span>", unsafe_allow_html=True)
st.write("The dataset contains apartment sales and rent offers from the 15 largest cities in Poland:")
st.write("- Warsaw")
st.write("- Lodz")
st.write("- Krakow")
st.write("- Wroclaw")
st.write("- Poznan")
st.write("- Gdansk")
st.write("- Szczecin")
st.write("- Bydgoszcz")
st.write("- Lublin")
st.write("- Katowice")
st.write("- Bialystok")
st.write("- Czestochowa")
st.write("The data comes from local websites with apartments for sale.")
st.write("To fully capture the neighborhood of each apartment better, each offer was extended by data from the Open Street Map with distances to points of interest (POI).")
st.write("The data is collected monthly and covers a timespan between August 2023 and March 2024.")

# if st.button('Press to show Report about Dataset'):
#     pr = ProfileReport(df, explorative=True)
#     st.header('**Pandas Profiling Report**')
#     st_profile_report(pr)
