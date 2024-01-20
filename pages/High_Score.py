import csv
import pandas
import streamlit as st

highScore = pandas.read_csv('highScore.csv', delimiter=",")

with st.container():
    x1, x2, x3 = st.columns([1,2,1])
    with x2:
        st.dataframe(highScore)