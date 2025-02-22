import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Dashboard de Vida")

# Entrada de edad actual
edad_actual = st.slider("Selecciona tu edad", 0, 100, 25)

# Opciones de esperanza de vida
edades_futuras = [30, 40, 50, 60, 70, 80, 90, 100]

# Calcular datos
data = {edad: (edad_actual / edad) * 100 for edad in edades_futuras}
trimestres = {edad: (edad * 4 - edad_actual * 4) for edad in edades_futuras}

# Mostrar métricas
st.write(f"🔹 **Edad actual:** {edad_actual} años")
for edad, pct in data.items():
    st.write(f"📌 {edad} años: {pct:.1f}% transcurrido, {trimestres[edad]} trimestres restantes")

# Gráfico de barras
fig, ax = plt.subplots()
ax.bar(data.keys(), data.values(), color='skyblue')
ax.set_xlabel("Esperanza de vida")
ax.set_ylabel("Porcentaje de vida transcurrido")
ax.set_title("Progreso de vida según expectativa")
st.pyplot(fig)
