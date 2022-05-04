# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:40:25 2020

@author: JULI
"""
def Base_de_datos():
    # Almacenar en listas la información, edición, eliminación y creación de los usuarios registtrados, 
    # las estaciones existentes en el sistema, las variables monitoreadas, los municipios y el registro 
    # de medidas.
    global new_estaciones
    datos=open('registros(1).txt')
    usuarios={}
    estaciones={}
    amb1={}
    amb2={}
    amb3={}
    amb4={}
    datos_estaciones={}


    for recorrer in datos:
        if recorrer[0]=='<':
            new=recorrer.lstrip('<')
            new=new.strip()
            new=new.rstrip('>')
            new=new.split(';')
            key=new[0]
            d=new[1:]
            usuarios[key]=[d[0], int(d[1]), d[2]]
            
        
        elif recorrer[0]==':':   
            new=recorrer.lstrip(':')
            new=new.strip()
            new_estaciones=new.split(',')
            
            
        elif recorrer[0]=='2' and recorrer[1]=='0':
        
            nf=''
            i=0
            ta=len(recorrer)
            while i<ta:
                if recorrer[i]==',' or recorrer[i]=='{' or recorrer[i]=='}':
                    nf=nf+';'
                else:
                    nf=nf+recorrer[i]

                i=i+1
            recorrer=nf
            new=recorrer.strip()
            new=new.rstrip(';')
                
            new=new.split(';')
            dat1=new[0:2]
            dat2=new[3:7]
            new=dat1 + dat2
            
            key=new[0]
            d=new[1:]
            datos_estaciones[key]=[d[0], d[1], d[2], d[3], d[4]]
        
        
        elif recorrer[0] in '1234567890':
            new=recorrer.strip()
            new=new.split(',')
            key=new[0]
            d=new[1:]
            estaciones[key]=[d[0], d[1]]
            
        
        elif 'PM' in recorrer:
            linea1=recorrer.strip()
            nf=''
            i=0
            ta=len(linea1)
            while i<ta:
                if linea1[i]=='[' or linea1[i]==':' or linea1[i]==',':
                    nf=nf+';'
                else:
                    nf=nf+linea1[i]

                i=i+1
            linea1=nf
            nf=''
            i=0
            while i<ta:
                if linea1[i]==']':
                    nf=nf+';'
                else:
                    nf=nf+linea1[i]
                i+=1
            linea1=nf
            linea1=linea1.rstrip(']')
            linea1=linea1.split(';')
            linea1_prim=linea1[0:4]
            linea1_seg=linea1[5:9]
            linea1_ter=linea1[10:14]
            linea1_cuar=linea1[15:19]
            linea1=linea1_prim + linea1_seg + linea1_ter + linea1_cuar
        
            key1_linea1=linea1[0]
            key2_linea1=linea1[4]
            key3_linea1=linea1[8]
            key4_linea1=linea1[12]
        
            d1_linea1=linea1[1:4]
            d2_linea1=linea1[5:8]
            d3_linea1=linea1[9:12]
            d4_linea1=linea1[13:]
        
            amb1[key1_linea1]=d1_linea1
            amb2[key2_linea1]=d2_linea1
            amb3[key3_linea1]=d3_linea1
            amb4[key4_linea1]=d4_linea1
            ambiente={**amb1, **amb2, **amb3, **amb4}
           
    return (usuarios,new_estaciones,datos_estaciones,estaciones,ambiente)  
    
    datos.close()
        
        
def escribir():
    global new_estaciones
    (usuarios,new_estaciones,_,estaciones,ambiente)=Base_de_datos()
    datos=open('registros(1).txt','w')
    for t in usuarios:
        usuario='<'+t +';'
        usuario+=str(usuarios[t][0])+';'
        usuario+=str(usuarios[t][1])+';'
        usuario+=str(usuarios[t][2]+'>')+'\n'
        datos.write(usuario)
    datos.write('\n')
    
    new_est=''   
    new_est+=new_estaciones[0]+','
    new_est+=new_estaciones[1]+','
    new_est+=new_estaciones[2]+','
    new_est+=new_estaciones[3]+','
    new_est+=new_estaciones[4]+','
    new_est+=new_estaciones[5]+','
    new_est+=new_estaciones[6]+','
    new_est+=new_estaciones[7]+','
    new_est+=new_estaciones[8]+','
    new_est+=new_estaciones[9]       
    datos.write(new_est+'\n')
    datos.write('\n')
    
    for d in estaciones:
        estacion=d+','
        estacion+=estaciones[d][0]+','
        estacion+=estaciones[d][1]+'\n'
        datos.write(estacion)
    datos.write('\n')
    
    for a in ambiente:
        amb=a+'['
        amb+=str(ambiente[a][0])+':'
        amb+=str(ambiente[a][1])+','
        amb+=str(ambiente[a][2])+'];'
        datos.write(amb)
    datos.write('\n')
    datos.write('\n')
    
    for b in datos_estaciones:
        datos_est=b+';'
        datos_est+=datos_estaciones[b][0]+';{'
        datos_est+=datos_estaciones[b][1]+','
        datos_est+=datos_estaciones[b][2]+','
        datos_est+=datos_estaciones[b][3]+','
        datos_est+=datos_estaciones[b][4]+'}\n'
        datos.write(datos_est)
    
    datos.close()
datos_estaciones={}
monitoreo={}
print('Ingrese el número de la estación a la que desea agregar datos')
est=input()     
pm10=input('Ingrese los datos de PM10: ')
pm25=input('Ingrese los datos de PM25: ')
temp=input('Ingrese los datos de temperatura: ')
hum=input('Ingrese los datos de humedad: ')

import time
hora=time.strftime("%H:%M:%S")
fecha=time.strftime("%Y-%m-%d")
fecha_hora=fecha+' '+hora
(_,_,datos_estaciones,estaciones,_)=Base_de_datos()
for key in estaciones.keys():
            if key==est:
                n=estaciones[key]
                print('Se le agregarán los datos a la siguiente estación')
                print(n)
                print('------------------OSO---------------------------------')
                break
            
if int(pm10)<=100 and int(pm10)>=0:
    if int(pm25)>=0 and int(pm25)<=200:
        if int(temp)>=-20 and int(temp)<=50:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,pm10,pm25,temp,hum]
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,pm10,pm25,temp,'-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
        else:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,pm10,pm25,'-999',hum]   
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,pm10,pm25,'-999','-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
    else:
        if int(temp)>=-20 and int(temp)<=50:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,pm10,'-999',temp,hum]
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,pm10,'-999',temp,'-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
        else:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,pm10,'-999','-999',hum]  
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,pm10,'-999','-999','-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
else:
    if int(pm25)>=0 and int(pm25)<=200:
        if int(temp)>=-20 and int(temp)<=50:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,'-999',pm25,temp,hum]
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,'-999',pm25,temp,'-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
        else:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,'-999',pm25,'-999',hum]   
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,'-999',pm25,'-999','-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
    else:
        if int(temp)>=-20 and int(temp)<=50:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,'-999','-999',temp,hum]
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,'-999','-999',temp,'-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
        else:
            if int(hum)>=0 and int(hum)<=100:
                monitoreo[fecha_hora]=[key,'-999','-999','-999',hum]   
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            else:
                monitoreo[fecha_hora]=[key,'-999','-999','-999','-999']
                datos_estaciones={**datos_estaciones, **monitoreo}
                escribir()
            
   



