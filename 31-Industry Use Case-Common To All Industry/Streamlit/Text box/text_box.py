%%writefile text_box.py


#File name     :  text_box.py
#Purpose       :  A simple text box for streamlit using python
#Author        :  Deepsphere.AI, INC.
#Date and Time :  24/06/2021 18:30 hrs

import streamlit as vAR_st
from PIL import Image
import urllib.request


#for Setting the page layout to wide
vAR_st.set_page_config(layout="wide")

#for having the logo and title in the same line we use vAR.st_beta_columns() and make the ratio accordingly 
vAR_logo, vAR_title = vAR_st.beta_columns((6,50))
with vAR_logo:
#Urllib module is the URL handling module for python, It uses the urlopen function and is able to fetch URLs 
  urllib.request.urlretrieve('https://raw.githubusercontent.com/DeepsphereAI/IndustryUseCases/main/31-Industry%20Use%20Case-Common%20To%20All%20Industry/Streamlit/Logo/logo.jpg',"logo.jpg")
  logo = Image.open("logo.jpg")
  vAR_st.image(logo)
with vAR_title:
#setting font size and colour for the title 
  vAR_st.markdown("""
  <style>
  .big-font {
    font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)

  vAR_st.markdown('<p class="big-font">Master Streamlit With DeepSphere.AI Personalized Learning Platform', unsafe_allow_html=True)

#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: green;'>A Simple Text Box</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

col1, col2, col3 = vAR_st.beta_columns((1,1,1))
with col2:
#with vAR_st.text_input() we can take the user input
  vAR_input = vAR_st.text_input('Favorite colour')

col1, col2, col3 = vAR_st.beta_columns((5,1,5))
with col2:
#for the submit button use vAR_st.button()
  button_submit = vAR_st.button('submit')

#to display the user input after hiting the submit button
if button_submit:
  col1, col2, col3 = vAR_st.beta_columns((1,1,1))
  with col2:
    vAR_st.subheader('Favorite colour')
    vAR_st.info(vAR_input)



#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.

