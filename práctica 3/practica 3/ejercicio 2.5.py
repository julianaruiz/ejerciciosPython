# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:37:02 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:1001370876
Enunciado: Teniendo en cuenta que un carro necesita cambio de aceite cada 6.000 km, haga 
un algoritmo que calcule cuántos cambios de aceite ha tenido un carro según el
total de kilómetros que ha recorrido.
Análisis:
-Entrada: k=kilómetros
-Salida: c=cambio de aceite 
"""

k=float(input('Total de kilómetros recorridos '))
if k>=6000:
    c=k//6000
    print('El cambio de aceite se ha hecho ', c, 'veces')
else:
    print('No se ha hecho cambio de aceite')