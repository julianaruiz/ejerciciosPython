# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:29:12 2020

@author: JULI


Grupo:6
Nombre:Juliana Ruiz Sánchez
Documento:1001370876
Enunciado:Haga un algoritmo que, dado un string ingresado por el usuario, determine si es una fecha válida o no. La fecha válida debe cumplir con el formato "yyyy-mm-dd".
Amálisis:
-Entrada: fe=fecha ingresada
-Salida: 'fecha inválida', 'fecha válida', 'fecha inválida, no es bisiesto'
-Auxiliares:
    ta=tamañño fecha
    i=contador
    ac=acumulador
    mes=unión de los caracteres en las posiciones 5 y 6
    dias=unión de los caracteres en las posiciones 8 y 9
"""
fe=input('Ingrese una fecha en formato yyyy-mm-dd válida ')
ta=len(fe)
i=0
ac=''

if ta==10:
    
    while fe[i] in '0,1,2,3,4,5,6,7,8,9':
        ac=ac+fe[i]
        i=i+1
        
    mes=fe[5]+fe[6]
    dias=fe[8]+fe[9]
            
    if fe[5]=='0' and fe[6]=='2':
        if fe[8]=='2' and fe[9]=='9':
            if int(ac)%4==0:
                if int(ac)%100==0:
                    if int(ac)%400==0:
                        if fe[4]=='-' and fe[7]=='-': 
                            print('Fecha válida')
                        else:  
                                print('Fecha inválida')
                    else:   
                        print('Fecha inválida') 
                else:
                    if fe[4]=='-' and fe[7]=='-': 
                        if int(mes)<=12 and int(dias)<=31:
                            print('Fecha válida')
                        else: 
                            print('Fecha inválida') 
                    else:  
                        print('Fecha inválida')
                        
            else: 
                print('Fecha inválida')                               
        else:
            if fe[4]=='-' and fe[7]=='-': 
                if int(mes)<=12 and int(dias)<=31:
                    print('Fecha válida')
                else: 
                    print('Fecha inválida') 
            else:  
                print('Fecha inválida')
                        
                
    else:
        if fe[4]=='-' and fe[7]=='-': 
            if int(mes)<=12 and int(dias)<=31:
                print('Fecha válida')
            else: 
                print('Fecha inválida') 
        else:  
            print('Fecha inválida')
else:
    print('Fecha inválida')
                        
