import streamlit as st
import datetime

# Toma la fecha de nacimiento como input
fecha_nacimiento = st.date_input('Selecciona tu fecha de nacimiento', datetime.date(1995, 1, 1))

# Calcula la edad a partir de la fecha de nacimiento
hoy = datetime.date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Calcula el tiempo transcurrido hasta hoy
dias_transcurridos = (hoy - fecha_nacimiento).days
años_transcurridos = dias_transcurridos // 365
meses_transcurridos = (dias_transcurridos % 365) // 30
dias_restantes = dias_transcurridos % 30

# Mostrar la introducción sobre el tiempo transcurrido
st.title("Porcentaje de Vida Transcurrido")

st.write(f"Han transcurrido {años_transcurridos} años, {meses_transcurridos} meses y {dias_restantes} días desde tu fecha de nacimiento hasta hoy.")

# Lista de edades a calcular (30, 50, 70, 90 años)
edades = [30, 50, 70, 90]

# Recorre cada edad para calcular el porcentaje de vida y los trimestres restantes
for edad_objetivo in edades:
    # Total de días hasta la edad objetivo (en años * 365)
    total_vida_objetivo = edad_objetivo * 365  
    dias_vividos = (hoy - fecha_nacimiento).days
    
    # Porcentaje de vida vivido hasta la edad objetivo
    porcentaje_vivido = (dias_vividos / total_vida_objetivo) * 100
    
    # Trimestres restantes
    trimestres_restantes = ((edad_objetivo * 365 - dias_vividos) / 90)  # 1 trimestre = 90 días
    
    # Mostrar los resultados para cada edad
    st.write(f"\n## Para los {edad_objetivo} años:")
    st.write(f"Tu edad actual es: {edad} años.")
    st.write(f"Has vivido el {porcentaje_vivido:.2f}% de tu vida si llegas a los {edad_objetivo} años.")
    st.write(f"Te quedan aproximadamente {trimestres_restantes:.0f} trimestres para llegar a los {edad_objetivo} años.")
