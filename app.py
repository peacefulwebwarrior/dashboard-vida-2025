import streamlit as st
import datetime
import pandas as pd

# Cargar el nuevo GIF de reloj de arena
st.image('https://i.gifer.com/Z30J.gif', width=100)

# Crear las secciones
seccion = st.selectbox("Selecciona una sección", ["Vista Principal", "Modificar Datos"])

# Lista de edades objetivo (30, 50, 70, 77.16 y 90 años)
edades = [70, 77.16, 90]  # Edad objetivo en orden de menor a mayor

# Por defecto los años de nacimiento
años_nacimiento_por_defecto = [1998, 1966, 1969, 2002, 1996]
nombres_personas_por_defecto = ["Persona 1", "Persona 2", "Persona 3", "Persona 4", "Persona 5"]

# Si se selecciona "Modificar Datos"
if seccion == "Modificar Datos":
    años_nacimiento = []
    nombres_personas = []  # Lista para guardar los nombres
    for i in range(1, 6):
        # Seleccionar el año de nacimiento para cada persona
        año = st.selectbox(f"Año de nacimiento de Persona {i}:",
                           options=[1998, 1966, 1969, 2002, 1996],
                           index=años_nacimiento_por_defecto.index(años_nacimiento_por_defecto[i-1]))
        años_nacimiento.append(año)

        # Ingresar el nombre de cada persona
        nombre = st.text_input(f"Nombre de Persona {i}:", value=nombres_personas_por_defecto[i-1])
        nombres_personas.append(nombre)

    # Botón para guardar los cambios
    if st.button("Guardar cambios"):
        st.success("Datos guardados correctamente")

# Si se selecciona "Vista Principal"
if seccion == "Vista Principal":
    # Aseguramos que las listas de años de nacimiento y nombres estén definidas
    años_nacimiento = años_nacimiento_por_defecto
    nombres_personas = nombres_personas_por_defecto

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

    # Obtener el resultado de la Persona 1
    año = años_nacimiento[0]
    nombre = nombres_personas[0]
    tiempos = calcular_tiempos(año)

    # Total de días hasta la edad objetivo (en años * 365)
    edad_objetivo = 77.16  # Edad promedio de vida
    total_vida_objetivo = edad_objetivo * 365
    porcentaje_vivido = (tiempos["Días Transcurridos"] / total_vida_objetivo) * 100

    # Años restantes
    años_restantes = (edad_objetivo - tiempos["Años Transcurridos"])

    # Mostrar la información de la Persona 1
    st.write(f"**{nombre}**")
    st.write(f"Edad actual: {tiempos['Edad']} | Edad Objetivo: {edad_objetivo} | Años Restantes: {años_restantes}")
    
    # Mostrar barra de progreso del porcentaje de vida vivido
    st.progress(int(porcentaje_vivido))

    # Mostrar el porcentaje de vida vivido
    st.write(f"Porcentaje de Vida Vivido: {porcentaje_vivido:.2f}%")

    # Mostrar la imagen de reloj de arena con animación
    st.image('https://i.gifer.com/Z30J.gif', width=200)

