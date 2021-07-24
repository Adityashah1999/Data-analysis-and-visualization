import streamlit as st
from multiapp import MultiApp
from apps import dataVisualization, covid, model

# import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Explore Covid-19 Data", covid.app)
app.add_app("Visualize your Own Dataset", dataVisualization.app)
app.add_app("Covid-19 Prediction Model", model.app)
# The main app
app.run()
