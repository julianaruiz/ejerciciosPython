# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:44:02 2020

@author: juli
"""
from sortfunc import sortSeleccion, sortBurbuja
from random import uniform

def caja_negra_burbuja():
    
    """
    la función recibe una lista de números aleatorios con un mínimo, máximo
    y el tamaño de la lista para verificar el ordenamiento burbuja.
    """
    print("""
          
         Pruebas caja negra de ordenamiento burbuja""")
#Ordenar lista aleatoria crecientemente
    lista = [uniform(-50, 200) for i in range(100)] 
    copia = lista.copy()
    sortBurbuja(lista)
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. prueba a una lista en orden creciente para el ordenamiendo burbuja""")
    else:
        print("""
FALLO. prueba a una lista en orden creciente para el ordenamiendo burbuja""")

#Ordenar lista decrecientemente
    sortBurbuja(lista, 1)
    lista.sort(reverse=False)
    copia.sort(reverse=False)
    if lista == copia:
        print("""
EXITOSA. prueba para una lista ordenada creciente a decreciente para el ordenamiento burbuja""")
    else:
        print("""
FALLO. prueba para una lista ordenada  creciente a decreciente para el ordenamiento burbuja""")
         
#Ordenar lista aleatoria decrecientemente
    lista = [uniform(20, 80) for i in range(75)] 
    copia = lista.copy()
    cop=lista.copy()
    sortBurbuja(lista, 1)
    cop.sort(reverse=True)
    copia.sort(reverse=True)
    if cop == copia:
        print("""
EXITOSA. prueba a una lista decreciente para el ordenamiendo burbuja""")
    else:
        print("""
FALLO. prueba a una lista decreciente para el ordenamiendo burbuja""")

#Ordenar lista crecientemente
    sortBurbuja(lista)
    copia.sort(reverse=False)
    if lista == copia:
        print("""
EXITOSA. prueba para una lista decreciente a creciente para el ordenamiento burbuja""")
    else:
        print("""
FALLO. prueba para una lista decreciente a creciente para el ordenamiento burbuja""")
   
#Ordenar una lista vacía
    lista = []
    copia = lista.copy()
    sortBurbuja(lista)
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba lista vacía para ordenamiento burbuja""")
    else:
        print("""
FALLO. Prueba lista vacía para ordenamiento burbuja""")
    
def caja_negra_seleccion():
    """
    la función recibe una lista de números aleatorios con un mínimo, máximo
    y el tamaño de la lista para verificar el ordenamiento seleccion.
    """
    print("""
          
         Pruebas caja negra de ordenamiento seleccion""")
         
#Ordenar lista aleatoria crecientemente
    lista = [uniform(-50, 200) for i in range(100)] 
    copia = lista.copy()
    sortSeleccion(lista)
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. prueba a una lista aleatoria creciente para el ordenamiendo selección""")
    else:
        print("""
FALLO. prueba a una lista aleatoria creciente para el ordenamiendo selección""")

#Ordenar lista decrecientemente
    sortSeleccion(lista, 1)
    lista.sort(reverse=False)
    copia.sort(reverse=False)
    if lista == copia:
        print("""
EXITOSA. prueba para una lista ordenada creciente a decreciente para el ordenamiento selección""")
    else:
        print("""
FALLO. prueba para una lista ordenada  creciente a decreciente para el ordenamiento selección""")
         
#Ordenar lista aleatoria decrecientemente
    lista = [uniform(20, 80) for i in range(75)] 
    copia = lista.copy()
    cop=lista.copy()
    sortSeleccion(lista, 1)
    cop.sort(reverse=True)
    copia.sort(reverse=True)
    if lista == copia:
        print("""
EXITOSA. prueba a una lista aleatoria decreciente para el ordenamiendo selección""")
    else:
        print("""
FALLO. prueba a una lista aleatoria decreciente para el ordenamiendo selección""")

#Ordenar lista crecientemente
    sortSeleccion(lista)
    copia.sort(reverse=False)
    if lista == copia:
        print("""
EXITOSA. prueba para una lista decreciente a creciente para el ordenamiento selección""")
    else:
        print("""
FALLO. prueba para una lista decreciente a crecient para el ordenamiento selección""")
   
#Ordenar una lista vacía
    lista = []
    copia = lista.copy()
    sortSeleccion(lista)
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba lista vacía para ordenamiento selección""")
    else:
        print("""
