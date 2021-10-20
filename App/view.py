"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

from os import times
import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from prettytable import PrettyTable


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - Req 1 - Listar cronológicamente los artistas")
    print("3 - Req 2 - Listar cronologicamente las adquisiciones")
    print("4 - Req 3 - Clasificar las obras de un artista por técnica")
    print("5 - Req 4 - Clasificar las obras por nacionalidad de sus creadores")
    print("6 - Req 5 - Transportar obras de un departamento")
    print("7 - Req 6 ")
    print("8 - Requerimiento laboratorio 6")
        

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)

    elif int(inputs[0]) == 2:
        #Requerimiento 1
        start = time.time()
        añoInicial = input('Desde que año quieres hacer la busqueda: ')
        añoFinal = input('Hasta que año quieres hacer la busqueda: ')
        listaRango = controller.filtrarArtistasPorAños(catalog, añoInicial, añoFinal)
        print(lt.getElement(listaRango,1))
        print(lt.getElement(listaRango,2))
        print(lt.getElement(listaRango,3))
        end = time.time()
        print(end - start)

    elif int(inputs[0]) == 3:
        #Requerimiento 2
        start = time.time()
        fechaInicial = input('Desde que fecha quieres hacer la busqueda: ')
        fechaFinal = input('Hasta que fecha quieres hacer la busqueda: ')
        listaRango = controller.filtrarObrasPorAños(catalog, fechaInicial, fechaFinal)
        print('')
        print("=============== Req No. 2 Inputs ===============")
        print("Artworks acquired between " + str(fechaInicial) + " and " + str(fechaFinal))
        print('')
        print('=============== Req No. 2 Answer ===============')
        print('The MoMa acquired ' + str(listaRango[1]) + ' unique pieces bewteen' + str(fechaInicial) + " and " + str(fechaFinal))
        print("The first and last 3 artworks in range are...") 
        itable = PrettyTable(["ObjectID", "Title", "ArtistNames", "Medium", "Dimensions", "Date", "DateAcquired", "URL"])

        q1 = 1
        k1= 1
        ca1 = 0
        while ca1 < 3:
            respuesta1 = lt.getElement(listaRango[0], q1)
            respuesta = respuesta1['obras']
            elemento = lt.getElement(respuesta, k1)
            if k1 >= lt.size(respuesta):
                q1 = q1 + 1
                k1 = 1
            else: k1 = k1 + 1
            #elemento = lt.getElement(elemento1, ca1)
            #Nombres a string
            lista = lt.iterator(elemento['ArtistNames'])
            devuelta = ''
            for name in lista:
                devuelta = devuelta + ',' +name

            itable.add_row([elemento['objectID'], elemento['Title'], devuelta, elemento['Medium'], elemento['Dimensions'], elemento['Date'], elemento['DateAcquired'], elemento['URL']])
            ca1 = ca1 + 1


        q1 = lt.size(listaRango[0])
        k1= lt.size(lt.getElement(listaRango[0], q1)['obras'])
        ca1 = 0
        while ca1 < 3:
            respuesta1 = lt.getElement(listaRango[0], q1)
            respuesta = respuesta1['obras']
            elemento = lt.getElement(respuesta, k1)
            if k1 == 1:
                q1 = q1 - 1
                k1 = lt.size(lt.getElement(listaRango[0], q1)['obras'])
            else: k1 = k1 - 1
            lista = lt.iterator(elemento['ArtistNames'])
            devuelta = ''
            for name in lista:
                devuelta = devuelta + name

            itable.add_row([elemento['objectID'], elemento['Title'], devuelta, elemento['Medium'], elemento['Dimensions'], elemento['Date'], elemento['DateAcquired'], elemento['URL']])
            ca1 = ca1 + 1

        print(itable)
        end = time.time()
        print(end - start)


    elif int(inputs[0]) == 4:
        #Requerimiento 3
        start = time.time()
        artist = input('Que artista quieres buscar: ')
        result = controller.clasificarObrasDeArtistaPorTecnica(catalog, artist)
        print("=============== Req No. 3 Inputs ===============")
        print('Examine the work of the artist named: ' + artist)
        print('')
        print('=============== Req No. 3 Answer ===============')
        print(artist + ' with MoMA ID ' + str(result[0]['ConstituentID']) + ' has ' + str(lt.size(result[0]['Obras'])) + ' in his/her name at the musem.')
        print('There are ' + str(result[2]) + ' different mediums/techniques in his/her working')

        

        #print = lt.getElement(result[0]['Artworks']['elements'], 1)\
        mtable = PrettyTable(['MediumName', 'Count'])
        for num in range(1, lt.size(result[1])):
            m1 = lt.getElement(result[1], num)
            mtable.add_row([m1['Medium'], m1['Number']])
            if num == 5:
                break
        medium = lt.getElement(result[1], 1)
        print(medium)
        medium2 = medium['Medium']
        print('His/Her most used Medium/Technique is: ' + str(medium2) + ' with ' + str(medium['Number']) + ' pieces.')
        print(mtable)
        
        ttable = PrettyTable(['ObjectID', 'Title', 'Medium', 'Dimensions', 'DateAcquired', 'Department', 'Classification', 'URL'])
        
        contador = 0
        for art in range(lt.size(medium['Obras']) - 4, lt.size(medium['Obras']) - 1):
            m1a = lt.getElement(medium['Obras'], art)
            if contador == 4:
                break
            
            ttable.add_row([m1a['ObjectID'], m1a['Title'], m1a['Medium'], m1a['Dimensions'], m1a['DateAcquired'], m1a['Department'], m1a['Classification'], m1a['URL']])
            contador = contador + 1
        print('')
        print('His/Her most used Medium/Techniques is: ' + medium2 + ' with ' + str(contador) + ' pieces.')
        print('A sample of ' + str(contador) + ' ' + medium2 + ' from the collection are:')
        print(ttable)
        end = time.time()
        print(end - start)
    

    elif int(inputs[0]) == 5:
        #Requerimiento 4
        print("Ranking countries by their number of artworks in the MoMA")
        lista, nacionalidad, numNacionalidad, maparesp = controller.obrasPorNacionalidad(catalog)

        print("======================= Req No.4 Answer ====================")
        print(" ")
        print("Top 10 countries in the MoMA are:")

        table = PrettyTable(['Nationality','Artworks'])
        # Ok necesitamos organizar un mapa, entonces lo que vamos a hacer es crear una nueva lista que tenga las llaves en el orden
        # de su mayor a menor
        keyset = mp.keySet(maparesp)

        listaMaxKey = lt.newList()

        for i in range(10):
            iteradorset = lt.iterator(keyset)
            max = 0
            maxkey = ""
            cent = 1
            cent2 = 1
            for key in iteradorset:
                if me.getValue(mp.get(maparesp,key)) > max:
                    max = me.getValue(mp.get(maparesp,key))
                    maxkey = key
                    cent2 = cent
                cent += 1
            lt.addLast(listaMaxKey,maxkey)
            lt.deleteElement(keyset,cent2)

        iterador2 = lt.iterator(listaMaxKey)
        for llave in iterador2:
            print(llave)
            table.add_row([llave,me.getValue(mp.get(maparesp,llave))])

        print(table)

        print("The top Nationality in the museum is: ", nacionalidad , "With ",numNacionalidad ," Unique Pieces")
        print("The first and last 3 objects in the american artworks list are:")

        table2 = PrettyTable(["ObjectID","Title","Artists Names","Medium","Date","Dimensions","Department","Clasification","URL"])
        last1 = lt.getElement(lista , lt.size(lista)-1)
        last2 = lt.getElement(lista , lt.size(lista)-2)
        last3 = lt.getElement(lista, lt.size(lista)-3)
        
        for ind in range(1, 4):
            nombresArtistas = ''
            first1 = lt.getElement(lista,ind)
            itera = lt.iterator(first1['ArtistNames'])
            for nombre in itera:
                nombresArtistas = nombresArtistas +" "+ nombre

            table2.add_row([first1['ObjectID'],first1['Title'],nombresArtistas,first1['Medium'],first1['Date'],first1['Dimensions'],first1['Department'],first1['Classification'],first1['URL']])
 
        for ind in range(1, 4):
            nombresArtistas = ''
            last2 = lt.getElement(lista,lt.size(lista)-ind)
            itera2 = lt.iterator(last2['ArtistNames'])
            for nombre in itera2:
                nombresArtistas = nombresArtistas +" "+ nombre
            table2.add_row([last2['ObjectID'],last2['Title'],nombresArtistas,last2['Medium'],last2['Date'],last2['Dimensions'],last2['Department'],last2['Classification'],last2['URL']])


        print(table2)
        



    elif int(inputs[0]) == 6:
        #Requerimiento 5
        start = time.time()
        dep = input('Departamento que se busca investigar: ')
        result = controller.obrasDeDepartamento(catalog, dep)
        print("=============== Req No. 5 Inputs ===============")
        print('Estimate the cost to transport all artifacts in ' + dep + ' Departament')
        print('')
        print('=============== Req No. 5 Answer ===============')
        print('The MOMA is going to transport ' + str(lt.size(result[0])) + ' from the ' + dep)
        print('Estimated cargo weight (kg): ' + str((result[2])))
        print('Estimated cargo cost (USD): ' + str((round(result[3], 3))))
        print('')
        prim1 = lt.getElement(result[0], 1)
        prim2 = lt.getElement(result[0], 2)
        prim3 = lt.getElement(result[0], 3)
        prim4 = lt.getElement(result[0], 4)
        prim5 = lt.getElement(result[0], 5)
        prim1a = prim1['dep']
        prim2a = prim2['dep']
        prim3a = prim3['dep']
        prim4a = prim4['dep']
        prim5a = prim5['dep']
        #print('ObjectID: ' + prim1['ObjectID'] + ', Title:' + prim2['Title'] + ', ArtistsNames' + prim1['ConsituentID'] + ', Medium' + prim1['Medium'] + ', Date' + prim1['Date'] + ', Dimensions: ' + prim1['Dimensions'] + ', Classification:' + prim1['Classification'] + ', TransCost (USD):' + (lt.getElement(result[0], 1)) + ', URL' + )
        prim1c = lt.getElement(result[1], 1)
        prim2c = lt.getElement(result[1], 2)
        prim3c = lt.getElement(result[1], 3)
        prim4c = lt.getElement(result[1], 4)
        prim5c = lt.getElement(result[1], 5)
        prim1b = prim1c['dep']
        prim2b = prim2c['dep']
        prim3b = prim3c['dep']
        prim4b = prim4c['dep']
        prim5b = prim5c['dep']
        print('The TOP 5 most expensive items to transport are:')
        table = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Date", "Dimensions", "Classification", "Transcost (USD)", "URL"])
        table.add_row([str(prim1a["ObjectID"]), str(prim1a["Title"]), '(prim1a["ArtistsNames"]["elements"])', str(prim1a["Medium"]), str(prim1a["Date"]), str(prim1a["Dimensions"]), str(prim1a["Classification"]), str(prim1['price']), str(prim1a["URL"])])
        table.add_row([str(prim2a["ObjectID"]), str(prim2a["Title"]), '(prim2a["ArtistsNames"]["elements"])', str(prim2a["Medium"]), str(prim2a["Date"]), str(prim2a["Dimensions"]), str(prim2a["Classification"]), str(prim2['price']), str(prim2a["URL"])])
        table.add_row([str(prim3a["ObjectID"]), str(prim3a["Title"]), '(prim3a["ArtistsNames"]["elements"])', str(prim3a["Medium"]), str(prim3a["Date"]), str(prim3a["Dimensions"]), str(prim3a["Classification"]), str(prim3['price']), str(prim3a["URL"])])
        table.add_row([str(prim4a["ObjectID"]), str(prim4a["Title"]), '(prim4a["ArtistsNames"]["elements"])', str(prim4a["Medium"]), str(prim4a["Date"]), str(prim4a["Dimensions"]), str(prim4a["Classification"]), str(prim4['price']), str(prim4a["URL"])])
        table.add_row([str(prim5a["ObjectID"]), str(prim5a["Title"]), '(prim5a["ArtistsNames"]["elements"])', str(prim5a["Medium"]), str(prim5a["Date"]), str(prim5a["Dimensions"]), str(prim5a["Classification"]), str(prim5['price']), str(prim5a["URL"])])
        print(table)
        end = time.time()
        print(end - start)

        print('')

        print('The TOP 5 most oldests items to transport are:')
        table2 = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Date", "Dimensions", "Classification", "Transcost (USD)", "URL"])
        table2.add_row([str(prim1b["ObjectID"]), str(prim1b["Title"]), (prim1b["ArtistsNames"]['elements']), str(prim1b["Medium"]), str(prim1b["Date"]), str(prim1b["Dimensions"]), str(prim1b["Classification"]), str(prim1c['Date']), str(prim1b["URL"])])
        table2.add_row([str(prim2b["ObjectID"]), str(prim2b["Title"]), (prim2b["ArtistsNames"]['elements']), str(prim2b["Medium"]), str(prim2b["Date"]), str(prim2b["Dimensions"]), str(prim2b["Classification"]), str(prim2c['Date']), str(prim2b["URL"])])
        table2.add_row([str(prim3b["ObjectID"]), str(prim3b["Title"]), (prim3b["ArtistsNames"]['elements']), str(prim3b["Medium"]), str(prim3b["Date"]), str(prim3b["Dimensions"]), str(prim3b["Classification"]), str(prim3c['Date']), str(prim3b["URL"])])
        table2.add_row([str(prim4b["ObjectID"]), str(prim4b["Title"]), (prim4b["ArtistsNames"]['elements']), str(prim4b["Medium"]), str(prim4b["Date"]), str(prim4b["Dimensions"]), str(prim4b["Classification"]), str(prim4c['Date']), str(prim4b["URL"])])
        table2.add_row([str(prim5b["ObjectID"]), str(prim5b["Title"]), (prim5b["ArtistsNames"]['elements']), str(prim5b["Medium"]), str(prim5b["Date"]), str(prim5b["Dimensions"]), str(prim5b["Classification"]), str(prim5c['Date']), str(prim5b["URL"])])
        print(table2)
        


    elif int(inputs[0]) == 7:
        print("Req6")

    elif int(inputs[0]) == 8:
        print("Cargando información de los archivos para el LAB 6....")
        timeinicial = time.time()
        catalog = controller.initCatalog()
        controller.loadDatalab(catalog)
        print("Existen :",lt.size(controller.pruebaMediumFunciona(catalog)),"Obras Con el medium Glass")
        print('---------------------------------------------')
        print("Existen: ",lt.size(controller.pruebaNationalityFunciona(catalog)), " Artistas Americanos")
        print("Carga Existosa")
        print("La carga se demoro: ", time.time()-timeinicial)
    else:
        sys.exit(0)
sys.exit(0)
