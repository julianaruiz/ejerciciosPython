# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:53:17 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:1001370876
Enunciado: Haga un algoritmo que muestre en pantalla las soluciones de la ecuación ax2+bx+c==0, dados valores para los coeficientes a, b y c.
Análisis:
-Entradas: a=primer número
           b=segundo número
           c=tercer número
-Salidas: x=valor de la ecuación
          x1=valor de la ecuación
          x2valor de la ecuación
"""
a=int(input('Ingrese el primer número '))
b=int(input('Ingrese el segundo número '))
c=int(input('Ingrese el tercer número '))
d=pow(b,2)-4*a*c
if d<0:
    print('Las soluciones son complejas')
else:
    if d>0:
        x1=(-b+(d**0.5))/(2*a)
        x2=(-b-(d**0.5))/(2*a)
        print('Las respetas son: ', x1, x2)
    else:
        x=-b/(2*a)
        print('La respuesta es: ', x)