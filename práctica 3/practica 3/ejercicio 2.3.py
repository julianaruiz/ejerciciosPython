#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 03:57:30 2020

@author: drai06

Nombre: Juliana Ruiz Sánchez
Grupo:6
Documento:1001370876
Enunciado: Determinar el área y volumen de un cilindro, dada su altura y su radio.
Análisis: 
    -Entradas: 
        h=altura ingresada
        r=radio ingresado
    -Salidas: 
        a=área
        v=volúmen
"""

h=float(input('Ingrese la altura'))
r=float(input('Ingrese el radio'))
a=2*3.1416*r*h+2*3.1416*r**2
v=3.1416*r**2*h
print (a)
print (v)