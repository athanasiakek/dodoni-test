import streamlit as st
import random

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

title = st.text_input("Ψηφιακό Μαντείο Δωδώνης", "...")


n = random.random() 

if(title != '...'):
    st.write("Η ερώτηση σου:....", n)