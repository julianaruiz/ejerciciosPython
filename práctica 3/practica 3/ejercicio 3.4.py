# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:17:53 2020

@author: JULI

Grupo:6
Nombre:Juliana Ruiz Sánchez
Documetno:1001370876
Enunciado: Reciba una palabra del usuario y un número entero menor que 26. El programa debe cambiar cada letra por la que 
le corresponda al dar saltos en el alfabeto de acuerdo al número especificado por el usuario. La nueva palabra codificada 
deberá ser mostrada en pantalla.
Análisis:
"""

pal=input('Ingrese una palabra ')
ta=len(pal)
i=0
com=0
c=0
np=''
alf='abcdefghijklmnopqrstuvwxyz'  
while com<ta:
    if pal[com]==' ':
        pal=input('Ingrese solo una palabra ')
    else:
        com=com+1
    
n=int(input('Ingrese un número '))
while i<ta:
    c=alf.index(pal[i])
    c=c+n
    if c>26:
        c=c-26
    else:
        if c<0:
            c=26+c
    np=np+alf[c]
    i=i+1
print(np)
    
  