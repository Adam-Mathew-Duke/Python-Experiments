'''
Name:           faruq_quotes.py
Version:        1
Description:    Faruq from Battle Bots fortune cookie style app
'''

# streamlit web app module
import streamlit as st

# built-in Python module
import random

# import faruq_quotes_list from faruq_quotes_data.py
from faruq_quotes_data import faruq_quotes_list

# choose a random quote from the faruq_quotes_list
quote = random.randint(0,len(faruq_quotes_list)-1)

# print quote index number and string from faruq_quotes_list
st.write("Faruq Quote #" + str(quote+1) + ". " + faruq_quotes_list[quote])

# pressing the streamlit button will re-run the script
st.button("New Faruq Quote")

# end of code
