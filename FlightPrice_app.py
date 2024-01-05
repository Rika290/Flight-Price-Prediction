import numpy as np
import pickle
import streamlit as st
import pandas as pd
import bz2

#setting up the page title,icons

st.set_page_config(page_title="Flight Price Predictor",page_icon="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1677184597.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*")
st.sidebar.image('https://wallpapers.com/images/featured/airplane-window-bubpfgncon8zd3ew.jpg')
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
    ch=st.selectbox('Airline✈',('Vistara','Air India','Indigo','GO FIRST','AirAsia','SpiceJet'))
    if(ch=='Vistara'):
        a=5
    elif(ch=='Air India'):
        a=1
    elif(ch=='Indigo'):
        a=3
    elif(ch=='GO FIRST'):
        a=2
    elif(ch=='AirAsia'):
        a=0
    elif(ch=='SpiceJet'):
        a=4        
    cg=st.selectbox('From',('Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'))
    if(cg=='Delhi'):
        b=2
    elif(cg=='Mumbai'):
        b=5
    elif(cg=='Bangalore'):
        b=0
    elif(cg=='Kolkata'):
        b=4
    elif(cg=='Hyderabad'):
        b=3
    else:
        b=1
    cf=st.selectbox('Departure time',('Morning','Early Morning','Evening','Night','Afternoon','Late Night'))
    if(cf=='Morning'):
        c=4
    elif(cf=='Early Morning'):
        c=1
    elif(cf=='Evening'):
        c=2
    elif(cf=='Night'):
        c=5
    elif(cf=='Afternoon'):
        c=0
    elif(cf=='Late Night'):
        c=3
    ci=st.selectbox('Stops',('one','zero','two or more'))
    if(ci=='one'):
        d=0
    elif(ci=='zero'):
        d=2
    elif(ci=='two or more'):
        d=1
    cs=st.selectbox('Arrival time',('Night','Evening','Morning','Afternoon','Early Morning','Late Night'))
    if(cs=='Night'):
        e=5
    elif(cs=='Evening'):
        e=2
    elif(cs=='Morning'):
        e=4
    elif(cs=='Afternoon'):
        e=0
    elif(cs=='Early Morning'):
        e=1
    elif(cs=='Late Night'):
        e=3
    cx=st.selectbox('Destination',('Mumbai','Delhi','Bangalore','Kolkata','Hyderabad','Chennai'))
    if(cx=='Mumbai'):
        f=5
    elif(cx=='Delhi'):
        f=2
    elif(cx=='Bangalore'):
        f=0
    elif(cx=='Kolkata'):
        f=4
    elif(cx=='Hyderabad'):
        f=3
    elif(cx=='Chennai'):
        f=1
    cb=st.selectbox('Class',('Economy','Business'))
    if(cb=='Economy'):
        g=1
    else:
        g=0        
    h=st.number_input('Duration 🕗')
    i=st.number_input('Days left 📅')
    btn=st.button('Check')
    if btn:
        def decompress_pickle(file):
            data = bz2.BZ2File(file, 'rb')
            data = pickle.load(data)
            return data
        model = decompress_pickle('Flight.pbz2')
        pred=model.predict([[a,b,c,d,e,f,g,h,i]])
        st.write("The predicted price is:-",pred[0],'Rs')
        st.header('Time to fly 😁✈🧳')
        st.image('https://image.cnbcfm.com/api/v1/image/106537227-1589463911434gettyimages-890234318.jpeg?v=1589463982&w=1600&h=900')
    
        



        


        
        
