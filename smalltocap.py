import streamlit as st 
st.title('small to capital')
st.header('converting small letters to capital letters')
x=st.text_input(label='enter a sentence')
y=x.upper()
clicked=st.button('submit')
if clicked:
    st.write(y)

                

