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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtistas(catalog)
    loadArtworks(catalog)

def loadArtistas(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    """
    Ejemplo de artista: {'ConstituentID': '10370', 'DisplayName': 'Edison Price, New York, NY', 'ArtistBio': ''
    , 'Nationality': '', 'Gender': '', 'BeginDate': '0', 'EndDate': '0', 'Wiki QID': '', 'ULAN': '',
    'Obras': [obra1,obra2] es un lt tho}"""
    artistfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    ejemplo  de artowrk:
    {
    'ObjectID': '147116', 
    'Title': '7', 
    'ConstituentID': '[6288]', 
    'Date': '1972', 
    'Medium': '33 1/3" LP',
    'Dimensions': '36:10 min.\n12 3/16 x 12 3/16" (31 x 31 cm)\n',
    'CreditLine': 'Partial gift of the Daled Collection and partial purchase through the generosity of Maja Oeri and Hans Bodenmann, Sue and Edgar Wachenheim III, Agnes Gund, Marlene Hess and James D. Zirin, Marie-Josée and Henry R. Kravis, and Jerry I. Speyer and Katherine G. Farley', 
    'AccessionNumber': '749.2011.a-b',
    'Classification': 'Audio', 
    'Department': 'Media and Performance', 
    'DateAcquired': '2011-05-19', 
    'Cataloged': 'Y', 
    'URL': 'http://www.moma.org/collection/works/147116', 
    'Circumference (cm)': '', 'Depth (cm)': '0', 'Diameter (cm)': '', 'Height (cm)': '31', 'Length (cm)': '', 
    'Weight (kg)': '', 'Width (cm)': '31', 'Seat Height (cm)': '', 'Duration (sec.)': ''
    'ArtistNames': ['','']
    'ArtistNationalities': ['','']
    }
    """
    artworkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def filtrarArtistasPorAños(catalog,añoInicial,añoFinal):
    listaRespuesta = model.filtrarArtistasPorAños(catalog,añoInicial,añoFinal)
    return listaRespuesta

def filtrarObrasPorAños(catalog,fechaInicial,fechaFinal):
    listaRespuesta = model.filtrarObrasPorAños(catalog,fechaInicial,fechaFinal)
    return listaRespuesta

def clasificarObrasDeArtistaPorTecnica(catalog, nombre):
    resultado = model.clasificarObrasDeArtistaPorTecnica(catalog, nombre)
    return resultado

def obrasPorNacionalidad(catalog):
     lista, nacionalidad, numNacionalidad, maparesp = model.obrasPorNacionalidad(catalog)
     return lista, nacionalidad, numNacionalidad, maparesp

def obrasDeDepartamento(catalog, departamento):
    resultado = model.obrasDeDepartamento(catalog, departamento)
    return resultado


## Funciones para el lab
def loadDatalab(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtistas(catalog)
    loadArtworkslab(catalog)

def loadArtworkslab(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    ejemplo  de artowrk:
    {
    'ObjectID': '147116', 
    'Title': '7', 
    'ConstituentID': '[6288]', 
    'Date': '1972', 
    'Medium': '33 1/3" LP',
    'Dimensions': '36:10 min.\n12 3/16 x 12 3/16" (31 x 31 cm)\n',
    'CreditLine': 'Partial gift of the Daled Collection and partial purchase through the generosity of Maja Oeri and Hans Bodenmann, Sue and Edgar Wachenheim III, Agnes Gund, Marlene Hess and James D. Zirin, Marie-Josée and Henry R. Kravis, and Jerry I. Speyer and Katherine G. Farley', 
    'AccessionNumber': '749.2011.a-b',
    'Classification': 'Audio', 
    'Department': 'Media and Performance', 
    'DateAcquired': '2011-05-19', 
    'Cataloged': 'Y', 
    'URL': 'http://www.moma.org/collection/works/147116', 
    'Circumference (cm)': '', 'Depth (cm)': '0', 'Diameter (cm)': '', 'Height (cm)': '31', 'Length (cm)': '', 
    'Weight (kg)': '', 'Width (cm)': '31', 'Seat Height (cm)': '', 'Duration (sec.)': ''
    'ArtistNames': ['','']
    'ArtistNationalities': ['','']
    }
    """
    artworkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtworkLab(catalog, artwork)
    
def pruebaMediumFunciona(catalog):
    return model.pruebaMediumFunciona(catalog)

    
def pruebaNationalityFunciona(catalog):
    return model.pruebaNationalityFunciona(catalog)