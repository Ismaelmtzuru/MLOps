Machine Learning Operations (MLOps)
Este es un proyecto en el cual se realiza Data Engineering, Machine Learnign y DevOps.

Descripción
Este proyecto está enfocado en un dataset de películas, se hace un modelo de Machine Learning para hacer una recomendación de 5 películas similare, 6 funciones que retornan datos en específico y todo esto haciendo un deploy en un API.

Características:

Este proyecto cuenta con 6 funciones y un modelo de recomendación de Machine Learning.
Todo esto, está realizado sobre un dataset llamado data_maestro, que recibe la información del archivo data_maestro.csv.

Funciones:
-Cantidad_filmaciones_mes(mes):
	En esta función se ingresa un mes en el idioma de español. Al consultar, devuelve la cantidad de películas que fueron estrenadas en el mes especificado.

-Cantidad_filmaciones_día(día):
	Esta funcion, la cantidad de películas que fueron estrenadas en el día especificado, el día se escribe en idioma español.

-Score_titulo(nombre_pelicula):
	En esta función se recibe el nombre de una película, retorna el título especificado, el año de estreno y el score o popularidad.

-Votos_titulo(nombre_pelicula):
	Se especifica el nombre de la pelicula, retornando el titulo, la cantidad de votos y el valor promedio de las votaciones. Toma en cuenta solo aquellas películas que tengan igual o más de 2,000 votaciones, en caso contrario, se da un mensaje al usuario que esta película no cumple con la condición de 2,000 valoraciones o más y no retorna nada.

-get_actor(nombre_actor):
	Esta función recibe el nombre de un actor para retornar el éxito de este, el éxito está medido a través del retorno de todas las películas en las cuales ha participado. Ademas de retornar lo anterior, se muestra la cantidad de películas en las que ha participado y el promedio de retorno de cada película.

-get_director(nombre_director):
	Se ingresa el nombre de un director, la función retorna el éxito del director por medio del retorno, devuelve el nombre de cada película con su fecha de lanzamiento, retorno, costo y ganancia de cada película.

El modelo de Machine Learning está realizado en una función, en la cual, se utiliza un modelo de Nearest Neighbors, para que vea cuales titulos son los más cercanos en cuestión de parecidos, las columnas utilizadas son:
-budget
-popularity
-vote_average
-vote_count
-runtime
Función de Machine Learning:
- Recomendacion(titulo):
	Funcion que recomienda peliculas similares dando un título utilizando el algoritmo de Nearest Neighbors
Parámetros:
titulo: str, es el nombre de la pelicula sobre la cual se hará la recomendación.
Retorna:
Peliculas_recomendadas: lista, una lista de strings con los títulos de las películas recomendadas
    

Uso
Explica cómo utilizar el proyecto una vez que esté instalado. Proporciona ejemplos de comandos, código o pasos que el usuario deba seguir para ejecutar el proyecto correctamente.

Conjunto de datos
Todo este proyecto, se usa solamente con data_maestro.csv, el cual consta de 42,195 filas y 26 columnas. Las columnas están conformadas de la siguiente manera:

- belongs_to_collection, 4,356 valores y es de tipo objeto.

- budget tiene 42,195 valores y son de tipo float.

- genres consta de 42,195 valores de tipo objeto, que se compone de listas de diccionarios.

-id tiene 42,195 valres de tipo entero. El cual es id de todas las películas.

-original_language tiene 42,184 valores de tipo object, el cual tiene las abreviaciones del lenguage original.

-Overview, consta de 41,293 valores de tipo objeto.
Tiene una descripción de la película.

-Popularity: tiene 42,195 valores de tipo float.

-Production_companies: tiene 42,195 es de tipo object, contiene diccionarios con el nombre de la productora y su id.

-Production_countries: contiene 42,195 valores de tipo objeto. En cada fila tiene lista de diccionario con el formato del nombre, abrevietura, y el nombre del país.

