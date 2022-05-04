# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:38:19 2020

@author: juli

Nombre: Juliana Ruiz Sánchez
Documento: 1001370876

La Gobernación de Antioquia entrega cada año una ayuda económica a los municipios productores 
de aguacate que hayan sufrido períodos de mucha sequía (menos de 750 mm) o mucha lluvia 
(más de 2000 mm). Para los que sufrieron mucha sequía la cantidad de dinero de ayuda 
es 1.000.000 de pesos por cada hectárea de cultivo. Para los que sufrieron por mucha 
lluvia la ayuda es de 500.000 pesos por cada hectárea de cultivo. En el archivo 
pluviosidad_ant.log se encuentra el nombre de cada municipio, la cantidad de hectáreas de 
aguacate cultivadas y los milímetros de lluvia que cayeron en el año, como se muestra en este 
ejemplo:

Urrao:4790;2170

Jericó:1230;1050
Sonsón:2650;680
...

Para el archivo ejemplo mostrado, a Urrao le sería entregada una ayuda de 2.395.000.000 de 
pesos, a Sonsón 2.650.000.000 de pesos y a Jericó no se le daría ayuda.

Haga un programa en Python que lea el archivo, guarde toda la información en un diccionario y 
luego pregunte al usuario qué municipio quiere consultar. El programa deberá informar al 
usuario si el municipio no tiene derecho a subsidio o el valor de éste en caso de que sí. 
Luego, el programa debe preguntar repetidamente al usuario por otro municipio a consultar 
o la letra X para terminar.
"""

def lectura():

    datos=open('pluviosidad_ant.txt') 
    municipios={}
    for recorrer in datos:
        lis=recorrer.strip()
        i=0
        nf=''
        ta=len(lis)
        while i<ta:
            if lis[i]==':':
                nf=nf+';'
            else:
                nf=nf+lis[i]

            i=i+1
        lis=nf
        lis=lis.split(';')
        key=lis[0]
        d=lis[1:]
        municipios[key]=[int(d[0]),int(d[1])]
    return municipios
otro=True   
while otro:    
    munis=lectura()
    print("""Si desea salir del programa oprima la letra X'
          
¿Qué municipio quiere consultar? El programa diferencia entre mayúsculas y minúsculas'""")
    
    muni=input()
    if muni=='x' or muni=='X':
        otro=False
    else:
        while not muni in munis:
            print('Municipio no encontrado, por favor ingrese otro')
            muni=input()

        for i in munis:
            if muni==i:
                break

        if munis[i][1]<750:
            print('Ha sufrido periodos de sequia')
            cant=1000000*munis[i][0]
            print('El subsidio es de: ',str(cant)+'\n')
        elif munis[i][1]>2000:
            print('Ha sufrido periodos de lluvia')
            cant=500000*munis[i][0]
            print('El subsidio es de: ',str(cant)+'\n')
        else: 
            print('Este municipio no cuenta con subsidio debido a que no ha tenido periodos de sequía o lluvia')
        otro=True
    
   
    
    
    
    

 
