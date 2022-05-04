#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 03:12:36 2020

@author: drai06
Grupo:6
Nombre:Juliana Ruiz Sánchez
Documetno:1001370876
Enunciado:Implemente el algoritmo de búsqueda lineal, completando el archivo 
busqueda_lineal_template.py y guiándose por las indicaciones que aparecen en los 
comentarios. Ayuda: recuerde el uso de la instrucción break. 
-Imprima un mensaje donde se muestre el valor a buscar
-Imprima el mensaje en el cual se muestre cada elemendo de la iteración   
-Imprima el mensaje en el cual se informe la posición
-en la que se encontró el número, o un mensaje indicando que no se encontró
-Imprima la cantidad de iteraciones que hizo el ciclo
Análisis:
    -Entrada: num=número ingresado
    -Salidas:
        i=número de iteraciones
        l[i]=número en la posición i
    -Auxiliares: 
        l=lista
        ta=tamaño lista
        lis=número en la posición i
    

"""

num=input('Ingrese un número ')
l=[-50,-45,-23,-21,-14,-9,-2,0,1,3,5,16,17,24,29,30,40,52,53,92]
i=0
ta=len(l)
while i<ta:
    lis=l[i]
    print('Iteración: ', i, 'Número=', l[i])
    
    if lis==int(num):
        print('Se encontró en la posición ', i)
        print('El número de iteracciones fueron ',i+1)
        break
    else:  
         i=i+1

if lis!=int(num):       
    print('El número no está en la lista')
    print('El número de iteraciones fueron ', i)

  
    
    