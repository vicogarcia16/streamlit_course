import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Ejemplo 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Ejemplo 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Ejemplo 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Ejemplo 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2024, 1, 1, 11, 30),
     format="DD/MM/YY - hh:mm")
st.write("Start time:", start_time.strftime( "%d/%m/%Y - %H:%M"))