import json
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd




col1, col2 = st.columns(2)


image = Image.open('main.png')
image2 = Image.open('enemigo.png')
image3 = Image.open('mundo.png')


with col1:
    st.write(""":green[RUBY]
             Ella es nuestra personaje principal, la cual va a viajar
             por el mundo y por la cual nos vamos a adentrar en las 
             historias de los diferentes lugares por los que tendra que 
             pasar""") 
    st.image(image2, caption='enemigo general',  width=180)
    st.write("""En este nivel se quiere empezar primero por el cambio climatico,
             nuestro personaje tendra que restaurar el valence de este ecosistema 
             mediante objetos magicos, los cuales seran recolectados por el jugador
             cuando tenga todos reunidos el ecosistema estara a savlo""")
    st.write("""\n
             \n""")
    options2 = ['exelente', 'buena', 'mala']
    star = st.selectbox( "Que tal te parecio la idea? :star2:", options2)
                       
    st.write('seleccionaste :smile::', star)
    st.write('Alguna sugerencia?')
    st.write('Cantidad de estrellas que le das?')
    estrellas = st.select_slider(
    'cuantas estrellas?',
    options=['1', '2', '3', '4', '5'])
    st.write('las estrrellas son ', estrellas)
    

    #st.button('enviar')
   # st.caption('Correos de contacto:')
    #st.caption('juancamilo.ulloa@ustabuca.edu.co:sunglasses:')
with col2:
    st.image(image, caption='personaje principal 🚨')
    st.write("""El es :red[Mr.Clock], es la creacion del villano el cual
             permace en anonimato, solo se sabe que es un gran
             cientifico """)
    st.image(image3, caption = 'este es la idea principal del primer nivel')


fig = go.Figure(data=[
   go.Bar(x=options2, y=[1 if opcion in star else 0 for opcion in options2])
])

fig.update_layout(
    title='calidad',
    xaxis_title='calidad',
    yaxis_title='Selección',
)
st.plotly_chart(fig)
    


