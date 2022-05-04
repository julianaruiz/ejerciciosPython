# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:21:30 2020

@author: JULI

Nombre:Juliana Ruiz Sánchez
Documetno:1001370876
Enunciado:Implemente el algoritmo de búsqueda de raíces para la función anterior 
usando el método exhaustivo. Para ello complete el archivo 
raices_exhaustivo_template.py guiándose por los comentarios en el código fuente y 
usando delta x=0.0001
análisis: -Entradas:
                inte=intervalo
                funcion=función ingresada
          -Salidas: 
              xl=raí a evaluar
              pasos=número de iteraciones
          -Auxiliares: 
              coma=lugar de la coma en el intervalo
              a=límite inferios
              b=límite superior
              epsilon=error
              delta=tamaño paso
              raíz=resultado de la función
"""
# Función
def f(funcion, x):
    f = eval(funcion) # agregar aquí el polinomio
    return f
# Variables del programa
inte=input('Ingrese un intervalo separado por comas: ')
coma=inte.index(',')
a=float(inte[:coma])  # Limite inferior
b=float(inte[coma+1:]) # Limite superior
pasos = 0 # Número de veces que se repite el ciclo
epsilon = 0.01 # Tolerancia al error
delta = 0.0001 # Tamaño de paso
 
# Inicialización de la variable que contendrá el valor de la raíz
funcion = input('Escriba una función a evaluar: ')
xl = a
raiz = f(funcion, xl) 
# Evaluación iterativa de la función en la raíz sospechada
while abs(raiz) > epsilon and xl <= b:
    pasos += 1
    xl += delta
    raiz = f(funcion, xl)
    # Actualización del número de pasos
    # Incremento de la variable que contiene la raíz
    # Evaluación iterativa de la función en la raíz sospechada
 
# Despliegue de los resultados
print('---------------------- Raiz exhaustiva --------------------------')
if xl > b:
    print('La raíz no fue encontrada')
else:
    print('La raíz de la función es aproximadamente: ', xl)
    
print('La cantidad de iteraciones fue: ', pasos)
