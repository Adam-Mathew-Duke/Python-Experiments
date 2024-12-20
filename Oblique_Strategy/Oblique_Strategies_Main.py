import streamlit as st
import random
from Oblique_Strategies_Data import oblique_list
from Oblique_Strategies_Data import music_list
from Oblique_Strategies_Data import drawing_list

if "key" not in st.session_state:
    st.session_state["key"] = 1
if "value" not in st.session_state:
    st.session_state["value"] = "Oblique Strategy"
if "current_quote" not in st.session_state:
    st.session_state["current_quote"] = random.choice(oblique_list)
    
st.header(st.session_state["value"])
st.write('')
st.subheader(f'"{st.session_state["current_quote"]}"')

def button_function(a, b):
    st.session_state["key"] = a
    st.session_state["value"] = b

    if a == 1:
        st.session_state["current_quote"] = random.choice(oblique_list)
    elif a == 2:
        st.session_state["current_quote"] = random.choice(music_list)
    elif a == 3:
        st.session_state["current_quote"] = random.choice(drawing_list)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Oblique Strategy (Official)", on_click=button_function, args=(1, "Oblique Strategy"))
with col2:
    st.button("Music Strategy (Unofficial)", on_click=button_function, args=(2, "Music Strategy"))
with col3:
    st.button("Drawing Strategy (Unofficial)", on_click=button_function, args=(3, "Drawing Strategy"))

st.divider()

st.page_link("https://en.wikipedia.org/wiki/Oblique_Strategies", label="Learn about the Oblique Strategies on Wikipedia!", icon="🌐")
st.page_link("https://buymeacoffee.com/adamd", label="Buy me a coffee!", icon="☕")
