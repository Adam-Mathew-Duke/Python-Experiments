import streamlit, random
from Oblique_Strategies_Data import quotes_list

streamlit.html('<p style=font-family:Arial,sans-serif;font-size:25px;background-color:;text-align:center;padding-right:10px;padding-left:10px;padding-top:0px;padding-bottom:0px;>'+'Brian Eno’s Oblique Strategies (1975-1979)'+'</p>')
streamlit.html('<p style=font-family:Arial,sans-serif;font-size:25px;background-color:black;text-align:center;padding-right:10px;padding-left:10px;padding-top:75px;padding-bottom:75px;>'+random.choice(quotes_list)+'</p>')

left, middle, right = streamlit.columns(3)
middle.button("New Oblique Strategy",use_container_width=True)

# original code with no special formatting
#streamlit.subheader(random.choice(quotes_list))
#streamlit.button("New Oblique Strategy")
