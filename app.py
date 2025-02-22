import streamlit as st
import datetime
import pandas as pd

# Establecer la fecha base como 14 de abril de 1998
fecha_nacimiento = datetime.date(1998, 4, 14)

# Calcula la edad a partir de la fecha de nacimiento
hoy = datetime.date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Calcula el tiempo transcurrido hasta hoy
dias_transcurridos = (hoy - fecha_nacimiento).days
años_transcurridos = dias_transcurridos // 365
meses_transcurridos = (dias_transcurridos % 365) // 30
dias_restantes = dias_transcurridos % 30

# Cálculo del próximo cumpleaños
if (hoy.month, hoy.day) > (fecha_nacimiento.month, fecha_nacimiento.day):
    proximo_cumple = datetime.date(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)
else:
    proximo_cumple = datetime.date(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)

# Tiempo restante hasta el próximo cumpleaños
dias_restantes_cumple = (proximo_cumple - hoy).days
años_restantes_cumple = dias_restantes_cumple // 365
meses_restantes_cumple = (dias_restantes_cumple % 365) // 30
dias_restantes_cumple_final = dias_restantes_cumple % 30

# Mostrar la introducción sobre el tiempo transcurrido
st.title("Porcentaje de Vida Transcurrido")

st.write(f"Han transcurrido {años_transcurridos} años, {meses_transcurridos} meses y {dias_restantes} días desde tu fecha de nacimiento (14 de abril de 1998) hasta hoy.")
st.write(f"Faltan {años_restantes_cumple} años, {meses_restantes_cumple} meses y {dias_restantes_cumple_final} días para tu próximo cumpleaños.")

# Lista de edades a calc


