import numpy as np
import pandas as pd
import streamlit as st
import plotly_express as px
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def app():
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV 📄 file", type=["csv"])
        st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

    # Pandas Profiling Report
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv

        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        global x_columns, y_columns
        try:
            x_columns = list(df.select_dtypes(['datetime64', 'float']))
            y_columns = list(df.select_dtypes(['integer', 'float']))

        except Exception as e:
            print(e)
            st.write("Please upload dataset in the sidebar > of the application\n"
                     "to visualize your own data")

        # add a select widget to sidebar
        chart_select = st.sidebar.selectbox(
            label="Select the chart type",
            options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot'])

        # Scatter Plots

        if chart_select == 'Scatterplots':
            st.sidebar.subheader("Scatterplot settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=x_columns)
                y_values = st.sidebar.selectbox('Y axis', options=y_columns)
                plot = px.scatter(data_frame=df, width=750, size_max=9, size=y_values, color=y_values,
                                  color_continuous_scale=px.colors.cyclical.mrybm, x=x_values, y=y_values, log_x=True)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)

        # Line plots

        if chart_select == 'Lineplots':
            st.sidebar.subheader("Lineplots settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=x_columns)
                y_values = st.sidebar.selectbox('Y axis', options=y_columns)
                plot = px.line(data_frame=df, x=x_values, y=y_values, color=y_values)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)

        # Histogram

        if chart_select == 'Histogram':
            st.sidebar.subheader("Histogram settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=x_columns)
                y_values = st.sidebar.selectbox('Y axis', options=y_columns)
                plot = px.histogram(data_frame=df, x=x_values, y=y_values)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)

        # Box plots

        if chart_select == 'Boxplot':
            st.sidebar.subheader("Boxplot settings")
            try:
                x_values = st.sidebar.selectbox('X axis', options=x_columns)
                y_values = st.sidebar.selectbox('Y axis', options=y_columns)
                plot = px.box(data_frame=df, x=x_values, y=y_values, color=x_values)
                st.plotly_chart(plot)
            except Exception as e:
                print(e)
        st.write('---')
        st.header('**Report of Your Dataset**')
        st_profile_report(pr)

    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Press to use Example Dataset'):
            # Example data
            @st.cache
            def load_data():
                a = pd.DataFrame(
                    np.random.rand(100, 5),
                    columns=['a', 'b', 'c', 'd', 'e']
                )
                return a

            df = load_data()
            pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Report of Your Dataset**')
            st_profile_report(pr)
