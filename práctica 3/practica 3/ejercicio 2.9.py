# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:34:08 2020

@author: JULI

Grupo: 6
Nombre: Juliana Ruiz Sánchez
Documento: 1001370876
Enunciado:
Análisis:Haga un algoritmo para calcular el costo de un serivio de video streaming por demanda.El algoritmo recibirá el momento en que inició y terminó la reproducción de videos, 
mediante dos números enteros máximo de 6 dígitos, que representan las horas (00-23), los minutos (00-59) y los segundos (00-59). el c osto del servicio es de $2 pesos por segundo, 
con un cobro mínimo de $1000 pesos.
-Entrada: i=hora,minutoss y segundos de inicio
          f=hora, minutos y segundos de inicio
-Salida: t=total a pagar
-Auxiliares: si=segundo inicial
             mi=minuto final
             hi=hora inicial
             sf=segundo final
             mf=minuto final
             hf=hora final
             s=segundos totales
             m=minutos totales
             h=horas totales
"""
i=(input('Ingrese la hora, los minutos y los segundos de inicio '))
f=(input('Ingrese la hora, los minutos y los segundos de finalización '))
si=int(i)%100
mi=(int(i)%10000)-si
mi=mi//100
hi=int(i)//10000
sf=int(f)%100
mf=(int(f)%10000)-sf
mf=mf//100
hf=int(f)//10000
if sf<si:
    mf=mf-1
    sf=sf+60
    s=sf-si
else:
    s=sf-si
if mf<mi:
    hf=hf-1
    mf=mf+60
    m=(mf-mi)*60
else:
    m=(mf-mi)*60
if hf<hi:
    hf=hf+24
    h=(hf-hi)*3600
    t=(h+m+s)*2
else:
    h=(hf-hi)*3600
t=(h+m+s)*2
if t<1000:
                
    print('El valor a pagar es 1.000' )
else:
    print('El valor a pagar es ', t)
