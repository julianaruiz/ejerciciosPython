#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 03:02:25 2020

@author: drai06

Nombre: Juliana Ruiz Sánchez
Grupo:6
Documento:1001370876
Enunciado: Dado el valor del lado de un triángulo equilátero, 
haga un algoritmo que calcule su perímetro, su altura y su área.
Análisis: 
    -Entrada: l=medida del lado
    -Salidas: 
        p=perímetro
        h=altura
        a=área
"""

l=int( input('Ingrese un número '))
p=l+l+l
h=((3**(1/2))*l)/2
a=(l*h)/2
print (p)
print (h)
print (a)