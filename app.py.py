import streamlit as st

st.title('Hacking with Hamid')

sentences1 = st.text_input('insert sentences1:')
sentences2 = st.text_input('insert sentences2:')

if st.button('Submit'):
  st.write('Sentences1 is:', sentences1)
  st.write('Sentences1 2s:', sentences2)


