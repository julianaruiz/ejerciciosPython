# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:14:31 2020

@author: JULI
Grupo:6
Nombre:Juliana Ruiz Sánchez
Documetno:1001370876
Enunciado: implemente el algoritmo de búsqueda de raíces para la función anterior 
usando el método debisección. Para ello complete el archivo 
raices_biseccion_template.py guiándose por los comentarios en el código fuente.
Análisis: -Entradas: 
                inte=intervalo
                funcion=función ingresada
          -Salidas:
              f1=si la raíz es el límite inferior
              f2=si la raíz es el límite superior
              cen=si la finción está entre el límite inferior y superior
              pasos=número de iteraciones
          -Auxiliares:
              coma=lugar de la coma en el intervalo
              a=límite inferios
              b=límite superior
              epsilon=error
              fcen=resultado de la función con el número central
"""


# Función
def f(funcion, x):
    f = eval(funcion) # agregar aquí el polinomio
    return f
 
# Variables del programa
pasos = 0 # Número de veces que se repite el ciclo
inte=input('Ingrese un intervalo separado por comas: ')
coma=inte.index(',')
a=float(inte[0:coma]) # Limite inferior
b=float(inte[coma+1:]) # Limite superio
epsilon = 0.01 # Tolerancia
funcion = input('Escriba una función a evaluar: ')
cen = (a+b)/2
print(cen)
print('a ',a, 'b ',b)

# Evaluación de la función en los limites
f1 = f(funcion,a)
f2 = f(funcion,b)
fcen=f(funcion,cen) 
# Verificar que existe raíz en los limites
# Hay 4 posibilidades:
# 1. Que la raíz sea a. Si f1 == 0.
# 2. Que la raíz sea b. Si f2 == 0.
# 3. Que no haya raíz. Si f1*f2 > 0 (asumiendo que hay máximo una raíz en el intervalo)
# 4. Que la raíz se encuentre en el intervalo [a,b]. Si f1*f2 < 0
if f1==0:
    print('La raíz es: ', f1)
     
elif f2==0:
    print('La raíz es: ', f2)
     
elif f1*f2>0:
    print('No hay raíz en el intervalo')
         
elif f1*f2<0:
    while abs(fcen-0) > epsilon:
        pasos += 1

        if f1*fcen<0:
            b=cen
        else:
            a=cen
       
        cen=(a+b)/2
        fcen=f(funcion,cen)
        
        
    # Busqueda de la raíz dentro del intervalo
# Evaluación iterativa de la función en la raíz sospechada
    
    print('---------------------- Raiz exhaustiva --------------------------')
    if cen > b:
        print('La raíz no fue encontrada')
    else:
        print('La raíz de la función es aproximadamente: ', cen)
    
print('La cantidad de iteraciones fue: ', pasos)
        # Actualización de las iteraciones
         
        # Cálculo del punto medio del intervalo        
                 
        # Determinación del intervalo en el que se encuentra la raíz
         
        # Búsqueda de la raíz dentro del intervalo
 
# Despliegue de los resultados