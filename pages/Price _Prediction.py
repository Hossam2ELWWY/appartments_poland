import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
#from PIL import Image
#from ydata_profiling import ProfileReport
#from streamlit_pandas_profiling import st_profile_report 
df = pd.read_csv("apartments_rent_pl_2024_01.csv")
df.dropna(subset=[ 'schoolDistance' , 'hasElevator','pharmacyDistance',
                  'kindergartenDistance', 'postOfficeDistance' , 'floorCount' , 'clinicDistance',  
                   'poiCount']
          , inplace=True)
df['type'].fillna(df['type'].mode()[0] , inplace=True)
df['floor'].fillna(df['floor'].mode()[0] ,inplace = True)
df['floorCount'].fillna(df['floorCount'].mode()[0] ,inplace = True)
df['buildYear'].fillna(df['buildYear'].mode()[0] , inplace=True)
df['squareMeters_cat'] = pd.cut(df['squareMeters'] , bins = [0 , 50 , 100 ,150] , labels = ["<50" , "50-100" , ">100"])
df.drop(columns=['condition' , 'id' , 'buildingMaterial' , 'collegeDistance' , 'restaurantDistance'], inplace=True)
df = df[df['floor'] < 20]
st.write('Welcome to the Price Prediction Page 📈  ')
#face = social_media[social_media['platform'] == 'Facebook']
floor_user = st.selectbox('floor' , df['floor'].unique() )
hasElevator = st.selectbox('hasElevator' , df['hasElevator'].unique() )
security = st.selectbox('security' , df['hasSecurity'].unique() )
balcony = st.selectbox('balcony' , df['hasBalcony'].unique() )
rooms_user = st.selectbox('rooms' , df['rooms'].unique() )
square_meters_user = st.selectbox('squareMeters' , df['squareMeters_cat'].unique() )
filtered_data = df[
    (df['floor'] == floor_user) &
    (df['hasElevator'] == hasElevator) &
    (df['hasSecurity'] == security) &
    (df['hasBalcony'] == balcony) &
    (df['rooms'] == rooms_user) &
    (df['squareMeters_cat'] == square_meters_user)
]
prediction = filtered_data['price'].mean()
if st.button('Predict'):
    try :
        prediction.round(2)
    except :
        prediction = 'nan' 
    if prediction == 'nan' :
        st.warning('there is no apartement with your needs')
    else:
        st.markdown('<p style="font-size:24px; color:red;">The predicted price is.</p>', unsafe_allow_html=True)
        st.success(int(filtered_data['price'].mean().round(0))) 
       

# st.write('### Result')
# if st.button('Predict'):
    

