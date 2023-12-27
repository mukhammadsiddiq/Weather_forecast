import streamlit as st

st.title("Weather forecast for the days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the numbers of forecasted days!")
option = st.selectbox("Select data to view", ("temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")
