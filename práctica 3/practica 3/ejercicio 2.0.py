# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:23:17 2020

@author: JULI

Grupo:6
Nombre:Juliana Ruiz Sánchez
Documento:1001370876
Enunciado: Haga un algoritmo que haga división entera de dos números sin el operador //
Análisis:
-Entradas: 
    n1=número a dividir
    n2=número divisor
-Salida: n=número resultante
-Auxiliar: m=número decimal 
"""

n1=int(input('Ingrese el número a dividir '))
n2=int(input('Ingrese el divisor '))
if n1%n2==0:
    n=n1/n2
else:
    n=n1/n2
    m=n%1
    n=n-m
print(n)