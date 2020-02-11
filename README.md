# El mejor sitio
En este proyecto hemos tratado de situar el mejor emplazamiento para una oficina en la ciudad de Nueva York. Basandonos en la distancia a un aeropuerto cercano,
el número de starbucks para empezar el día con un buen café y el número de night clubs para poder ir de afterworks como dios manda.

# Criterios
## Aeropuerto
Para la búsqueda del aeropuerto se ha escogido una distancia máxima de 15 km. Se ha cogido un valor para la media ponderada de 50%.

## Night Club
Para la búsqueda de los night clubs, se ha escogido una distancia máxima de 500 metros con respecto a la oficina. Se ha cogido un valor para la media ponderada de 25%. 

## Starbucks
Para la búsqueda de los starbucks, se ha escogido una distancia máxima de 250 metros con respecto a la oficina. Se ha cogido un valor para la media ponderada de 25%. 

# Carpetas
## data
Contiene los dataset (starbucks y airports) utilizados en el proyecto

## json
Contiene los jsons generados para ser importados a mongoDB. Los jsons denominados cleaned contiene datos filtrados. El archivo airports-nightClub-starbucks.json contiene los datos de todos los datos filtrados.
