import streamlit as st
import numpy as np
import pandas as pd

st.title("Elementos de interfase :iphone:")

###
# static table
###
st.header("tabla statica")
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=("col %d" % i for i in range(20)))
st.table(dataframe)

###
# Dynamic DF
###
st.header("Dynam,ic DataFrame")
dataframe=pd.DataFrame(
    np.random.rand(10,20),
    columns=("col %d" % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

###
# Chart
###
st.header("Line Chart")
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)
