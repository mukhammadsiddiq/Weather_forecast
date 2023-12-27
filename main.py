import streamlit as st
import plotly.express as px

st.title("Weather forecast for the days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the numbers of forecasted days!")
option = st.selectbox("Select data to view", ("temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

dates = ["2025-10-14", "2025-10-15", "2025-10-16"]
temperature = [5, 20, 8]
temperature = [days * i for i in temperature]

figure = px.line(x=dates, y=temperature, labels={"x": "dates","y": "temperatures (C)"})
st.plotly_chart(figure)
