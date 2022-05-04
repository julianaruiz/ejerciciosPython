# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:36:30 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:1001370876
enunciado: 3.2.	Escriba un programa que le pida al usuario una palabra o frase y una letra. El programa deberá imprimir la misma frase 
o palabra ingresada, pero ocultando la letra que ingresó el usuario con un asterisco.
Análisis:
-Entrada: 
        pa=palabra o frase
        le=letra
-Salida: nf=nueva frase
"""
pa=input('Ingrese una palabra o frase ')
le=input('Ingrese letra a ocultar ')
nf=''
i=0
ta=len(pa)
while i<ta:
    if pa[i]==le:
        nf=nf+'*'
    else:
        nf=nf+pa[i]

    i=i+1
print(nf)

