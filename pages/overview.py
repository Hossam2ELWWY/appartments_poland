import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
# from PIL import Image
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report 
df = pd.read_csv("apartments_pl_2024_01.csv")
df.drop(columns=['condition' , 'id' , 'buildingMaterial' , 'collegeDistance' , 'restaurantDistance'], inplace=True)
st.title('Welcome to the Overview Page 📈  ')


st.header('average price appartments in Poland'  )
st.plotly_chart( px.box(df , x = 'price' , template= 'plotly_dark' ,color_discrete_sequence=px.colors.sequential.Electric_r )
,use_container_width=True) 




c1,c33,c2 = st.columns([4,1,4])


with c1 :
    st.title('Square meters vs price ')
    st.plotly_chart(px.scatter(df , x = 'squareMeters' , y = 'price' , template= 'plotly_dark' ,
                               color_discrete_sequence=px.colors.sequential.Electric_r ,width=600,height=400 ))
    st.markdown('<p style="font-size:24px; color:orange;">More square meters means more price.</p>', unsafe_allow_html=True)

with c2:

    st.title('City vs price ')
    st.plotly_chart(px.bar( df.groupby('city')['price'].mean().reset_index(), x= 'price' , y = 'city' , template= 'plotly_dark' ,
       color_discrete_sequence=px.colors.sequential.Electric_r , color='price'
       ,width=600,height=400))
    #smumarry chart as text
    st.markdown('<p style="font-size:24px; color:orange;">The highest average real estate in the city in Poland is located in Warszawa.</p>', unsafe_allow_html=True)
c1,c33,c2 = st.columns([4,1,4]) 
with c1 : 
    st.title('Rooms vs price ')
    st.plotly_chart(px.bar(df.groupby('rooms')['price'].median().reset_index() , x = 'rooms' , y= 'price' , template= 'plotly_dark' ,
       color_discrete_sequence=px.colors.sequential.Electric_r ,color='rooms', title='Average apartment prices for rooms'))
    st.markdown('<p style="font-size:24px; color:orange;">More rooms means more price.</p>', unsafe_allow_html=True)
with c2 :
    st.title('Floor vs price ')
    st.plotly_chart(px.line(df.groupby('floor')['price'].sum().reset_index().sort_values(by='floor') , x= 'floor' , y= 'price' , template= 'plotly_dark' ,
        color_discrete_sequence=px.colors.sequential.Electric_r , title= 'Total price VS floor' ))
    st.markdown('<p style="font-size:24px; color:orange;">The highest price is in the ground floor.</p>', unsafe_allow_html=True)
c1,c33,c2 = st.columns([4,1,4])
with c1 :
    st.title('Building year vs price ')
    bins = [1850 ,1900, 2000, 2024]  
    labels = ['old', 'medium', 'modren']
    df['distance_year_group'] = pd.cut(df['buildYear'], bins=bins, labels=labels)
    st.plotly_chart(px.bar(df.groupby('distance_year_group')['price'].sum().reset_index().sort_values(by='price')
     , x='distance_year_group' , y = 'price' , template= 'plotly_dark' 
     ,color_discrete_sequence=px.colors.sequential.Electric_r ,
     color='distance_year_group'))
    st.markdown('<p style="font-size:24px; color:orange;">The highest price is in the modern age.</p>', unsafe_allow_html=True)
    
with c2 : 
    st.title('ownership Vs Price ')
    st.plotly_chart(px.bar(df.groupby('ownership')['price'].sum().reset_index().sort_values(by='price')
     , x='ownership' , y = 'price' , template= 'plotly_dark' 
     ,color_discrete_sequence=px.colors.sequential.Electric_r ,
     color='ownership'))
    st.markdown('<p style="font-size:24px; color:orange;">The highest price is in the condominium ownership.</p>', unsafe_allow_html=True)

c1,c33,c2 = st.columns([4,1,4])
with c1 : 
    bins = [0,0.4,0.9,2.56]  
    labels = ['Near', 'Medium', 'Far']
    df['distance_clinic_group'] = pd.cut(df['clinicDistance'], bins=bins, labels=labels)

            
    st.title("Rooms Vs price Vs distance_clinic ")
    st.plotly_chart(px.bar(df.groupby(['rooms' , 'distance_clinic_group'])['price'].mean().reset_index().sort_values(by='price') ,
    x = 'rooms' , y = 'price' , color='distance_clinic_group' , color_discrete_sequence=px.colors.sequential.Electric_r , title= 'price VS rooms VS distance_clinic' , 
     barmode='group' , template='plotly_dark' ))
    st.markdown('<p style="font-size:24px; color:orange;">The highest price is in the nearest distance and in the most rooms.</p>', unsafe_allow_html=True)

with c2 :
    st.title("Rooms Vs price Vs Security ")
    grouped_df = df.groupby(['rooms', 'hasSecurity'])['price'].mean().reset_index()
    st.plotly_chart(
px.line(grouped_df, x='rooms', y='price', color='hasSecurity',
             labels={'rooms': 'Number of Rooms', 'price': 'Average Price (PLN)', 'hasSecurity': 'has Security'},
             title='Average Price vs Number of Rooms by Security', template='plotly_dark',color_discrete_sequence=px.colors.sequential.Electric_r ) 

)    
    st.markdown('<p style="font-size:24px; color:orange;">The highest price is the most rooms and has security .</p>', unsafe_allow_html=True)
df['squareMeters_cat'] = pd.cut(df['squareMeters'] , bins = [0 , 50 , 100 ,150] , labels = ["<50" , "50-100" , ">100"])
st.header('squareMeters_cat Vs price Vs rooms') 
st.plotly_chart(px.box(df, x='squareMeters_cat', y='price', color='rooms',
             labels={'squareMeters_cat': 'Square Meters Category', 'price': 'Price (PLN)', 'rooms': 'Number of Rooms'},
             title='Price Distribution by Square Meters Category and Number of Rooms' , template='plotly_dark')
,use_container_width=True)   
st.markdown('<p style="font-size:24px; color:orange;">The highest price is in the most rooms and in the most square meters.</p>', unsafe_allow_html=True)
