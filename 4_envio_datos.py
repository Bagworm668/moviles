import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def enviar_a_google_sheets(datos):
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

    client = gspread.authorize(credentials)
    spreadsheet = client.open('pagina')
    worksheet = spreadsheet.get_worksheet(0)
    last_row = len(worksheet.col_values(1)) + 1
    worksheet.update('A{}'.format(last_row), [datos]) 
    
def main():
    st.title('Enviar datos a Google Sheets')

        # Obtener los datos ingresados por el usuario
    datos = st.text_input('Ingrese los datos')
    lista =[datos]
    # Botón para enviar los datos a Google Sheets
    if st.button('Enviar'):
        enviar_a_google_sheets(lista)
        st.success('Datos enviados correctamente')

if __name__ == '__main__':
    main()      
#sheet = client.create('pagina')
#sheet.share("juancamiloxone@gmail.com", perm_type='user', role='writer')

