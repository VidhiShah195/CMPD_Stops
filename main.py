# conda activate streamlit_2
# pip freeze so you freeze the version of the packages, stremlit and python so someone can run it 10 years later and get the same results. 
import streamlit as st
import altair as alt
import pandas as pd

st.write('CMPD Traffic Stops')
st.write('practice for class')


@st.cache_data
def load_data(csv):
    df=pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

chart = (
    alt.Chart(stops).mark_bar().encode(
        alt.X("Driver_Age", bin=alt.Bin(maxbins=10)),
        alt.Y('count()'),
        tooltip = alt.Tooltip(['Driver_Age','count()'])
    )
)

st.altair_chart(chart)


