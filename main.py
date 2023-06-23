from fastapi import FastAPI
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.model_selection import train_test_split


data_maestro = pd.read_csv("MLOps\data\data_maestro.csv")
app = FastAPI()

#Aqui se le llama con la misma ruta para obtener la funcion y llamarla a traves de uvicorn


@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor:str):
    """Funcion que recibe el nombre de un actor y retorna toda la informacion de este, como cantidad de peliculas en las que ha participado
    , el éxito medido en retorno y el promedo de retorno en cada película
    """

    # se da formato de title al nombre del actor
    nombre_actor = nombre_actor.title()

    #se crea un dataframe filtrado con el nombre del actor
    actor_df = data_maestro[data_maestro["cast_names"].apply(lambda x: nombre_actor.title() in x)]
    
    #Se calcula la sumatoria del retorno que es el exito de toda la carrera del actor
    exito = actor_df["return"].sum()

    #se establece la cantidad de pelicuals en la cual ha actuado
    actuado = actor_df.shape[0]

    # Se establece el ppromedio por pelicula que ha conseguido
    promedio_retorno = actor_df["return"].sum() / len(actor_df)

    return "El actor/actriz " + nombre_actor + " ha participado en " + str(actuado) + " filmaciones, el mismo ha conseguido un retorno total de " + str(exito) + ", con un promedio de " + str(promedio_retorno) + " por filmación"
    
@app.get("/votos_titulo/{title}")
def votos_titulo(title:str):
    """Funcion que recibe el nombre de una pelicula para especificar la cantidad de votos que ha recibido
    Parametros:
    title:str, el nombre de una pelicula

    Retorna:
    str, un mensaje con la infromacion sobre los votos de la pelicula, el año de estreno, su promedio de votos
    """
    
    # se da formato al nombre para evitar problemas 
    title = title.lower()

    # se filtra el dataframe con el titulo especificado
    titulo = data_maestro[data_maestro["title"].str.lower() == title]
   
    # se comprueba que no arroje un dataframe vacio, de lo contrario, la pelicula no existe
    if titulo.empty == False:
        # Una vez que el dataframe no está vacío, se verifica que tenga mas de 2 mil valoracoines y se procede a retornar lo solicitado
        # de lo contrario, regresa que no cumple la condicion.
        if int(titulo["vote_count"]) >= 2000:
            votos = int(titulo["vote_count"])
            promedio = float(titulo["vote_average"])
            año = int(titulo["release_year"])
            return "La pelicula " + str(title).title() + " fue estrenada en el año " + str(año) + ". La misma cuenta con un total de " + str(votos) + " votos, con un promedio de valoración de " + str(promedio)
        else:
            return "Esta pelicula no cumple con al menos 2,000 valoraciones."
    else:
        return "Esta pelicula no existe"

@app.get("/score_titulo/{title}")    
def score_titulo(title:str):
    """ Función que retorna el score de una pelicula especificada
    Parametros:
    title: str, recibe el nombre de la pelicula e especificar

    Retorna:
    str, una texto con la descripcion de la pelicula, su nombre, el año que fue publicada y su score
    """

    #se da formato title al titulo
    title  =title.title()

    #se crea dataframe filtrado con el titulo
    titulo = data_maestro[data_maestro["title"]==title]

    #se establece al popularidad del titulo buscado
    pop = float(titulo["popularity"])

    # se establece el año en el cual fue publicada
    año = int(titulo["release_year"])

    return "La pelicula " + title + " fue estrenada en el año " + str(año) + " con un score de " + str(pop)  


