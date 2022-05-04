#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 03:29:36 2020

@author: drai06

Nombre: Juliana Ruiz Sánchez
Grupo:6
Documento:1001370876
Enunciado: Haga un algoritmo que muestre el siguiente patrón en la pantalla:

#
###
#####
#######
#########

El tamaño del patrón estará determinado por un número entero impar que ingrese el usuario. En el ejemplo mostrado, el tamaño de la figura es 9.
Análisis: 
    -Entrada: n=número ingresado
    -Salida: t=número de # a mostrar
    -Auxiliares:
        a=#
        i=contador ciclo
    
"""
a='#'
i=1
n= int(input ('Ingrese un número impar '))
while (n%2)==0:
    n= int(input ('Ingrese un número impar '))

while i<=n:
    if i==1:
        t=a
        i=i+2
        print (t)
    else:
        t=t+a+a
        i=i+2
        print (t)