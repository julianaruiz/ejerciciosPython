# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:07:40 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:1001370765
Enunciado: Haga un algoritmo que diga si un número ingresado es perfecto o no. 
Un número perfecto es un número que es igual a la suma de sus divisores propios 
positivos. De esta forma, 6 es un número perfecto porque sus divisores propios 
son 1, 2 y 3; y 6 = 1 + 2 + 3.
Análisis:
-Entrada: n=número ingresado
-Salida: n=número ingresado
-Auxiliares: d=contador
             s=suma de los números propios
"""

n=int(input('Ingrese un número '))
d=1
s=0
while d<=n/2:
    if n%d==0:
        s=s+d
        d=d+1
    else:
        d=d+1
        
if s==n:
    print(n, 'es un número perfecto')
else:
    print(n, 'no es un número perfecto')