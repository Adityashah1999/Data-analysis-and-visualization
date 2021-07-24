import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


def app():
    st.title(" Covid-19 Prediction 🔮 Model")
    a = st.slider('select a day range from 0 to 5', min_value=0, max_value=5, value=2)
    data = pd.read_csv('total_Cases.csv')
    nan_value = float("NaN")
    data.replace("", nan_value, inplace=True)
    data.dropna(subset=['id', 'cases'], inplace=True)
    m = (data.dtypes == 'float')
    data.loc[:, m] = data.loc[:, m].astype(int)

    x = np.array(data['id']).reshape(-1, 1)
    y = np.array(data['cases']).reshape(-1, 1)
    plt.plot(y, '-m')

    polyFeat = PolynomialFeatures(degree=5)
    x = polyFeat.fit_transform(x)

    model = linear_model.LinearRegression()
    model.fit(x, y)
    accuracy = model.score(x, y)
    st.write(f'Accuracy:{round(accuracy * 100, 3)} %')
    y0 = model.predict(x)
    plt.plot(y0, '--b')

    # prediction
    st.write(f'Prediction - Cass after {a} days:', end='')
    st.write(round(int(model.predict(polyFeat.fit_transform([[504 + a]]))) / 1000000, 2), 'Million Cases')
    st.pyplot(plt)
    st.write(f'Purple line represents original data while blue dash line is predicted data')
    st.write(f'last updated 📅 date data: June 6, 2021')


