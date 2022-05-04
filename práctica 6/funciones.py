# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:10:05 2020

@author: JULI


"""

import sys

def pantalla_inicio():
    # Mostrar en pantalla 'MENÚ PRINCIPAL'.
    # Mostrar en pantalla las opciones(usuario visitante, usuario registrado o salir del sistema).
    # Depende de lo que seleccione el usuario poner condicionales para ir donde quiere.
    print('MENÚ PRINCIPAL')
    print('Usuario visitante')
    print('Usuario registrado')
    print('Salir del menú')
    us=input('Escriba la acción que quiera realizar(visitante, ingresar o salir): ')
    us=us.lower()
    otro=True
    while otro:
        while not(us=='visitante' or us=='ingresar' or us=='salir'):
            us=input('Escriba la acción que quiera realizar(visitante, ingresar o salir): ')
            us=us.lower()
        if us=='visitante':
            Visitante()
        elif us=='ingresar':
            usuario_registrado()
        elif us=='salir':
            sys.exit()
            
    pass

def Base_de_datos():
    # Almacenar en listas la información, edición, eliminación y creación de los usuarios registtrados, 
    # las estaciones existentes en el sistema, las variables monitoreadas, los municipios y el registro 
    # de medidas.
    global new_estaciones
    datos=open('registros.txt')
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
            usuarios[key]=[d[0], d[1], d[2]]
            
        
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
           
    return [usuarios,new_estaciones,datos_estaciones,estaciones,ambiente]
    
    datos.close()
     
 
    pass

def usuario_registrado():
    # Mostrar en pantalla 'USUARIO REGISTRADO'
    # Ingresar el documento del usuario.
    # Ingresar la clave del usuario.
    # Validar si el documento y la clave coinciden, si no es así pedirle que lo haga de nuevo.
    print('PANTALLA PRINCIPAL')
    otro=True
    while otro:
        print('Ingrese el usuario, el programa diferencia entre mayúsculas y minúsculas')
        usuario=input()
        print('Ingrese la contraseña')
        clave=input()

        while not (usuario.isalpha and clave.isdigit):
            print('Ingrese un nombre válido')
            usuario=input()
            print('Ingrese una contraseña válida')
            clave=input()
        (usuarios,new_estaciones,datos_estaciones,estaciones,ambiente)=Base_de_datos()
        for i in usuarios:
            if usuario==usuarios[i][0]:
                break
        while not (usuario==usuarios[i][0] and clave==usuarios[i][1]):
            print('Ingrese un usuario registrado, el programa diferencia entre mayúsculas y minúsculas')
            usuario=input()
            print('Ingrese la contraseña')
            clave=input()
        for value1 in usuarios:
            n=usuarios[value1]
            if n[0]==usuario:
                m=list(usuarios.keys())[list(usuarios.values()).index(n)]
                break
        w=list(usuarios.keys())[list(usuarios.values()).index(n)]
                
        if m==w:
            if n[2]=='Administrador' or n[2]=='administrador' or n[2]=='ADMINISTRADOR':
                otro=False
                Administrador()
     
            elif n[2]=='Operador' or n[2]=='operador' or n[2]=='ADMINISTRADOR':
                otro=False
                Operador()
      
        else:
            otro=True

    pass

def Operador():
    # Ingresar municipio
    # Comprobar si está el municipio ingresado.
    # Ingresar la estación
    # Combrobar si la estación está en el sistema.
    (_,new_estaciones,_,_,_)=Base_de_datos()
    print('MENÚ OPERADOR')
    print('Ingrese un municipio')
    mun=input()
    while not mun in new_estaciones:
        print('Municipio no encontrado, por favor ingrese otro')
        mun=input()
    validar_medidas()
    
    pass

def Administrador():
    # Seleccionar si se va a gestionar un usuario o una estación.
    print('MENÚ ADMINISTRADOR')
    print('GESTIONAR ESTACIONES')
    print('GESTIONAR USUARIOS')
    print('VOLVER AL MENU PRINCIPAL')
    print('Ingrese una de las opciones')
    opcion=input()
    opcion=opcion.lower()
    while not(opcion=='gestionar estaciones' or opcion=='gestionar usuarios' or opcion=='volver al menu principal'):
         print('Ingrese una de las opciones')
         opcion=input()
         opcion=opcion.lower()   
    if opcion=='gestionar estaciones':
        gestionar_estaciones()
    elif opcion=='gestionar usuarios':
        gestionar_usuarios()
    else:
        pantalla_inicio()
    pass

def Visitante():
    # Elegir periodo de tiempo a evaluar
    # Elegir las variables (PM10, PM25, Temperatura y Humedad). 
    # Elegir los municipios
    # Las estadísticas que se mostrarán serán el valor máximo, mínimo y promedio de las medidas
    # tomadas en las estaciones de los municipios seleccionados y en el lapso de tiempo seleccionado.
    # Preguntar si quiere salir del menú.
    import datetime  
    (_,_,datos_estaciones,estaciones,ambiente)=Base_de_datos()
    print('MENÚ VISITANTE')
    otro_def=True
    while otro_def:
        for d in estaciones:
            estacion=d+' '
            estacion+=estaciones[d][0]+','
            estacion+=estaciones[d][1]+'\n'
            print(estacion)
        est=input('Ingrese los números de las estaciones que desea visualizar separados por comas: ')
        est=est.split(',')
        fecha=input('Ultimos 7 días, últimos 30 días o escoger fechas manualmente(ingrese 7, 30 o escoger): ')
        fecha=fecha.lower()
        while not (fecha=='7' or fecha=='30' or fecha=='escoger'):
            fecha=input('Ultimos 7 días, últimos 30 días o escoger fechas manualmente(ingrese 7, 30 o escoger): ')
            fecha=fecha.lower()
        for a in ambiente:
            print(a)
        para=input('Ingrese los parámetros que desea visualizar separados por comas: ')
        para=para.lower()
        para=para.split(',')
        otro=True
        while otro:
            for i in est:
                while not i in est:
                    est=input('Alguna de las estaciones es inválida, ingrese los números de las estaciones que desea visualizar separados por comas: ')
                    est=est.split(',')
                
                for key in estaciones.keys():
                    if key==i: 
                        n=estaciones[key][0]+','
                        n+=estaciones[key][1]

                        for datos in datos_estaciones:
                            if datos_estaciones[datos][0]==key:
                                if fecha=='7':
                                    hoy=datetime.datetime.utcnow()
                                    com=(hoy - datetime.timedelta(days=7))
                                    comp=str(com)
                                    comp=comp[0:19]
                                    ho=str(hoy)
                                    ho=ho[0:19]
                                    if datos<=ho and datos>=comp:
                                        print(n)
                                        print(datos) 

                                        for b in para:
                                            while not (b=='pm10' or b=='pm25' or b=='temperatura'):
                                                if b=='humedad':
                                                    hum=datos_estaciones[datos][4]+'%'
                                                    print('humedad: ',hum)
                                                    break
                                                else:
                                                    para=input('Ingrese los parámetros que desea visualizar separados por comas: ')
                                                    para=para.lower()
                                                    para=para.split(',')   
                                            if b=='pm10':
                                                pm10=datos_estaciones[datos][1]+'ug/m3'
                                                print('PM10: ',pm10)
                                            elif b=='pm25':
                                                pm25=datos_estaciones[datos][2]+'ug/m3'
                                                print('PM25: ',pm25)
                                            elif b=='temperatura':
                                                temp=datos_estaciones[datos][3]+'°C'
                                                print('temperatura: ',temp) 
                                        print('-----------------------------OSO---------------------------')
                                elif fecha=='30':
                                    hoy=datetime.datetime.utcnow()
                                    comp=hoy - datetime.timedelta(days=30)
                                    comp=str(comp)
                                    hoy=str(hoy)
                            
                                    if datos<=hoy[0:19] and datos>=comp[0:19]:
                                        print(n)
                                        print(datos)
                                        for b in para:
                                            while not (b=='pm10' or b=='pm25' or b=='temperatura'):
                                                if b=='humedad':
                                                    hum=datos_estaciones[datos][4]+'%'
                                                    print('humedad: ',hum)
                                                    break
                                                else:
                                                    para=input('Ingrese los parámetros que desea visualizar separados por comas: ')
                                                    para=para.lower()
                                                    para=para.split(',')   
                                            if b=='pm10':
                                                pm10=datos_estaciones[datos][1]+'ug/m3'
                                                print('PM10: ',pm10)
                                            elif b=='pm25':
                                                pm25=datos_estaciones[datos][2]+'ug/m3'
                                                print('PM25: ',pm25)
                                            elif b=='temperatura':
                                                temp=datos_estaciones[datos][3]+'°C'
                                                print('temperatura: ',temp) 
                                        print('-----------------------------OSO---------------------------')
            otro=False
        
        lista=[]
        otro1=True
        if fecha=='escoger':
            while otro1:                                    
                for e in est:
                    for recorrer in estaciones.keys():
                        if recorrer==e: 
                            s=estaciones[recorrer][0]+','
                            s+=estaciones[recorrer][1]

                            for dats in datos_estaciones:
                                if datos_estaciones[dats][0]==recorrer:
                                    print(s)
                                    print(dats)
                                    lista.append(dats)                 
                otro1=False

            print('Ingrese una de las fechas que se muestran')
            escoger_fecha=input()
            while not escoger_fecha in lista:
                print('Ingrese una de las fechas que se muestran')
                escoger_fecha=input()
            otro1=True
            while otro1:                                    
                for w in est:
                    for t in estaciones.keys():
                        if recorrer==w: 
                            p=estaciones[t][0]+','
                            p+=estaciones[t][1]

                            for dat in datos_estaciones:
                                if datos_estaciones[dat][0]==t:
                                    if str(dat)==escoger_fecha:
                                        print(p)
                                        print(dat)
                                        for b in para:
                                            while not (b=='pm10' or b=='pm25' or b=='temperatura'):
                                                if b=='humedad':
                                                    hum=datos_estaciones[datos][4]+'%'
                                                    print('humedad: ',hum)
                                                    break
                                                else:
                                                    para=input('Ingrese los parámetros que desea visualizar separados por comas: ')
                                                    para=para.lower()
                                                    para=para.split(',')   
                                            if b=='pm10':
                                                pm10=datos_estaciones[datos][1]+'ug/m3'
                                                print('PM10: ',pm10)
                                            elif b=='pm25':
                                                pm25=datos_estaciones[datos][2]+'ug/m3'
                                                print('PM25: ',pm25)
                                            elif b=='temperatura':
                                                temp=datos_estaciones[datos][3]+'°C'
                                                print('temperatura: ',temp) 
                                             
                otro1=False
                
        print('Se devolverá a la pantalla principal'+'\n')
        
        pantalla_inicio()
        
    pass

def gestionar_usuarios():
    # Seleccionar si desea editar, crear o eliminar la gestión elegida.
    # Si escoge crear, se creará una gestión nueva si cumple con los requerimientos.
    # Si escoge eliminar, se le pedirá el documento o código a eliminar. Confirmar que se desea eliminar
    #el usuario. No puede eliminarse el usuario actual del sistema.
    # Preguntar si quiere modificar alguna otra cosa, de no ser así regresarlo al menú anterior.
    print('GESTIÓN DE USUARIOS')
    print('EDITAR')
    print('ELIMINAR')
    print('CREAR')
    print('SALIR')
    global new_estaciones
    otro=True
    while otro:          
        opcion=input('Ingrese una de las opciones: ')
        opcion=opcion.lower()
        while not (opcion=='editar' or opcion=='eliminar' or opcion=='crear'):
            if opcion=='salir':
                print('¿Desea salir del menú?')
                resp=input().lower()
                if resp=='no':
                    otro=True
                else:
                    otro=False
                    Administrador()        
            opcion=input('Ingrese una de las opciones')
            opcion=opcion.lower()
        if opcion=='editar':
            Editar_usuario()
        elif opcion=='eliminar':
            Eliminar_usuario()
        elif opcion=='crear':
            Crear_usuario()
        
    pass

def gestionar_estaciones():
    # Seleccionar si desea editar, crear o eliminar la gestión elegida.
    # Si escoge crear, se creará una gestión nueva si cumple con los requerimientos.
    # Si escoge eliminar, se le pedirá el documento o código a eliminar. Confirmar que se desea eliminar
    #el usuario. No puede eliminarse el usuario actual del sistema.
    # Preguntar si quiere modificar alguna otra cosa, de no ser así regresarlo al menú anterior.
    print('GESTIÓN DE ESTACIONES')
    print('EDITAR')
    print('ELIMINAR')
    print('CREAR')
    print('SALIR')
    global new_estaciones
    otro=True
    while otro:          
        opcion=input('Ingrese una de las opciones: ')
        opcion=opcion.lower()
        while not (opcion=='editar' or opcion=='eliminar' or opcion=='crear'):
            if opcion=='salir':
                print('¿Desea salir del menú?')
                resp=input().lower()
                if resp=='no':
                    otro=True
                else:
                    otro=False
                    Administrador() 
            opcion=input('Ingrese una de las opciones')
            opcion=opcion.lower()
        if opcion=='editar':
            Editar_estacion()
        elif opcion=='eliminar':
            Eliminar_estacion()
        elif opcion=='crear':
            Crear_estacion()
        print('¿Desea hacer algo más?')
        resp=input().lower()
        while not resp=='si' or resp=='no':
            print('¿Desea salir del menú?')
            resp=input().lower()
        if resp=='si':
            otro=True
        else:
            Administrador()
    pass

def escribir_usuarios():
    #Escribe los cambios hechos en las gestiones de usuarios.
    global new_estaciones
    (_,new_estaciones,datos_estaciones,estaciones,ambiente)=Base_de_datos()
    datos=open('registros.txt','w')
    for t in usuarios:
        usuario='<'+t +';'
        usuario+=str(usuarios[t][0])+';'
        usuario+=str(usuarios[t][1])+';'
        usuario+=str(usuarios[t][2]+'>')+'\n'
        datos.write(usuario)
    datos.write('\n')
    new_est=''   
    
    new_est+=':'+new_estaciones[0]+','
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
    
    pass

def escribir_estaciones():
    #Escribe los cambios hechos en las gestiones de estaciones.
    global new_estaciones
    (usuarios,new_estaciones,datos_estaciones,_,ambiente)=Base_de_datos()
    datos=open('registros.txt','w')
    for t in usuarios:
        usuario='<'+t +';'
        usuario+=str(usuarios[t][0])+';'
        usuario+=str(usuarios[t][1])+';'
        usuario+=str(usuarios[t][2]+'>')+'\n'
        datos.write(usuario)
    datos.write('\n')
    new_est=''   
    
    new_est+=':'+new_estaciones[0]+','
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
    
    pass

def Editar_estacion():
    #Edita una estación mediante su número, estos aparecerán en pantalla con su 
    #respectivo nombre 

    global new_estaciones
    global estaciones
    (_,_,_,estaciones,_)=Base_de_datos()
    otro=True
    while otro:
        for d in estaciones:
            print('Estación:')
            estacion=d+' '
            estacion+=estaciones[d][0]+','
            estacion+=estaciones[d][1]+'\n'
            print(estacion)
        print('Ingrese el número de la estación a editar')
        edit=input()
    
        while not edit.isnumeric and edit in estaciones.keys():
            print('Ingrese el número de la estación a editar válido')
            edit=input()  
        
        for key in estaciones.keys():
            if key==edit:
                n=estaciones[key][0]+','
                n+=estaciones[key][1]
                print(n)
                print('¿Qué dato deseea modificar?(lugar, municipio o todo)')
                dat=input()
                dat=dat.lower()
            
                while not (dat=='lugar' or dat=='municipio'):
                
                    if dat=='todo':
                        lugar=(input('Ingrese un lugar nuevo: '))
                        estaciones[edit][0]=lugar
                        municipio=(input('Ingrese un nuevo municipio: '))
                        estaciones[edit][1]=municipio
                        escribir_estaciones()
                        break
                
                    else:
                        print('¿Qué dato deseea midificar?(lugar, municipio o todo)')
                        dat=input()
                        dat=dat.lower()
                    
                if dat=='lugar':
                    lugar=(input('Ingrese un lugar nuevo: '))
                    estaciones[edit][0]=lugar
                    escribir_estaciones()
            
                elif dat=='municipio':
                    municipio=(input('Ingrese un nuevo muncipio: '))
                    estaciones[edit][1]=municipio
                    escribir_estaciones()
            
            
        otro=(input('¿Desea modificar otra estación? '))  
        otro=otro.lower()
        while not (otro=='si' or otro=='no'):
            otro=(input('¿Desea modificar otra estación? '))  
            otro=otro.lower()
        if otro=='si':
            otro=True
        else:
            gestionar_estaciones()
    pass

def Eliminar_estacion():
    #elimina una estación mediante su número, este aparece en pantalla con su respectivo nombre.
    global new_estaciones
    global estaciones
    (_,_,_,estaciones,_)=Base_de_datos()
    otro=True
    while otro:
        for d in estaciones:
            print('Estación:')
            estacion=d+' '
            estacion+=estaciones[d][0]+','
            estacion+=estaciones[d][1]+'\n'
            print(estacion)
        print('Ingrese el número de la estación')
        eliminar=input()
        while not eliminar in estaciones.keys():
            print('Número inválido, por favor ingrese otro')
            eliminar=input()
        for key in estaciones.keys():
            if key==eliminar:
                n=estaciones[key][0]+','
                n+=estaciones[key][1]
        print('¿Realmente quiere borrar esta estación?', n)
        res=input()
        if res=='si':
            estaciones.pop(eliminar)
            escribir_estaciones()
    
        otro=(input('¿Desea eliminar otra estación? '))  
        otro=otro.lower()
        while not (otro=='si' or otro=='no'):
            otro=(input('¿Desea modificar otra estación? '))  
            otro=otro.lower()
        if otro=='si':
            otro=True
        else:
            gestionar_estaciones()
    pass

def Crear_estacion():
    #Crea una estación con número, lugar y municipio
    global new_estaciones
    global estaciones
    (_,_,_,estaciones,_)=Base_de_datos()
    otro=True
    while otro:
        estacion={}
        print('Ingrese el número de la estación')
        numero=input()
        lugar=(input('Ingrese el lugar: '))
        municipio=(input('Ingrese el municipio: '))
        estaciones[numero]=[lugar,municipio]
        estaciones={**estaciones, **estacion}
        escribir_estaciones()
        otro=(input('¿Desea agregar otra estación? '))  
        otro=otro.lower()
        while not (otro=='si' or otro=='no'):
            otro=(input('¿Desea modificar otra estación? '))  
            otro=otro.lower()
        if otro=='si':
            otro=True
        else:
            gestionar_estaciones()
    pass
   
def Editar_usuario():
    #aparecerá la información de gestión indicada y preguntará que se quiere editar.
    global new_estaciones
    global usuarios
    (usuarios,_,_,_,_)=Base_de_datos()
    otro=True
    while otro:
        print('Ingrese el documento del usuario a editar')
        edit=input()
    
        while not edit.isnumeric and edit in usuarios.keys():
            print('Ingrese el documento del usuario válido a editar')
            edit=input()  
        
        for key in usuarios.keys():
            if key==edit:
                for n in usuarios:
                    if n==edit:
                        usuario='Documento: '+n
                        usuario+='Nombre: '+str(usuarios[n][0])+', Clave: '
                        usuario+=str(usuarios[n][1])+'Cargo: '
                        usuario+=str(usuarios[n][2])  
                        print(usuario)
                print('¿Qué dato deseea midificar?(Nombre, clave, cargo o las tres)')
                dat=input()
                dat=dat.lower()
            
                while not (dat=='nombre' or dat=='clave' or dat=='cargo'):
                
                    if dat=='las tres':
                        nombre=(input('Ingrese un nombre nuevo: '))
                        usuarios[edit][0]=nombre
                        clave=(input('Ingrese una nueva clave: '))
                        usuarios[edit][1]=clave
                        cargo=(input('Ingrese el nuevo cargo: '))
                        usuarios[edit][2]=cargo
                        escribir_usuarios()
                        break
                
                    else:
                        print('¿Qué dato deseea midificar?(Nombre, clave, cargo o las tres)')
                        dat=input()
                        dat=dat.lower()
                    
                if dat=='nombre':
                    nombre=(input('Ingrese un nombre nuevo: '))
                    usuarios[edit][0]=nombre
                    escribir_usuarios()
            
                elif dat=='clave':
                    clave=(input('Ingrese una nueva clave: '))
                    usuarios[edit][1]=clave
                    escribir_usuarios()
            
                elif dat=='cargo':
                    cargo=(input('Ingrese el nuevo cargo: '))
                    usuarios[edit][2]=cargo
                    escribir_usuarios()
            
                otro=(input('¿Desea modificar otro usuario? '))  
                otro=otro.lower()
                while not (otro=='si' or otro=='no'):
                    otro=(input('¿Desea modificar otro usuario? '))  
                    otro=otro.lower()
                if otro=='si':
                    otro=True
                else:
                    gestionar_usuarios()
    pass

def Eliminar_usuario():
    #Eliminará un usuario mediante su documento, se mostrará si se quiere eliminar
    #y aparecerán todos los datos.
    global new_estaciones
    global usuarios
    (usuarios,_,_,_,_)=Base_de_datos()
    otro=True
    while otro:
        print('Ingrese el documento')
        documento=input()
        while not documento in usuarios.keys():
            print('Documento inválido, por favor ingrese otro')
            documento=input()
        
        for n in usuarios:
            if n==documento:
                usuario='Nombre: '+str(usuarios[n][0])+', Clave: '
                usuario+=str(usuarios[n][1])+'Cargo: '
                usuario+=str(usuarios[n][2])    
        print('¿Realmente quiere borrar este usuario?', usuario)
        s=input
        if s=='si':
            usuarios.pop(documento)
            escribir_usuarios()
            
        otro=(input('¿Desea eliminar otro usuario? '))  
        otro=otro.lower()
        while not (otro=='si' or otro=='no'):
            otro=(input('¿Desea modificar otro usuario? '))  
            otro=otro.lower()
        if otro=='si':
            otro=True
        else:
            gestionar_usuarios()
    pass

def Crear_usuario():
    #Crea un usuario.
    global new_estaciones
    global usuarios
    (usuarios,_,_,_,_)=Base_de_datos()
    otro=True
    while otro:
        usuario={}
        print('Ingrese el documento')
        documento=input()
        tam=len(documento)
        while not (documento in usuarios.keys() and tam==10 and documento.isnumeric):
            print('Ingrese otro documento, el documento debe tener 10 números')
            documento=input()
        nombre=(input('Ingrese el nombre: '))
        while not nombre.isalpha:
            nombre=(input('Ingrese un nombre válido, sin números: '))
        clave=(input('Ingrese la clave: '))
        ta_cla=tam(clave)
        while ta_cla<4:
            clave=input('Ingrese una clave de mínimo 4 caracteres: ')
        confi_clave=input('Confirme la clave: ')
        while not clave==confi_clave:
            confi_clave=input('contraseñas no coinciden, volver a ingresar: ')
        cargo=(input('Ingrese el cargo: '))
        usuario[documento]=[nombre,clave,cargo]
        usuarios={**usuarios, **usuario}
        escribir_usuarios()
        otro=(input('¿Desea agregar otro usuario? '))  
        otro=otro.lower()
        while not (otro=='si' or otro=='no'):
            otro=(input('¿Desea modificar otro usuario? '))  
            otro=otro.lower()
        if otro=='si':
            otro=True
        else:
            gestionar_usuarios()
    
    pass


def escribir_datos_estaciones():
    #Escribe las modificaciones de las estaciones e el archivo txt.
    global new_estaciones
    (usuarios,new_estaciones,_,estaciones,ambiente)=Base_de_datos()
    datos=open('registros.txt','w')
    for t in usuarios:
        usuario='<'+t +';'
        usuario+=str(usuarios[t][0])+';'
        usuario+=str(usuarios[t][1])+';'
        usuario+=str(usuarios[t][2]+'>')+'\n'
        datos.write(usuario)
    datos.write('\n')
    new_est=''   
    
    new_est+=':'+new_estaciones[0]+','
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
    
    pass


def validar_medidas(): 
    # Ingresar los datos.
    # Listar medidas.
    # Preguntar si va a ingresar más datos o quiere volver al menú anterior.
    # Preguntar si qquiere ingresar otro municipio.
    global datos_estaciones
    (_,_,datos_estaciones,estaciones,_)=Base_de_datos()
    datos_estaciones={}
    monitoreo={}
    otro=True
    while otro:
        for d in estaciones:
            print('Estación:')
            estacion=d+' '
            estacion+=estaciones[d][0]+','
            estacion+=estaciones[d][1]+'\n'
            print(estacion)
        print('Ingrese el número de la estación a la que desea agregar datos')
        est=input() 
        while not est in estaciones.keys():
            print('Estación no encontrada, por favor ingrese otra')
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
                break
            
        if int(pm10)<=100 and int(pm10)>=0:
            if int(pm25)>=0 and int(pm25)<=200:
                if int(temp)>=-20 and int(temp)<=50:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,pm10,pm25,temp,hum]
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    
            
                    else:
                        monitoreo[fecha_hora]=[key,pm10,pm25,temp,'-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                else:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,pm10,pm25,'-999',hum]   
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,pm10,pm25,'-999','-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
            else:
                if int(temp)>=-20 and int(temp)<=50:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,pm10,'-999',temp,hum]
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,pm10,'-999',temp,'-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                else:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,pm10,'-999','-999',hum]  
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,pm10,'-999','-999','-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
        else:
            if int(pm25)>=0 and int(pm25)<=200:
                if int(temp)>=-20 and int(temp)<=50:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,'-999',pm25,temp,hum]
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,'-999',pm25,temp,'-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                else:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,'-999',pm25,'-999',hum]   
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,'-999',pm25,'-999','-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
            else:
                if int(temp)>=-20 and int(temp)<=50:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,'-999','-999',temp,hum]
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,'-999','-999',temp,'-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                else:
                    if int(hum)>=0 and int(hum)<=100:
                        monitoreo[fecha_hora]=[key,'-999','-999','-999',hum]   
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                    else:
                        monitoreo[fecha_hora]=[key,'-999','-999','-999','-999']
                        datos_estaciones={**datos_estaciones, **monitoreo}
                        escribir_datos_estaciones()
                
        print('¿Desea agregar más datos, ir a otro municipio o ver la información?(agregar, municipio, ver o no)')
        res=input()
        res=res.lower()
        while not res=='agregar' or res=='municipio' or res=='no':
            if res=='ver':
                ex=input('Ingrese número de estación a examinar: ')
                while not ex in estaciones.keys():
                    ex=input('Ingrese número de estación a examinar: ')
                    
                for d in estaciones:
                    if d==ex:
                        print('Estación:')
                        estacion=d+' '
                        estacion+=estaciones[d][0]+','
                        estacion+=estaciones[d][1]+'\n'
                        print(estacion)
                        
                for b in datos_estaciones:
                    if datos_estaciones[b][0]==ex:    
                        datos_est=b+' (PM10: '
                        datos_est+=datos_estaciones[b][1]+', PM25: '
                        datos_est+=datos_estaciones[b][2]+', Temperatura: '
                        datos_est+=datos_estaciones[b][3]+', Humedad: '
                        datos_est+=datos_estaciones[b][4]+')\n'
                        print(datos_est)      
            print('¿Desea agregar más datos o ir a otro municipio?(agregar, municipio, ver o no)')
            res=input()
            res=res.lower()
        if res=='agregar':
            otro=True
        elif res=='municipio':
            otro=False
            Operador()
        elif res=='no':
            otro=False
            pantalla_inicio()
    
    
    pass
