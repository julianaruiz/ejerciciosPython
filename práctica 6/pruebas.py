

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
      
"""
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
"""      
d = {"a": ['1','5'],"b": '2',"c": '3',"d": '4'}
for r in d:
    n=(d[r])
    for puto in n:
        if puto=='4':
            print(r[0])
    #print(n)   
    #print(r[0])
"""    
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
        print('-----------------------------OSO-----------------------------')
    #usuarios,new_estaciones,datos_estaciones,estaciones,ambiente=Base_de_datos()

    for value1 in usuarios:
        n=usuarios[value1]
        if n[0]==usuario:
            m=list(usuarios.keys())[list(usuarios.values()).index(n)]
        
            break

    for value2 in usuarios:
        n=usuarios[value2]
        if n[1]==clave:
            w=list(usuarios.keys())[list(usuarios.values()).index(n)]
       
            break
    if m==w:

        if n[2]=='Administrador' or n[2]=='administrador' or n[2]=='ADMINISTRADOR':
            otro=False
            Administrador()
            
                
        elif n[2]=='Operador' or n[2]=='operador' or n[2]=='ADMINISTRADOR':
            otro=False
            Operador()
            
               
    else:
        otro=True
    #print('------------------OSO-------------------')
    #m=list(usuarios.keys())[list(usuarios.values()).index(n)]
    #print(m)
            

    
    
        