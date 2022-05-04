# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:29:57 2020

@author: JULI

Grupo:6
Nombre:Juliana Ruiz Sánchez
Documetno:1001370876
Enunciado:Implemente el algoritmo de búsqueda binaria, completando el archivo
busqueda_binaria_template.py y guiándose por las indicaciones que aparecen en los 
comentarios.
Análisis:
    -Entrada: num=número ingresado
    -Salida: i=número iteraciones
             cen=valor central
             l[i]=número en la posición i
    -Auxiliares: l=lista
                 ta=límite superior
                 lis=número en la posición cen
                 it=límite inferior
                 
"""
num=int(input('Ingrese un número '))
l=[-50,-45,-23,-21,-14,-9,-2,0,1,3,5,16,17,24,29,30,40,52,53,92]
i=0
it=0
ta=len(l)-1
cen=(ta+it)//2
lis=l[cen]


while it <= ta:
    print('Número iteración: ', i+1, 'valor central: ', cen, 'l[cen]', lis, 'Intervalo: ', l[it:ta+1])
    if l[cen] == num:
        print('Se encontró en la posición ', cen)
        print('El número de iteracciones fueron ',i+1)
        break
    if num<lis:
        ta=cen-1
    else:
        it=cen+1
    i+=1
    cen=(ta+it)//2
    lis = l[cen]
if lis!=num:
    print('No se encontró en la lista')