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
    catalog['medium'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=comparebyMedium)
    catalog['objectId'] =  mp.newMap(100,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareArtworksbyObjectID)
    return catalog
# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    """
    Edita el artwork para que busque sus artistas y las nacionalidades de estos artistas y los guarda
    Agrega el artwork que se suministro al catalog usando su objectID como su llave
    """
    #constituentIds = artwork['ConstituentID'].split(",")  # Se obtienen los autores
    ##for constituentId in constituentIds :
        #ARREGLAMOS LOS CONSTITUENTID ANTES DE UTILIZARLOS
        ##Id = constituentId.strip()
        ##Id = Id.strip("[")
        ##Id = Id.strip("]")
        
        # UTILIZAMOS LOS CONSTITUENTID INDIVIDUALES PARA ASIGNAR NOMBRE Y NACIONALIDAD A LAS ARTWORKS
        # TAMBIEN SE AGREGA ESTA OBRA A LAS OBRAS DEL ARTISTA AL CUAL REFERENCIA
        #artists = catalog['artists']
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

def addArtist(catalog, artist):
    """
    Agrega el artist al mapa artists del catalogo usando su ConsituentID como llave y agregandole un 
    nuevo parametro llamado obras el cual guarda todas las obras que este artista tenga a su nombre"""
    artist["Obras"]= lt.newList()
    mp.put(catalog['artists'],artist['ConstituentID'],artist)


def addArtworkLab(catalog,artwork):
    """
    Funcion para agregar el artwork a la lista y despues agregar al mapa medium
    """
    lt.addLast(catalog['artworks'],artwork)
    


# Funciones para creacion de datos

# Funciones de consulta
def getOldByMedium(catalog,number,medium):
    listaRespuesta = lt.newList("ARRAY_LIST")
    listArtworks = (mp.get(catalog['medium'],medium))
    print(listArtworks== None)
    print(listArtworks)
    listArtworks = me.getValue(listArtworks)
    iteracion = lt.iterator(listArtworks)
    for artwork in iteracion:
        if (artwork['Medium'] == medium):
            lt.addLast(listaRespuesta,artwork)
    sa.sort(listaRespuesta,compareByDate)
    listaRespuesta = lt.subList(listaRespuesta,0,int(number))
    return listaRespuesta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Funciones de Comparacion
def compareByDate(artwork1,artwork2):
     return ((artwork1['Date'] < artwork2['Date']))

def compareArtworksbyObjectID(id, entry):
    """
    Compara dos ids de los artowrks, id es un identificador
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

def comparebyMedium(id, entry):
    """
    Compara dos mediums, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (id) == (identry):
        return 1
    elif ((id) > (identry)):
        return 0
    else:
        return 0


