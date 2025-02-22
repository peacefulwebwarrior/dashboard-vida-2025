import streamlit as st
import datetime
import pandas as pd

# Crear una lista con los años de nacimiento por defecto
años_nacimiento_por_defecto = [1998, 1966, 1969, 2002, 1996]

# Título de la aplicación
st.title("DEATH THERAPY")

# Mostrar las opciones para que el usuario pueda elegir el año de nacimiento de cada persona
años_nacimiento = []
for i in range(1, 6):
    año = st.selectbox(f"Año de nacimiento de Persona {i}:", 
                       options=[1998, 1966, 1969, 2002, 1996], 
                       index=años_nacimiento_por_defecto.index(años_nacimiento_por_defecto[i-1]))
    años_nacimiento.append(año)

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

# Lista de edades objetivo (30, 50, 70, 90 años y esperanza de vida en Chile)
edades = [30, 50, 70, 90, 77.16]  # Esperanza de vida en Chile (77.16 años)

# Crear la lista para almacenar los resultados de todas las personas
resultados_totales = []

# Calcular los resultados para cada persona
for idx, año in enumerate(años_nacimiento):
    resultados = []
    for edad_objetivo in edades:
        # Obtener el tiempo transcurrido para la persona actual
        tiempos = calcular_tiempos(año)
        
        # Total de días hasta la edad objetivo (en años * 365)
        total_vida_objetivo = edad_objetivo * 365
        porcentaje_vivido = (tiempos["Días Transcurridos"] / total_vida_objetivo) * 100
        
        # Trimestres restantes
        trimestres_restantes = ((edad_objetivo * 365 - tiempos["Días Transcurridos"]) / 90)  # 1 trimestre = 90 días
        
        # Años restantes
        años_restantes = (edad_objetivo - tiempos["Años Transcurridos"])
        
        # Guardar los resultados para la persona actual
        resultados.append([f"Persona {idx + 1}", edad_objetivo, porcentaje_vivido, trimestres_restantes, años_restantes])
    
    resultados_totales.extend(resultados)

# Crear un DataFrame con los resultados
df_resultados = pd.DataFrame(resultados_totales, columns=["Persona", "Edad Objetivo", "Porcentaje de Vida Vivido (%)", "Trimestres Restantes", "Años Restantes"])

# Mostrar la tabla con los resultados
st.dataframe(df_resultados)