FALLO. Prueba lista vacía para ordenamiento selección""")

def caja_blanca_burbuja():
    """
    Esta función hace pruebas de caja blanca al ordenamiento burbuja
    """
    print("""
          
         Pruebas caja blanca de ordenamiento burbuja""")
    #Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente
    lista = []
    sortBurbuja(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente""")
    else:   
       print("""
FALLO. Las listas deben ser iguales, no pueden existir listas vacías""")
    #Prueba de un arreglo vacío que no entra al ciclo más interno de forma decreciente
    lista = []
    sortBurbuja(lista, 1)
    copia = lista.copy()
    copia.sort(reverse=True)
    if lista == copia:
        print("""
EXITOSA. Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente""")
    else:   
       print("""
FALLO. Las listas deben ser iguales, no pueden existir listas vacías""")
    #Prueba con una lista con todos sus elementos desordenados
    lista = [54,26,93,17,77,31,44,55,20]
    sortBurbuja(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
       print("""
EXITOSA. Prueba con una lista con todos sus elementos desordenados""") 
    else:
        print("""
FALLO. Las listas deben ser iguales, elementos desordenados no pasaron del if""")
    #Prueba con una lista con todos sus elementos desordenados de manera decreciente
    lista = [31,26,20,17,77,54,44,55,93]
    sortBurbuja(lista, 1)
    copia = lista.copy()
    copia.sort(reverse=True)
    if lista == copia:
       print("""
EXITOSA. Prueba con una lista con todos sus elementos desordenados de manera decreciente""") 
    else:
        print("""
FALLO. Las listas deben ser iguales, elementos desordenados descendentemente no pasaron del if""")
    #Prueba con lista totalmente ordenada de forma creciente, nunca entra en las codiciones pero si en los ciclos
    lista = [-100,-60,-20,0,5,25,48,72,139.434]
    sortBurbuja(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba con lista totalmente ordenada de forma creciente, nunca entra en las codiciones""")
    else:
        print("""
FALLO. Las listas deben ser iguales, no entró al ciclo.""")
    #Prueba con lista totalmente ordenada de forma decreciente, nunca entra en las codiciones pero si en los ciclos
    lista = [10000,300,150,90.4,65,32,19,4,1,0,-3,-26,-54.5234]
    sortBurbuja(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba con lista totalmente ordenada de forma decreciente, nunca entra en las codiciones pero si en los ciclos""")
    else:
        print("""
FALLO. Las listas deben ser iguales, no entró al ciclo.""") 
 
    
def caja_blanca_seleccion():
    """
    Esta función hace pruebas de caja blanca al ordenamiento seleccion
    """
    print("""
          
         Pruebas caja blanca de ordenamiento seleccion""")
    #Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente
    lista = []
    sortSeleccion(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente""")
    else:   
       print("""
FALLO. Las listas deben ser iguales, no pueden existir listas vacías""")
    #Prueba de un arreglo vacío que no entra al ciclo más interno de forma decreciente
    lista = []
    sortSeleccion(lista, 1)
    copia = lista.copy()
    copia.sort(reverse=True)
    if lista == copia:
        print("""
EXITOSA. Prueba de un arreglo vacío que no entra al ciclo más interno de forma creciente""")
    else:   
       print("""
FALLO. Las listas deben ser iguales, no pueden existir listas vacías""")
    #Prueba con una lista con todos sus elementos desordenados
    lista = [54,26,93,17,77,31,44,55,20]
    sortSeleccion(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
       print("""
EXITOSA. Prueba con una lista con todos sus elementos desordenados""") 
    else:
        print("""
FALLO. Las listas deben ser iguales, elementos desordenados no pasaron del if""")
    #Prueba con una lista con todos sus elementos desordenados de manera decreciente
    lista = [31,26,20,17,77,54,44,55,93]
    sortSeleccion(lista, 1)
    copia = lista.copy()
    copia.sort(reverse=True)
    if lista == copia:
       print("""
EXITOSA. Prueba con una lista con todos sus elementos desordenados de manera decreciente""") 
    else:
        print("""
FALLO. Las listas deben ser iguales, elementos desordenados descendentemente no pasaron del if""")
    #Prueba con lista totalmente ordenada de forma creciente, nunca entra en las codiciones pero si en los ciclos
    lista = [-100,-60,-20,0,5,25,48,72,139.434]
    sortSeleccion(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba con lista totalmente ordenada de forma creciente, nunca entra en las codiciones""")
    else:
        print("""
FALLO. Las listas deben ser iguales, no entró al ciclo.""")
    #Prueba con lista totalmente ordenada de forma decreciente, nunca entra en las codiciones pero si en los ciclos
    lista = [10000,300,150,90.4,65,32,19,4,1,0,-3,-26,-54.5234]
    sortSeleccion(lista)
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        print("""
EXITOSA. Prueba con lista totalmente ordenada de forma decreciente, nunca entra en las codiciones pero si en los ciclos""")
    else:
        print("""
FALLO. Las listas deben ser iguales, no entró al ciclo.""")    
    
caja_negra_burbuja()
caja_negra_seleccion()
caja_blanca_burbuja()
caja_blanca_seleccion()