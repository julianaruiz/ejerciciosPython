#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 02:13:09 2020

@author: drai06

Nombre: Juliana Ruiz Sánchez
Grupo:6
Documento:1001370876
Enunciado: Haga un algoritmo que muestre el siguiente patrón en la pantalla:

*            *
***        ***
*****    *****
**************


El tamaño del patrón estará determinado por un número entero impar que ingrese el usuario.
Análisis:
    -Entrada: n=número ingresado impar
    -Salidas: 
        t=número de * a mostrar
        cd=número final de * a mostrar
    -Auxiliares: 
        a=*
        ce=contador de espacios
        cte=espacios total
        cd=acumulador de *
        i=contador de filas
        b=' '(espacio)
        e=acumulador de espacios
"""

n= int(input ('Ingrese un número impar '))
while (n%2)==0:
    n= int(input ('Ingrese un número impar '))

a='*'
ce=1
cte=n*2-2
cd=a
i=1
b=' '
e=b
while ce<cte:
    ce=ce+1
    e=e+b
    
while i<=n:
    if i==1:
        t= a+e+a
        i=i+2
        cd=cd+a
        print (t)
        t=a
    else:
        ce=1
        cte=cte-4
        e=b
        while ce<cte:
            ce=ce+1
            e=e+b
                
        if i==n:
            cd=cd+a+cd+a
            print (cd)
            i=i+2
        else:
            t=cd+a+e+cd+a
            i=i+2
            cd=cd+a+a
            print (t)
    
    