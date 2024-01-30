import csv
import pandas
import streamlit as st
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///highScores.db")
conn = engine.connect()

# Insert some data with conn.session.

conn.execute(text('''
    CREATE TABLE IF NOT EXISTS players (
        uuid TEXT PRIMARY KEY, 
        Date TEXT, 
        Name TEXT, 
        Score INT
    );
'''))

conn.commit()


query = conn.execute(text("SELECT * FROM players"))
conn.commit()

highScores = pandas.DataFrame(query.all(), columns=query.keys())
highScores = highScores.drop('uuid', axis=1)

with st.container():
    x1, x2, x3 = st.columns([1,2,1])
    with x2:
        st.dataframe(highScores)
