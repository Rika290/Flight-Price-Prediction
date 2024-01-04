import numpy as np
import pickle
import streamlit as st
import pandas as pd
import bz2

#setting up the page title,icons

st.set_page_config(page_title="Flight Price Predictor",page_icon="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1677184597.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*")
st.title('Welcome')
st.text('Predict the flight price')
choice=st.sidebar.selectbox('Menu',('Home','Predict'))
if(choice=='Home'):
    st.image('https://feeds.abplive.com/onecms/images/uploaded-images/2021/09/08/634259599cd6f60c24f9e67a5680c064_original.jpg')
elif(choice=='Predict'):
    st.image('https://media.istockphoto.com/id/955952680/photo/passengers-commercial-airplane-flying-above-clouds.jpg?s=612x612&w=0&k=20&c=9bZsGq8-uZaPXR1lCztXur4JRlI1gNksYOOSZzfXPAA=')
    ch=st.toggle('Airline',['Airline name'])
    if ch:
        q=pd.DataFrame(data=['Vistara','Air_India','Indigo','GO_FIRST','AirAsia','SpiceJet'],columns=['Airline Name'])
        q['Code']=[5,1,3,2,0,4]
        st.dataframe(q)
    cv=st.toggle('Place & Time',['Source'])
    if cv:
        q=pd.DataFrame(data=['Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'],columns=['Source City'])
        q['Code for Source City']=[2,5,0,4,3,1]
        q['Destination City']=['Mumbai','Delhi','Bangalore','Kolkata','Hyderabad','Chennai']
        q['Code for Destination City']=[5,2,0,4,3,1]        
        q['Departure time']=['Morning','Early_Morning','Evening','Night','Afternoon','Late_Night']
        q['Code for Departure']=[4,1,2,5,0,3]
        q['Arrival time']=['Night','Evening','Morning','Afternoon','Early_Morning','Late_Night']
        q['Code for Arrival time']=[5,2,4,0,1,3]
        st.dataframe(q)
    by=st.toggle('Stops',['Stop'])
    if by:
        q=pd.DataFrame(data=['one','zero','two_or_more'])
        q['Code']=[0,2,1]
        st.dataframe(q)
    bh=st.toggle('Class',['Class'])
    if bh:
        q=pd.DataFrame(data=['Economy','Business'],columns=['Class'])
        q['Code']=[1,0]
        st.dataframe(q)
    a=st.number_input('Airline name')
    b=st.number_input('Source City')
    c=st.number_input('Departure time')
    d=st.number_input('stops')
    e=st.number_input('Arrival time')
    f=st.number_input('Destination City')
    g=st.number_input('Class')
    h=st.number_input('Duration')
    i=st.number_input('Days left')
    btn=st.button('Check')
    if btn:
        def decompress_pickle(file):
            data = bz2.BZ2File(file, 'rb')
            data = pickle.load(data)
            return data
            model = decompress_pickle('Flight.pbz2')            
            p=model.predict([[a,b,c,d,e,f,g,h,i]])
            st.write("The predicted price is:-",p[0],'Rs')


        


        
        
