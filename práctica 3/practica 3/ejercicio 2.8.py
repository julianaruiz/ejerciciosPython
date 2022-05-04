# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:06:21 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:: 1001370876
Enunciado: Una máquina dispensadora de productos requiere un algoritmo para calcular 
las devueltas en monedas. El objetivo del algoritmo es que dada una cantidad a devolver 
se debe calcular la combinación que genere la mínima cantidad de monedas, utilizando 
denominaciones de $1.000, $500, $200, $100 y $50. Si es imposible lograr la cantidad exacta, 
el sistema deberá decir lo que resta para lograrla.
Análisis: 
-entradas: d=monto a devolver
-Salidas: a=monedas de 1.000
          b=monedas de 500
          c=monedas de 200
          e=monedas de 100
          f=monedas de 50
          r=residuo
"""

d=int(input('Ingrese el monto a devolver '))
a=d//1000
b=(d%1000)//500
c=(d%500)//200
f=(d%100)//50
r=(d%100)%50
if d%200/100>=1:
    if (d%1000)//500==1:
        e=0
    else:
        e=1
else:
    if  (d%500)/200>=1:
        e=1
    else:
        if (d%200)/100>=1:
            e=0
        else:
            e=1
        
print('La devolución son ', a, 'monedas de 1.000')
print('La devolución son ', b, 'monedas de 500')
print('La devolución son ', c, 'monedas de 200')
print('La devolución son ', e, 'monedas de 100')
print('La devolución son ', f, 'monedas de 50')
print('El residuo es ', r)