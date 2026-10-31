import streamlit as st
import pandas as pd

st.title("Digital Addiction Analysis Tool")

# Load the dataset
df = pd.read_csv("digital_addiction_dataset (1).csv")

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Summary Statistics")
st.write(df.describe())
