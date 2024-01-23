import csv
import pandas
import streamlit as st
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///highScores.db")
conn = engine.connect()

highScore = conn.execute("SELECT * FROM highScores").fetchone()
conn.commit()

with st.container():
    x1, x2, x3 = st.columns([1,2,1])
    with x2:
        st.dataframe(highScore)
