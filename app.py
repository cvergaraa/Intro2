import streamlit as st
from PIL import Image

st.title( "Mi primera pagina")

st.header("Huele feo")
st.write("Oliver y leopoldo gatos gordos")
image = Image.open('gato.jpg')

st.image(image, caption ='interfac multimodales')


texto = st.text_input('Tu eres mi mundo entero mi negra', 'Ramon')
st.write('camila llega ya plis :C', texto)
