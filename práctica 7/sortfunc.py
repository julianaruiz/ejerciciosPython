from random import uniform
from tkinter import *

def loadFromFile(name):
    ''' 
        Recibe el nombre de un archivo (str)
        Retorna una lista de floats con cada uno 
        de los números extraídos del archivo name
    '''
    
    lista = []
    try:
        with open(name, "r") as file:
            for recorrer in file:
                lista.append(float(recorrer.strip("\n")))
            
        return lista
    except:
        men= 'Archivo de texto no valido, verifique que sean solo números con salto de línea'
        m = Tk()
        m.wm_title("Error")
        label = Label(m, text=men, font=("Helvetica",12))
        label.pack(side="top", fill="x", pady=10)
        exit_button = ttk.Button(m, text="Aceptar", command=m.destroy)
        exit_button.pack()
        m.mainloop()
        return 
    
    pass

def sortBurbuja(L,orde=0):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de burbuja
        para ordenar la lista L
    '''
    i=0
    for s in range(len(L)):
        for t in range(len(L)-1):
            i+=1
            if orde==1:
                if L[t]<L[t+1]:
                    L[t],L[t+1]=L[t+1],L[t]
            else:
               if L[t]>L[t+1]:
                    L[t],L[t+1]=L[t+1],L[t] 
                
    return i
    
    #complejidad computacional: O(sortBurbuja(L,orde=0))=(len(L))^2
    pass

def sortSeleccion(L,orde=0):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de selección
        para ordenar la lista L
    '''
    i=0
    for s in range(len(L)-1):
        for t in range(s+1,len(L)):
            i+=1
            if orde==1:
                if L[t]>L[s]:
                    L[t],L[s]=L[s],L[t]
            else:
                if L[t]<L[s]:
                    L[t],L[s]=L[s],L[t]
    return i
    
    #complejidad computacional: O(sortSeleccion(L,orde=0))=len(L)
    pass

def createRandomList(size, minimo, maximo):
    '''
    Retorna un lista de size números aleatorios. Cada elemento de la lista debe 
    estar en el rango [minimo, maximo]
    
    Parámetros
        n: cantidad de elementos a poner en la lista
        minimo: número mínimo que puede haber en la lista
        maximo: número máximo que puede haber en la lista
    '''
    lista = []
    for i in range(size):
        n = uniform(minimo, maximo)
        lista.append(n)
    
    return lista
    
    pass
