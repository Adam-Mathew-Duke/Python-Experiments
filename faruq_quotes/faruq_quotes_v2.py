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

background_colors = [
'#000000','#00008B','#006400','#8B0000','#2F4F4F',
'#556B2F','#8B008B','#008B8B','#FF8C00','#9400D3']

string = ""

for word in faruq_quotes_list[quote].split():

    # random number is used for random word background highlights
    rand = random.randrange(100)

    # upper case words get a color background and larger font
    if word.isupper() and len(word) >= 2:
        string += ' <font style=color:'+'white'+';background:'+background_colors[random.randint(0,len(background_colors)-1)]+';font-size:30px; line-height:180>'+word+'</font>'
    
    # random words get a color background and a larger font
    elif rand >= 0 and rand <= 10 and len(word) >= 5:
        string += ' <font style=color:white;background:'+background_colors[random.randint(0,len(background_colors)-1)]+';font-size:30px; line-height:180>'+word+'</font>'
    
    # other words are printed out as normal
    else:
        string += ' <font style=display:inline;font-size:20px;>'+word+'</font>'

st.html(string)
st.button("New Faruq Quote")

# end of code
