# 🤖 Machine Learning Operations (MLOps)

Este proyecto abarca la convergencia de Data Engineering, Machine Learning y DevOps.

## Descripción

Este proyecto tiene como foco principal un dataset de películas. Se desarrolla un modelo de Machine Learning para realizar recomendaciones de 5 películas similares y se implementa un conjunto de 6 funciones que retornan información específica. Todo esto es desplegado a través de una API.

## Características

Este proyecto presenta las siguientes características:

- Incorpora un modelo de recomendación de Machine Learning y 6 funciones relacionadas.
- Utiliza el conjunto de datos "data_maestro" obtenido del archivo "data_maestro.csv".

## Funciones

1. `Cantidad_filmaciones_mes(mes)`:
    - Retorna la cantidad de películas estrenadas en el mes especificado.

2. `Cantidad_filmaciones_día(día)`:
    - Retorna la cantidad de películas estrenadas en el día especificado.

3. `Score_titulo(nombre_pelicula)`:
    - Retorna el título, año de estreno y puntuación de una película específica.

4. `Votos_titulo(nombre_pelicula)`:
    - Retorna el título, cantidad de votos y valor promedio de las votaciones de una película, solo si tiene al menos 2,000 votos.

5. `get_actor(nombre_actor)`:
    - Retorna el éxito de un actor, incluyendo la lista de películas en las que ha participado, la cantidad total y el promedio de retorno de cada película.

6. `get_director(nombre_director)`:
    - Retorna el éxito de un director, incluyendo la lista de películas dirigidas por él, con sus fechas de lanzamiento, retorno, costo y ganancia.

## Modelo de Machine Learning

El modelo de recomendación se basa en el algoritmo de Nearest Neighbors y utiliza las siguientes columnas para encontrar películas similares:

- `budget`
- `popularity`
- `vote_average`
- `vote_count`
- `runtime`

Función de Machine Learning:

- `Recomendacion(titulo)`:
    - Recomienda películas similares al título dado utilizando el algoritmo de Nearest Neighbors.

## Uso

Una vez instalado el proyecto, se puede utilizar de la siguiente manera:

1. Importar las funciones del proyecto.
2. Utilizar las funciones según las necesidades.
3. Para la función de recomendación, proporcionar el título de una película y obtener la lista de películas recomendadas.

## Ejemplo de uso de la función de recomendación:
```python
from proyecto_ml_ops import Recomendacion

peliculas_recomendadas = Recomendacion("Título de película")
print(peliculas_recomendadas)
```

## Conjunto de datos
El proyecto se basa exclusivamente en el archivo "data_maestro.csv", el cual contiene 42,195 filas y 26 columnas. Las columnas incluyen información sobre presupuesto, popularidad, géneros, idiomas, fechas de lanzamiento, entre otros.

## Estructura del proyecto
```
Env/
├── data/
│   ├── data_maestro.csv
│   
├── notebooks/
│   ├── Realización proyecto.ipynb
│     
├── src/
│   ├── Frecuencia idioma.png
│   ├── generos frecuencia.png
│   ├── Heatmap_correlaciones.png
│   ├── peliculas por año.png
│   ├── Visualizacion de nulos columna.png
│
└── README.md
```
## Resultados

- Se observa una alta correlación entre "popularity" y "vote_count", indicando que películas con más votos generalmente son más populares.
- Las columnas "popularity" y "return" presentan sesgo y falta de uniformidad en su distribución.
- La columna "status" muestra un desbalance significativo.
- El análisis de palabras clave sugiere ciertos términos relevantes para el sistema de recomendación.
  
## Contacto

Para más información, puede contactarnos a través del correo: ismamtz4@gmail.com
