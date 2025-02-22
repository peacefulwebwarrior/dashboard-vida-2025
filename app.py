import streamlit as st
import datetime

# Toma la fecha de nacimiento como input
fecha_nacimiento = st.date_input('Selecciona tu fecha de nacimiento', datetime.date(1995, 1, 1))

# Calcula la edad a partir de la fecha de nacimiento
hoy = datetime.date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Cálculo de porcentaje de vida
total_vida_30 = 30 * 365  # Total de días hasta los 30 años
dias_vividos = (hoy - fecha_nacimiento).days
porcentaje_vivido = (dias_vividos / total_vida_30) * 100

# Cálculo de trimestres restantes
trimestres_restantes_30 = ((30 * 365 - dias_vividos) / 90)  # 1 trimestre = 90 días

# Mostrar la información
st.title("Porcentaje de Vida Transcurrido")

# Mostrar los resultados
st.write(f"Tu edad actual es: {edad} años.")
st.write(f"Has vivido el {porcentaje_vivido:.2f}% de tu vida si llegas a los 30 años.")
st.write(f"Te quedan aproximadamente {trimestres_restantes_30:.0f} trimestres para llegar a los 30 años.")