-Release_date: tiene 42,195 datos de tipo objeto. Este contiene las fechas de formado yyyy-mm-dd, que es la fecha en la cual la película fue estrenada.

-Revenue: contiene 42,195 valores de tipo float. Esta fila es la que tiene las ganancias de la película sin contar los gastos o inversión.

-Runtime: Tiene 41,956 valores de tipo float64.
Esta específica la cantidad de minutos que tiene la película.

-Spoken_languages: Consta de 42,195 de tipo objeto.
En cada fila, tiene lista de diccionario, los cuales contiene el codigo del idioma, su abreviacion y el nombre del idioma.

-Status: Específica el estado de la película, si ya fue estrenada o no. Contiene 42,120 valores de tipo objeto.

-tagline: En esta columna está especificada el slogan de cada película. Contiene 19,039 datos de tipo objeto.

-title: Contiene 42,195 valores de tipo objeto. Aquí se especifica el título o nombre de cada película.

-Vote_average: En esta columna se especifica el promedio de las valoraciones o puntuación dada por los usuarios. Contiene 42,195 valores de tipo float64.

-Vote_count: Aquí tiene especificado el total de personas que ha calificado a la película. contiene 42,195 valores de tipo float64.

-Release_year: En esta columna, que se ha creado a partir de la columna release_date. Contiene el valor del año en el cual se ha estrenado. Tiene 42,195 valores de tipo float64.

-Return: Esta columna ha sido creada a partir de la división del budget / revenue, esto es el éxito que ha tenido cada película. Tiene 42,195 filas de tipo float64.

-Cast: En cada fila tiene una lista que contiene un diccionario con todo el cast de la película especificando cada personaje, actor que partició, género, entre otras cosas. El total de filas es de 42,195 de tipo objeto.

-Crew:  Esta columna contiene lista de varios diccionarios que contiene toda la producción que participó en la realización de esa película.Contiene 42,195 valores de tipo objeto.

-Cast_names: En esta columna, se especifica los nombres de los actores y/o actrices que participan en esa película. Contiene 42,195 valores de tipo objeto.

-Director: Aquí se nombra al director de esta película, consta de 41,383 valores de tipo objeto.

-Generos: Contiene una lista de los géneros a los cuales pertenece la película, tiene un total de 39,970 registros de tipo objeto.

-Lenguages: Esta columna ha sido creada con los puros nombres de los lenguages de los cuales se ha doblado cada película. contiene 38,564 registos de tipo objeto.


Estructura del proyecto

Env/
├── data/
│   ├── data_maestro.csv
│   
├── notebooks/
│   ├── Realización proyecto.ipynb
│     
├── src/
│   ├── Frecuencia idioma.png
│   └── generos frecuencia.png
|   ├── Heatmap_correlaciones.png
│   └── peliculas por año.png
|   └── Visualizacion de nulos columna.png
└── README.md

Resultados
- Se puede ver que popularity está altamente relacionado con vote_count, debido a que entre más votos tenga, significa que más personas fueron a ver y por lo tanto gustó más.

- En las columnas popularity y return, estan altamente sesgadas, ya que en algunas no proporcionan información o algunas peliculas no han tenido tanto exito como otras

- La columna status, se muestra altamente desbalanceada.

- En la nube de palabras, solo las palabras que podrían tener impacto en el sistema de recomendacin, son "man", "love". Hay más palabras pero son conectores que a fin de cuentas, no sirven para un sistema de recomendacion o clustering.
se mencionan a continuación, palabras con menos repeticiones:<br>
 -man <br>
 -king<br>
 -life<br>
 -love<br>
 -story<br>
 -girl<br>
 -movie<br>
 -night<br>
 -war<br>
 -blood<br>
 -death<br>
 -black<br>
 -summer<br>
 -last<br>
 -one<br>
 -christmas<br>
 -american<br>


Contacto:
ismamtz4@gmail.com