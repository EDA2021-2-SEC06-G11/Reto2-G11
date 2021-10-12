"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
               'artworks': None,
               'medium': None,
               'objectId': None
    }
    """
    Este indice crea un mapa cuyas llaves son los id de la Artwork que guarda
    """

    catalog['artworks'] = lt.newList()

    """
    Este indice crea un mapa cuyas llaves son los id del Artista que guarda
    """
    catalog['artists'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtistbyConstituentID)
    catalog['DateAcquired'] = mp.newMap(800,
                                    maptype='CHAINING',
                                    loadfactor=4.0,
                                    comparefunction=compareArtworkbyYear)
    catalog['medium'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=4.0)
    catalog['objectId'] =  mp.newMap(100,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareArtworksbyObjectID)
    catalog['department'] =  mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=4.0)
    catalog['Nationalities'] = mp.newMap(1000,
                                  maptype= 'CHAINING',
                                  loadfactor = 4.0
    )
    return catalog
# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    """
    Edita el artwork para que busque sus artistas y las nacionalidades de estos artistas y los guarda
    Agrega el artwork que se suministro al catalog usando su objectID como su llave
    """
    constituentIds = artwork['ConstituentID'].split(",")  # Se obtienen los autores
    for constituentId in constituentIds :
        listaArtistas = lt.newList()
        #ARREGLAMOS LOS CONSTITUENTID ANTES DE UTILIZARLOS
        Id = constituentId.strip()
        Id = Id.strip("[")
        Id = Id.strip("]")
        
        # UTILIZAMOS LOS CONSTITUENTID INDIVIDUALES PARA ASIGNAR NOMBRE Y NACIONALIDAD A LAS ARTWORKS
        # TAMBIEN SE AGREGA ESTA OBRA A LAS OBRAS DEL ARTISTA AL CUAL REFERENCIA
        artists = catalog['artists']
        if(mp.contains(artists,Id)):
            ## Aqui se agrega la obra a la lista del artista
            dupla = mp.get(artists,Id)
            artista = me.getValue(dupla)
            obras = artista['Obras']
            lt.addLast(obras,artwork)
            artista['Obras'] = obras
            ## Aqui se le pone la informacion del artista a la obra
            nacionalidad = artista['Nationality']
            nombreArtista = artista['DisplayName']
            ## Si todavia no ha creado la lista la crea y la guarda bajo el nombre ArtistNames
            try : 
                listaArtistas = (artwork['ArtistNames'])
                print(listaArtistas)
            except:
                listaArtistas = lt.newList()
            lt.addLast(listaArtistas,nombreArtista)
            ## Hace lo mismo de nombre pero para nacionalidad
            try:
                listaNacionalidades = artwork['ArtistNationalities']
            except:
                listaNacionalidades = lt.newList()
            lt.addLast(listaNacionalidades,nacionalidad)
                


    ## En esta parte vamos a agregar el artwork a su correcto lugar en el mapa de Medium
    medium = artwork['Medium']
    if mp.contains(catalog['medium'],medium) :
        lista = mp.get(catalog['medium'], medium)
        valor = me.getValue(lista)
        lt.addLast(valor,artwork)
        mp.put(catalog['medium'],medium,valor)

    else:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(catalog['medium'], artwork["Medium"], lista)

    lt.addLast(catalog['artworks'], artwork)
    #mp.put(catalog['artworks'],artwork['ObjectID'],artwork)

    ## En esta parte vamos a agregar el artwork dependiendo del anio en el que adquirio
    anio = artwork['DateAcquired'][:4]
    if mp.contains(catalog['DateAcquired'], anio):
        lista = mp.get(catalog['DateAcquired'], anio)
        valor = me.getValue(lista)
        dicfinal = ({'objectID': artwork['ObjectID'], 'Title': artwork['Title'], 'ArtistNames': listaArtistas, 'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'Date': artwork['Date'], 'DateAcquired': artwork['DateAcquired'], 'URL': artwork['URL']})
        lt.addLast(valor,dicfinal)
        mp.put(catalog['DateAcquired'],anio,valor)

    else:
        if anio != '':
            lista = lt.newList("ARRAY_LIST")
            dicfinal = ({'objectID': artwork['ObjectID'], 'Title': artwork['Title'], 'ArtistNames': listaArtistas, 'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'Date': artwork['Date'], 'DateAcquired': artwork['DateAcquired'], 'URL': artwork['URL']})
            lt.addLast(lista,dicfinal)
            mp.put(catalog['DateAcquired'], anio, lista)

    ## En esta parte vamos a agregar el artwork dependiendo del departamento al que pertenece
    department = artwork['Department']
    if mp.contains(catalog['department'],department) :
        lista = mp.get(catalog['department'], department)
        valor = me.getValue(lista)
        #dicfinal = ({'objectID': artwork['ObjectID'], 'Title': artwork['Title'], 'ArtistNames': listaArtistas, 'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'Date': artwork['Date'], 'DateAcquired': artwork['DateAcquired'], 'URL': artwork['URL']})
        lt.addLast(valor,artwork)
        mp.put(catalog['department'],department,valor)

    else:
        lista = lt.newList("ARRAY_LIST")
        #dicfinal = ({'objectID': artwork['ObjectID'], 'Title': artwork['Title'], 'ArtistNames': listaArtistas, 'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'Date': artwork['Date'], 'DateAcquired': artwork['DateAcquired'], 'URL': artwork['URL']})
        lt.addLast(lista,artwork)
        mp.put(catalog['department'], artwork["Department"], lista)

    #lt.addLast(catalog['department'], artwork)



def addArtist(catalog, artist):
    """
    Agrega el artist al mapa artists del catalogo usando su ConsituentID como llave y agregandole un 
    nuevo parametro llamado obras el cual guarda todas las obras que este artista tenga a su nombre"""
    artist["Obras"]= lt.newList()
    mp.put(catalog['artists'],artist['ConstituentID'],artist)


    


# Funciones para creacion de datos

# Funciones de consulta
def filtrarArtistasPorAños(catalog, añoInicial , añoFinal):
    listaRespuesta = lt.newList()
    llaves = mp.keySet(catalog['artists'])
    iterator = lt.iterator(llaves)
    for llave in iterator:
        dupla = mp.get(catalog['artists'],llave)
        artista = me.getValue(dupla)
        añoArtista = int (artista['BeginDate'])
        if int(añoInicial) <= añoArtista and añoArtista <= int(añoFinal):
            lt.addLast(listaRespuesta, artista)

    ## Ahora que ya tenemos la lista filtrada podemos usar una funcion de ordenamiento y returnearla
    sa.sort(listaRespuesta, compararArtistasPorAño)
    return listaRespuesta


def filtrarObrasPorAños(catalog,fechaInicial,fechaFinal):
    listaRespuesta = lt.newList()
    llavesa = mp.keySet(catalog['DateAcquired'])
    llaves = lt.iterator(llavesa)
    for llave in llaves:
        if(int(fechaInicial[:4]) <= int(llave) and int(llave) <= int(fechaFinal[:4])):
            dupla = mp.get(catalog['DateAcquired'],llave)
            obra = me.getValue(dupla)
            obriterator = lt.iterator(obra)
            for o in obriterator:
                fechaArtista = o['DateAcquired']
                if fechaInicial <= fechaArtista and fechaArtista <= fechaFinal:
                    lt.addLast(listaRespuesta, o)

    sa.sort(listaRespuesta, compareByDate)
    return listaRespuesta

def clasificarObrasDeArtistaPorTecnica(catalog, nombre):
    mapartists = mp.valueSet(catalog['artists'])
    iteration = lt.iterator(mapartists)
    elegido = []
    for artista in iteration:
        if artista['DisplayName'] == nombre:
            elegido = artista
            break
    sa.sort(elegido['Obras'], comparetech)

    popularity = lt.newList("ARRAY_LIST")
    art1 = None
    art2 = None
    n = 0
    tech_num = 0
    artlist = lt.newList("ARRAY_LIST")
    iteration = lt.iterator(elegido['Obras'])

    for artwork in iteration:         
        art1 = artwork['Medium']
        if art1 != art2:
            tech_num = tech_num + 1
            if art2 != None:
                lt.addLast(popularity, dic)
            n = 1
            artlist = lt.newList("ARRAY_LIST")
            lt.addLast(artlist, artwork)
            dic = {"Medium": artwork['Medium'], 'Number': n, 'Obras': artlist}
            art2 = art1
        else:
            n = n + 1
            art2 = art1
            lt.addLast(artlist, artwork)
            dic = {"Medium": artwork['Medium'], 'Number': n, 'Obras': artlist}
    
    if art1 == None:
        tech_num = 0
    elif art1 == art2:
        lt.addLast(popularity, dic)
        
    sa.sort(popularity, comparetechniques)

    return elegido, popularity, tech_num

def obrasPorNacionalidad(catalog):
        #Falta :D
    listaRespuesta = 'falta'
    return listaRespuesta

def obrasDeDepartamento(catalog, departamento):
    indep = lt.newList('ARRAY_LIST')
    inold = lt.newList('ARRAY_LIST')
    t_cost = 0.0
    t_weight = 0.0
    
    mapartwork = mp.get(catalog['department'], departamento)
    obras = me.getValue(mapartwork)
    iteration = lt.iterator(obras)

    for depo in iteration:
            size = ''
            cost = 0
            if depo['Height (cm)'] != '' and depo['Width (cm)'] != '':
                size = float(depo['Height (cm)']) * float(depo['Width (cm)'])/10000

            if depo['Depth (cm)'] != '' and depo['Depth (cm)'] != '0':
                if depo['Diameter (cm)'] !='':
                    size = float(depo['Depth (cm)']) * (float(depo['Diameter (cm)']))/1000000
                elif (depo['Height (cm)'] != '' and depo['Height (cm)'] != '0') and (depo['Width (cm)'] != '0' and depo['Width (cm)'] != ''):
                     size = float(depo['Height (cm)']) * float(depo['Width (cm)']) * float(depo['Depth (cm)'])/1000000 
            
            if depo['Circumference (cm)'] != '' and depo['Circumference (cm)'] != '0':
                size = ((float(depo['Circumference (cm)'])/2)**2)/3.14
                if depo['Diameter (cm)'] !='' and depo['Diameter (cm)'] !='0':
                        size = float(depo['Circumference (cm)']) * float(depo['Diameter (cm)'])/10000 
                        if depo['Length (cm)'] != '' and depo['Length (cm)'] != '0':
                            size = float(depo['Circumference (cm)']) * float(depo['Diameter (cm)']) * float(depo['Length (cm)'])/1000000
            if size == '' or size == 0:
                cost = 48.00
            elif (depo['Weight (kg)']) != '' and float(depo['Weight (kg)']) > size*72:
                size = float(depo['Weight (kg)'])

            
            if cost != 48.00 and (size != '' or size != 0):
                cost = size*72.00

            lt.addLast(indep, {'dep': depo, 'price': cost})
            if depo['Date'] != '' and depo['Date'] != '0':
                lt.addLast(inold, {'dep': depo, 'Date': depo['Date']})
            t_cost = t_cost + cost
            if depo['Weight (kg)'] != '':
                t_weight = t_weight + float(depo['Weight (kg)'])

    sa.sort(indep, comparecost)
    sa.sort(inold, compareage)
    return indep, inold, t_weight, t_cost

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Funciones de Comparacion
def compararArtistasPorAño(artista1,artista2):
    return int(artista1['BeginDate']) < int(artista2['BeginDate'])

def compareByDate(artwork1,artwork2):
     return ((artwork1['DateAcquired'] < artwork2['DateAcquired']))

def compareArtworksbyObjectID(id, entry):
    """
    Compara dos ids de los artworks, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareArtistbyConstituentID(id, entry):
    """
    Compara dos ids de artistas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareArtworkbyYear(year, entry):
    yearentry = me.getKey(entry)
    if (int(year) == int(yearentry)):
        return 0
    elif (int(year) > int(yearentry)):
        return 1
    else:
        return -1

def comparetech(art1, art2):
    return (art1['Medium'] < art2['Medium'])

def comparetechniques(art1, art2):
    return (art1['Number'] > art2['Number'])

def comparecost(art1, art2):
    return (art1['price'] > art2['price'])

def compareage(art1, art2):
    return (art1['Date'] < art2['Date'])


## CODIGO DE REQUERIMIENTOS DE LABORATORIOS
def addArtworkLab(catalog, artwork):
    constituentIds = artwork['ConstituentID'].split(",")  # Se obtienen los autores
    for constituentId in constituentIds :
        #ARREGLAMOS LOS CONSTITUENTID ANTES DE UTILIZARLOS
        Id = constituentId.strip()
        Id = Id.strip("[")
        Id = Id.strip("]")
        artists = catalog['artists']
        dupla = mp.get(artists,Id)
        artista = me.getValue(dupla)
        nacionalidadArtista = artista['Nationality']
        try : 
            ## Caso en el que la nacionalidad del artista ya existia
            dupla = mp.get(catalog['Nationalities'],nacionalidadArtista)
            listaObras = me.getValue(dupla)
        except:
            ## Caso en que la nacionalidad no existia
            listaObras = lt.newList()
        lt.addLast(listaObras,artwork)
        mp.put(catalog['Nationalities'],nacionalidadArtista, listaObras)
        
    ## En esta parte vamos a agregar el artwork a su correcto lugar en el mapa de Medium
    medium = artwork['Medium']
    if mp.contains(catalog['medium'],medium) :
        lista = mp.get(catalog['medium'], medium)
        valor = me.getValue(lista)
        lt.addLast(valor,artwork)
        mp.put(catalog['medium'],medium,valor)

    else:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(catalog['medium'], artwork["Medium"], lista)

    lt.addLast(catalog['artworks'], artwork)


