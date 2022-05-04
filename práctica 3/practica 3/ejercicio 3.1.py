# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:15:40 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento:1001370876
enunciado: Escriba un programa que tome un carácter (es decir, un string de longitud 1) y determine si el carácter es vocal o consonante.
Análisis:
-Entrada: le=letra
-Salida: le=vocal o consonante
-Auxiliares:
    vocal=ocales del abecedario
    consonantes=consonantes del abecedario
#"""

le=input('Ingrese una letra ')
vocal=['a','A','e','E','i','I','o','O','u','U']
consonante=['q','Q','w','W','r','R','t','T','y','Y','p','P','s','S','d','D','f','F','g','G','h','H','j','J','k','K','l','L','ñ','Ñ','z','Z','x','X','c','C','v','V','b','B','n','N','m','M']
if le in vocal:
    print(le, ' es una vocal')
else:
    if le in consonante:
        print(le, ' es una consonante')