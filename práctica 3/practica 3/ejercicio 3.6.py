3#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:34:32 2020

@author: drai06

Grupo:6
Nombre:Juliana Ruiz Sánchez
Documento:1001370876
Enunciado.Haga un aldoritmo que determine si un año es bisiesto o no.
Análisis:
-Entrada: a=año ingresado
-Salida: a=año bisiesto o no
"""
a=int(input('Ingrese un año '))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a, 'es bisiesto')
        else:
            print(a, 'no es bisiesto')
    else:
        print(a, 'es bisiesto')
else:
    print(a, 'no es bisiesto')