import streamlit as st
import pandas as pd

data = {
            'Course Name': ['DevOps', 'Azure2'], 
            'Duration': ['30 days', '30days']
    }
df = pd.DataFrame(data)

st.dataframe(df)