@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia:str):
    """ Función que retorna la cantidad de filmaciones que fueron realizadas en un día de la semana en específico
    Parámetros:
    dia:str, el nombre de un día en español.

    Retorna:
    str: Un mensaje con la cantidad de películas estrenadas en el día especificado
    """

    #se convierte el nombre del dia a formato capitalize
    dia = dia.capitalize()

    #diccionario de dias en español y su equivalente en inglés
    dias = {
    'Lunes': 'Monday',
    'Martes': 'Tuesday',
    'Miércoles': 'Wednesday',
    'Jueves': 'Thursday',
    'Viernes': 'Friday',
    'Sábado': 'Saturday',
    'Domingo': 'Sunday'
}
    
    #Se convierte la columna releas_date a formato datetime
    data_maestro["release_date"] = pd.to_datetime(data_maestro["release_date"], format = "%Y-%m-%d",errors="coerce")
    

    if dia not in dias:
        return "Eliga un dia valido(Recuerda usar acentos)"
    else:
        ingles = dias[dia]
        # se hace una columna con los nombres de cada mes extraidos de release date
        columna_dia = data_maestro["release_date"].dt.day_name()

        #se filtran las peliculas realizadas el día especificado
        estrenos_dia = data_maestro[data_maestro["release_date"].dt.day_name() == ingles]
        
        return str(estrenos_dia.shape[0]) +  " películas fueron estrenadas en " + dia.lower()

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes:str):
    """ Funcion que obtiene la cantidad de filmaciones realizadas de un mes en especifico
    Parámetros:
    mes: str, el nombre del mes en español

    Retorna:
    str, un mensaje con la cantidad de películas estrenadas en el mes especificado
    """

    #se convierte el nombre del mes en capitalize
    mes = mes.capitalize()
   
    # diccionario de meses en español y su traducción en inglés
    meses = {
    'Enero': 'January',
    'Febrero': 'February',
    'Marzo': 'March',
    'Abril': 'April',
    'Mayo': 'May',
    'Junio': 'June',
    'Julio': 'July',
    'Agosto': 'August',
    'Septiembre': 'September',
    'Octubre': 'October',
    'Noviembre': 'November',
    'Diciembre': 'December'
    }

    # Se convierte releas_date a tipo datetime
    data_maestro["release_date"] = pd.to_datetime(data_maestro["release_date"], format = "%Y-%m-%d",errors="coerce")
    

    if mes not in meses:
        return "Eliga un mes valido"
    else:
        ingles = meses[mes]
        # se hace una columna con los nombres de cada mes extraidos de release date
        columna_mes = data_maestro["release_date"].dt.month_name()
        
        #Se filtran las filmaciones realizadas en el mes especificado
        estrenos_mes = data_maestro[data_maestro["release_date"].dt.month_name() == ingles]
        
        return str(estrenos_mes.shape[0]) +  " Películas fueron estrenadas el mes de " + mes

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director:str):
    """ En esta funcion se obtiene como parametro el nombre de un director de peliculas.
    Parámetros:
    nombre_director: str, el nombre del director

    Retorna:
    Dict, un diccionario con dos claves:
        1."mensaje":str, un mensaje descripotivo sobre el director y su carrera.
        2."datos":dict, un diccionario con los datos del director, donde las claves son los índices y los valores
        son otro diccionario con los datos de cada película.
    """

    #se rellenan los valores faltantes de la columna Director con diccionarios vacíos
    data_maestro['Director'] = data_maestro['Director'].fillna({})

    #se convierte la columna Director a tipo string
    data_maestro["Director"] = data_maestro["Director"].astype(str)
    
    #Se convierte el nombre del director a formato Title
    nombre_director = nombre_director.title()

    #Se filtran las filas que contienen el nombre del director
    director_df = data_maestro[data_maestro["Director"].apply(lambda x: nombre_director in x)]
    
    # se calcula el exito con la sumatoria de la columna Return
    exito = director_df["return"].sum()

    # se crea un dataframe para mostrar los datos relevantes
    mostrar_df = pd.DataFrame([director_df["title"],director_df["release_year"].astype(int),director_df["revenue"],director_df["budget"],director_df["return"] ])
    # se transpone el dataframe debido a que los nombres de las columnas aparecian como indices.
    mostrar_df = mostrar_df.T
    
    #Se crea la cadena que contiene el mensaje descriptivo del director y su carrera
    cadena = "El director " + nombre_director + " ha generado " + str(exito) + " en toda su carrera"
    
    return {
        "mensaje": cadena,
        "datos": mostrar_df.to_dict("index")
    }

@app.get("/recomendacion/{titulo}")
def recomendacion(titulo:str):
    
    """Funcion que recomienda peliculas similares dando un título utilizando el algoritmo de Nearest Neighbors
    Parámetros:
    titulo: str, es el nombre de la pelicula sobre la cual se hará la recomendación.

    Retorna:
    Peliculas_recomendadas: lista, una lista de strings con los títulos de las películas recomendadas
    """
    # se da formato title a la variable titulo
    titulo = titulo.title()

    #se importa el dataset a utilizar
    data_maestro = pd.read_csv("data/data_maestro.csv")

    #se hace una copia del dataset originar para trabajar sobre este y evitar que se modifique
    data_modelo = data_maestro.copy()
    
    #Se eliminan todos los valores faltantes del dataset, para que el modelo funcione lo mejor posible
    data_modelo = data_modelo.dropna()
    
    # se sobreescribe data_modelo con las columnas numericas relevantes para el modelo
    columnas = ["budget","popularity","vote_average","vote_count","runtime"]
    data_modelo = data_modelo[columnas]
    
    # se normalizan los datos
    normalizada = (data_modelo - data_modelo.mean()) / data_modelo.std()
    referencia = data_maestro[data_maestro["title"].str.title() ==titulo]

    # Se busca la pelicula en el dataset
    if referencia.empty:
        return[] # esto devolverá la lista vacía e indica que no se encuentra el titulo

    # Se dividen los datos en conjunto de entrenamiento y prueba
    x_train,x_test = train_test_split(normalizada,test_size=0.3, random_state=0)

    #se entrena el modelo de nearest neighbors
    modelo  = NearestNeighbors(n_neighbors=6, algorithm="ball_tree")
    modelo.fit(x_train)

    
    #se obtiene el indice lde la pelicula de referencia
    indice = referencia.index[0]

    # obtener las mas parecidas (peliculas)
    distancias,indices = modelo.kneighbors(x_test.iloc[indice:indice + 1])
    indice_recomendaciones = indices[0][1:6]
    peliculas_recomendadas = data_maestro["title"].iloc[indice_recomendaciones].values    
   
    return list(peliculas_recomendadas) 
    











