import streamlit as st
from plotly import express as px
import pandas as pd

st.set_page_config(
    page_title="Mill vs Bill",
    page_icon="📊",
)

st.title("📊 Mill vs Bill")
st.caption("Visualize the difference between a million and a billion.")

df = pd.DataFrame({
    "Number": ["1M", "10M", "100M", "1B"],
    "Value": [1_000_000, 10_000_000, 100_000_000, 1_000_000_000]
})
df['Number'] = df['Number'].astype(str)
df = df.sort_values('Value', ascending=False)

p = px.bar(
    df,
    y='Number',
    x='Value',
    color='Number',
    orientation='h'
)
st.plotly_chart(p, use_container_width=True)