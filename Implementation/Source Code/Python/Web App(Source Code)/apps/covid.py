import pandas as pd
import plotly_express as px
import numpy as np
import streamlit as st


def app():
    st.info('It takes a while ⏳ to fetch data. You can see the data 👇 once its loaded.')
    st.title('Covid-19 Live Data Explorer')
    st.sidebar.image("https://media.giphy.com/media/d7ksD7AarGUDz0NmxU/giphy.gif", width=300)
    covid = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/Covid-19-Preprocessed-Dataset/master/preprocessed/covid_19_data_cleaned.csv')
    covid = covid.drop(["Province/State", "Lat", "Long"], axis=1)
    covid.columns = ['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths', 'Active']
    covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
    st.write(covid)

    country_options = covid['Country'].unique().tolist()
    date_options = covid['Date'].unique().tolist()
    #date = st.selectbox('Which date would you like to see?', date_options, 100)
    country = st.multiselect('Which country 🌎 would you like to see?', country_options, ['US', 'India', 'Italy'])
    covid = covid[covid['Country'].isin(country)]
    #covid = covid[covid['Date'] == date]
    cases_select = st.selectbox(
        label="Select the Case type",
        options=['Confirmed', 'Recovered', 'Deaths'])

    if cases_select == 'Confirmed':
        st.subheader("Confirmed Cases")
        fig = px.bar(covid, x="Country", y="Confirmed", color="Country")
        fig.update_layout(height=600, width=800)
        
        st.write(fig)

        st.subheader("Date-wise Area plot")
        fig1 = px.area(covid, x="Date", y="Confirmed", color="Country")
        fig1.update_layout(height=600, width=800)
        st.write(fig1)

    elif cases_select == 'Recovered':
        st.subheader("Recovered Cases")
        fig = px.bar(covid, x="Country", y="Recovered", color="Country")
        fig.update_layout(height=600, width=800)
        st.write(fig)

        fig2 = px.line(covid, x="Date", y="Recovered", color="Country")
        fig2.update_layout(height=600, width=800)
        st.write(fig2)
    else:
        st.subheader("Deaths Cases")
        fig = px.bar(covid, x="Country", y="Deaths", color="Country")
        fig.update_layout(height=600, width=800)
        st.write(fig)

        fig3 = px.line(covid, x='Date', y="Deaths", color="Country")
        fig3.update_layout(height=600, width=800)
        st.write(fig3)
        
    st.header(f'Credits')    
    st.markdown("""
    **Thank you for using my application!**
    
    The dataset used to feed this application is provided by [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).   
    """)
