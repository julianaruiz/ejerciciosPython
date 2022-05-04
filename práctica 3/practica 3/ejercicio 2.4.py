#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 04:35:05 2020

@author: drai06

Nombre: Juliana Ruiz Sánchez
Grupo:6
Documento:1001370876
Enunciado: En un sistema de bicicletas públicas se cobra a los usuarios $10 pesos por 
minuto de uso hasta un máximo de 2 horas. El tiempo adicional se cobra con un sobrecargo 
de $50 pesos por minuto, pero si supera las 24 horas se cobra un sobrecargo fijo de 
$100.000 pesos. Haga un algoritmo que calcule el monto a cobrar a un usuario dado el tiempo
que usó la bicicleta.
Análisis: 
    -Entrada: t=tiempo en minutos
    -Salida: c=sobrecargo
        
"""
t=int(input('Ingrese el tiempo en minutos '))
if t<=120:
    c=10*t
    print('El sobrecargo es ', c)
else:
    if t<1440:
        c=(t-120)*50+1200
        print('El sobrecargo es ', c)
    else:
        c=67150+100000
        print('El sobrecargo es ', c)
