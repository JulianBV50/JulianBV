import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('Datos.csv')

def main():
    st.write("¡Hola, mundo!")
    st.success("Correcto !!")
    nombre = st.text_input('Tu nombre:',placeholder='nombre completo...')
    edad=st.number_input('Edad:',1,20,step=1)
    cita=st.date_input('Fecha de cita :',)
    st.write(f'Nombre: {nombre.upper()}')
    st.write(f'Edad: {edad}')
    st.write(f'Fecha de la cita: {cita}')
    img1=Image.open('Logo J2.jpeg')
    img2=Image.open('Logo J2.png')
    st.image(img1, use_container_width=True)
    st.image(img2, use_container_width=True)
    st.image('https://picsum.photos/800')





    st.header("Dataframe:")
    st.dataframe(df)
    st.table(df)
    st.json({"Clave:" "Valor"})

    opcion=st.selectbox(
        'Selecciona la fruta',
        ['Manzana', 'Naranja','Banano']
    )

    st.write(f'Tu fruta es : {opcion}')

    opciones=st.multiselect(
        'Selecciona la fruta',
        ['Manzana', 'Naranja','Banano','Coco','Papaya']
    )

    st.write('Tus frutas son :',opciones)

if __name__ == "__main__":
    main()
