#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:42:12 2020

@author: drai06

Grupo:6
Nombre: Juliana Ruiz Sánchez
Documento: 1001370876
Enunciado: Haga un algoritmo que determine si un string, ingresado por el usuario, es un documento válido.
	Un documento válido tiene 10 dígitos (solo números).
Análisis:
-Entrada: d=documento ingresado
-Salida: d=documento válido o inválido
"""
d=input('Ingrese su documento ')
ta=len(d)

if int(d)>0:
    if ta==10:
        print(d, 'es un documento válido')
    else:
        print(d, 'es un documento inválido')
else:
    print(d, 'es un documento inválido')
