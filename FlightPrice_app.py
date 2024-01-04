import numpy as np
import pickle
import streamlit as st
import pandas as pd
import bz2

#setting up the page title,icons

st.set_page_config(page_title="Flight Price Predictor",page_icon="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1677184597.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*")
st.sidebar.image('https://media.istockphoto.com/id/1392494719/photo/woman-with-pink-suitcase-and-passport-with-boarding-pass-standing-on-passengers-ladder-of.jpg?s=612x612&w=0&k=20&c=MVUZvIdaUmvRKdG-B5EEGGkIVFj51jss-b6IkxqY3fg=')
choice=st.sidebar.selectbox('Menu',('Home','Predict'))
st.sidebar.image('https://i.pinimg.com/736x/0d/1e/96/0d1e967cde176af6f8f0568af424d07b.jpg')
if(choice=='Home'):
    st.title('Welcome to Flight Price Predictor')
    st.text('🙏😊')
    st.text('Hi. Want to predict your flight ticket price❓❓')
    st.text('Click the Menu bar for further details😊')
    st.image('https://images.unsplash.com/opengraph/1x1.png?blend=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1567748534085-467f8a8a475d%3Fblend%3D000000%26blend-alpha%3D10%26blend-mode%3Dnormal%26crop%3Dfaces%252Cedges%26h%3D630%26mark%3Dhttps%253A%252F%252Fimages.unsplash.com%252Fopengraph%252Fsearch-input.png%253Fh%253D84%2526txt%253Dboarding%252Bpass%2526txt-align%253Dmiddle%25252Cleft%2526txt-clip%253Dellipsis%2526txt-color%253D000000%2526txt-pad%253D80%2526txt-size%253D40%2526txt-width%253D660%2526w%253D750%2526auto%253Dformat%2526fit%253Dcrop%2526q%253D60%26mark-align%3Dmiddle%252Ccenter%26mark-w%3D750%26w%3D1200%26auto%3Dformat%26fit%3Dcrop%26q%3D60%26ixid%3DM3wxMjA3fDB8MXxzZWFyY2h8Mnx8Ym9hcmRpbmclMjBwYXNzfGVufDB8fHx8MTcwMzczNjI4NXww%26ixlib%3Drb-4.0.3&blend-w=1&h=630&mark=https%3A%2F%2Fimages.unsplash.com%2Fopengraph%2Flogo.png&mark-align=top%2Cleft&mark-pad=50&mark-w=64&w=1200&auto=format&fit=crop&q=60')
    st.image('https://feeds.abplive.com/onecms/images/uploaded-images/2021/09/08/634259599cd6f60c24f9e67a5680c064_original.jpg')
elif(choice=='Predict'):
    st.text('Kindly fill your flight details to view the predicted price')
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
        st.header('Time to fly 😁✈🧳')


        


        
        
