'''
Name:           faruq_quotes_v2.py
Version:        2
Description:    Faruq from Battle Bots fortune cookie style app
'''

'''
Ideas:
> Collect more quality faruq quotes from Youtube!
> I can do a lot with HTML to make the quotes look cool.
> I'm looking forward to getting my sisters feedback on version 2!
'''

import streamlit as st
import random

from faruq_quotes_data_v2 import faruq_quotes_list
quote = random.randint(0,len(faruq_quotes_list)-1)

st.image("faruq_image.jpg",width=150)
st.html('<h4 style=line-height:180%>'+faruq_quotes_list[quote]+'</style></h4>')
st.button("New Faruq Quote")

# end of code
