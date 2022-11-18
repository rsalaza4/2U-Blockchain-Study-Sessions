# STREAMLIT TUTORIAL

# Import libraries and dependencies
import streamlit as st
import pandas as pd
import time

# DISPLAY TEXT

# Title
st.title('My title')

# Header
st.header('My header')

# Subheader
st.subheader('My subheader')

# Text
st.text("This is some text")

# Markdown
st.markdown("**Markdown Text**")

# LaTex
st.latex(r'''e^{i\pi} + 1 = 0''')

# Write a string
st.write('Most objects')

# Write a list
st.write(['Hellow', 'Wolrd', 42])

# Code
st.code('for i in range(8): function()')

# DISPLAY DATA

# Read csv file
df = pd.read_csv("my_file.csv")

# Display dataframe
st.dataframe(df)

# Display table
st.table(df.iloc[0:5])

# Display JSON
st.json({"numbers":[0,1,2,3,4], "letters":["a","b","c","d","e"]})

# DISPLAY CHARTS

# Line chart
st.line_chart(df["column_1"])

# Area chart
st.area_chart(df["column_1"])

# Bar chart
st.bar_chart(df["column_1"])

# DISPLAY INTERACTIVE WIDGETS

# Button
st.button('Click me')

# Checkbox
st.checkbox('I agree')

# Radio button
st.radio('Pick one', ['cats', 'dogs'])

# Selectbox
st.selectbox('Pick one', ['cats', 'dogs'])

# Multiselect
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

# Slider
st.slider('Pick a number', 0, 100)

# Select slider
st.select_slider('Pick a size', ['S', 'M', 'L'])

# Text input
st.text_input('First name')

# Number input
st.number_input('Pick a number', 0, 10)

# Text Area
st.text_area('Text to translate')

# Date input
st.date_input('Your birthday')

# Time input
st.time_input('Meeting time')

# File uploader
st.file_uploader('Upload a CSV')

# Download file
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

# Camera input
st.camera_input("Take a picture")

# Color picker
st.color_picker('Pick a color')

# DISPLAY PROGRESS AND STATUS

# Static Progress Bar
st.progress(value=50)

with st.spinner(text="In progress"):
	time.sleep(5)
	st.text("Done!")

# Balloons
if st.button("Press for balloons"):
	st.balloons()

# Success
st.success("Success!")

# Info
st.info("Information")

# Warning
st.warning("This is a warning!")

# Error
st.error("This is an error. Danger!")

# Exception
st.exception("NameError('name variable not defined')")

# Get Help Info About Python
st.help(range)

# DISPLAY MEDIA 

# Loading images
from PIL import Image
img = Image.open("python.png") # this file must be inside the Streamlit folder directory!
st.image(img, width=700,caption="Simple Image")

# Loading videos
# vid_file = open("example.mp4","rb")
# vide_bytes = vid_file.read()
# st.video(vid_file)

# Loading audios
# audio_file = opne("examplemusic.mp3","rb").read()
# st.audio(audio_file, format='audio/mp3')

# CONTROL FLOW

# Stop code execution
st.stop()