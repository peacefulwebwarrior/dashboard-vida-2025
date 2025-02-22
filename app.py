import streamlit as st
import datetime
import pandas as pd

# Cargar el GIF de reloj de arena
st.image('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjg3NmRhZGQwZjFkYTg5MGY2ZmQ5YzY3N2E1Y2ZjZWU0MTM5NDc1NWM4YiZjdD1n/8QNvAwT5AYvDb9Dtm8/giphy.gif', width=100)

# Crear una lista con los años de nacimiento por defecto
años_nacimiento_por_defecto = [1998, 1966, 1969, 2002, 1996]

# Título de la aplicación
st.title("Porcentaje de Vida Transcurrido por Persona")

# Mostrar las opciones para que el usuario pueda elegir el año de nacimiento de cada persona
años_nacimiento = []
nombres_personas = []  # Lista para guardar los nombres

for i in range(1, 6):
    # Seleccionar el año de nacimiento para cada persona
    año = st.selectbox(f"Año de nacimiento de Persona {i}:", 
                       options=[1998, 1966, 1969, 2002, 1996], 
                       index=años_nacimiento_por_defecto.index(años_nacimiento_por_defecto[i-1]))
    años_nacimiento.append(año)
    
    # Ingresar el nombre de cada persona
    nombre = st.text_input(f"Nombre de Persona {i}:", value=f"Persona {i}")
    nombres_personas.append(nombre)

# Función para calcular la edad y los detalles
def calcular_tiempos(año_nacimiento):
    fecha_nacimiento = datetime.date(año_nacimiento, 1, 1)
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
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
    
    return {
        "Edad": edad,
        "Días Transcurridos": dias_transcurridos,
        "Años Transcurridos": años_transcurridos,
        "Meses Transcurridos": meses_transcurridos,
        "Días Restantes": dias_restantes,
        "Próximo Cumpleaños": f"{años_restantes_cumple} años, {meses_restantes_cumple} meses, {dias_restantes_cumple_final} días"
    }

# Lista de edades objetivo (30, 50, 70, 77.16 y 90 años)
edades = [70, 77.16, 90]  # Edad objetivo en orden de menor a mayor

# Crear la lista para almacenar los resultados de todas las personas
resultados_totales = []

# Calcular los resultados para cada persona
for idx, (año, nombre) in enumerate(zip(años_nacimiento, nombres_personas)):
    resultados = []
    for edad_objetivo in edades:
        # Obtener el tiempo transcurrido para la persona actual
        tiempos = calcular_tiempos(año)
        
        # Total de días hasta la edad objetivo (en años * 365)
        total_vida_objetivo = edad_objetivo * 365
        porcentaje_vivido = (tiempos["Días Transcurridos"] / total_vida_objetivo) * 100
        
        # Años restantes
        años_restantes = (edad_objetivo - tiempos["Años Transcurridos"])
        
        # Guardar los resultados para la persona actual
        resultados.append([nombre, tiempos["Edad"], edad_objetivo, porcentaje_vivido, años_restantes])
    
    resultados_totales.extend(resultados)

# Crear un DataFrame con los resultados
df_resultados = pd.DataFrame(resultados_totales, columns=["Persona", "Edad Actual", "Edad Objetivo", "Porcentaje de Vida Vivido (%)", "Años Restantes"])

# Filtrar los resultados donde el porcentaje de vida vivido es menor al 100%
df_resultados_filtrados = df_resultados[df_resultados["Porcentaje de Vida Vivido (%)"] < 100]

# Mostrar la tabla con los resultados filtrados
st.dataframe(df_resultados_filtrados)
