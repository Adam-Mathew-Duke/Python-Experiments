import streamlit, random
from Oblique_Strategies_Data import quotes_list
streamlit.text(random.choice(quotes_list))
streamlit.button("New Oblique Strategy")
