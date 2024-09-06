'''
Name:           faruq_quotes_v2.py
Version:        2
Description:    Faruq from Battle Bots fortune cookie style app
'''

import streamlit as st
import random

from faruq_quotes_data_v2 import faruq_quotes_list
quote = random.randint(0,len(faruq_quotes_list)-1)

st.image("faruq_image.jpg",width=175)
st.html(faruq_quotes_list[0]) #quote
st.button("New Faruq Quote")

# end of code
