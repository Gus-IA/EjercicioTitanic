# Análisis Exploratorio del Dataset Titanic 🛳️

Este proyecto realiza un análisis exploratorio de datos (EDA) utilizando el famoso dataset **Titanic** que viene incluido en la librería `seaborn`.

## 📊 Objetivo

El objetivo principal es comprender la estructura de los datos, analizar la supervivencia según diferentes variables (como sexo y clase), y practicar técnicas básicas de limpieza de datos y visualización.

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **pandas**: para manipulación de datos
- **seaborn**: para cargar el dataset y visualizar relaciones
- **matplotlib**: para visualizaciones personalizadas

## 🔍 Análisis Realizado

1. **Carga del dataset** directamente desde `seaborn`.
2. **Inspección general**:
   - Primeras filas
   - Información del DataFrame (`info`)
   - Estadísticas descriptivas
   - Revisión de valores nulos
3. **Visualizaciones**:
   - Histograma de edades
   - Gráfico de barras de supervivencia por sexo
   - Gráfico de barras del porcentaje de supervivencia por clase
4. **Limpieza de datos**:
   - Relleno de valores nulos en la columna `age` con la media
5. **Análisis de supervivencia**:
   - Cálculo de la tasa de supervivencia por clase (`pclass`)

## 📈 Ejemplos de resultados

- Las mujeres tienen mayor probabilidad de haber sobrevivido que los hombres.
- Las personas en primera clase (`pclass=1`) tienen mayores tasas de supervivencia que aquellas en clases más bajas.
- La columna `age` tenía valores nulos, que fueron reemplazados con la media de edades.

Instalación de dependencias

Para instalar las dependencias necesarias, puedes usar el siguiente comando:

pip install -r requirements.txt

🧑‍💻 Autor

Desarrollado por Gus como parte de su aprendizaje en Python e IA.
