import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga desde seaborn en un dataframe
df = sns.load_dataset("titanic")

# Mostrar primeras filas
print(df.head())

# información general
print(df.info())

# Estadísticas descriptivas
print(df.describe(include='all'))

# Valores nulos por columna
print(df.isnull().sum())

# distribución edades
plt.hist(df['age'].dropna(), bins=20, edgecolor='black')
plt.title('Distribución de edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()


# comparar los supervivientes por sexo
sns.countplot(x='sex', hue='survived', data=df)
plt.title('Supervivencia por sexo')
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.legend(title='Sobrevivió', labels=['No', 'Sí'])
plt.show()


# Ver cuántos valores nulos tiene 'age'
print(df['age'].isnull().sum())

# Rellenar los valores nulos con la media de la columna
df.fillna({'age': df['age'].mean()}, inplace=True)

# Confirmar que ya no hay valores nulos en 'age'
print(df['age'].isnull().sum())

# supervivencia por clase
survival_rate_by_class = df.groupby('pclass')['survived'].mean()
print(survival_rate_by_class)

# Porcentaje de supervivencia por clase
df.groupby('pclass')['survived'].mean().plot(kind='bar')

plt.title('Tasa de Supervivencia por Clase')
plt.xlabel('Clase')
plt.ylabel('Tasa de Supervivencia')
plt.ylim(0, 1)
plt.show()