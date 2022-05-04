# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:59:40 2020

@author: JULI

Grupo:6
Nombre:Juliana Ruiz Sánchez
Documento.1001370876
Enunciado:3.3.	Haga un programa que determine si una palabra ingresada por el usuario es palíndroma o
no. Utilice la instrucción while.
Análisis: 
-Entrada: pal=palabra
-auxiliares: ta=tamaño de la palabra
             i=contador en aumento
             com=comprobador de espacio
             c=contador  disminuyendo
"""

pal=input('Ingrese una palabra ')
ta=len(pal)
i=0
com=0
c=ta-1
npal=''
while com<ta:
    if pal[com]==' ':
        pal=input('Ingrese una palabra ')
    else:
        com=com+1

while i<ta:
    if pal[i]==pal[c]:
        npal=npal+pal[c]
        
    c=c-1
    i=i+1
if npal==pal:   
    print('Es palindroma')
else:
    print('No es palindroma')