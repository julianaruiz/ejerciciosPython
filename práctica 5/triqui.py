#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 02:49:40 2020

@author: drai06
"""

import random

def printIntro(intro):
    intro= open(intro)
    print(intro.read())
    intro.close()

    # Desarrolle el cuerpo de la función aquí...


    pass

def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    pass

def inputPlayerLetter():
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".
    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    
   
    let=''
    while not (let == 'X' or let == 'O'):
        let=input('Escoja X o O: ')
        let=let.upper()
    if let=='X':
      
        return ['X','O']
    else:
       
        return ['O','X']
    
    pass

def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...
    
    if random.randint(0,1)==0:
        return 'Usuario'
    else:
        return 'Computador'
    pass

def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...
    board[move] = letter
    
    
    pass

def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    return ((board[1]==letter and board[2]==letter and board[3]==letter) or #horizontal inferior
            (board[4]==letter and board[5]==letter and board[6]==letter) or #horizontal intermedia
            (board[7]==letter and board[8]==letter and board[9]==letter) or #horizontal superior
            (board[1]==letter and board[5]==letter and board[9]==letter) or #diagonal ascendente
            (board[3]==letter and board[5]==letter and board[7]==letter) or #diagonal decresente
            (board[1]==letter and board[4]==letter and board[7]==letter) or #vertical izquierda
            (board[2]==letter and board[5]==letter and board[8]==letter) or #vertical intermedia
            (board[3]==letter and board[6]==letter and board[9]==letter)) #vertical derecha
    pass

def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    return board[move] in '123456789'
    
    pass

def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    # Desarrolle el cuerpo de la función aquí...
    
    move=input('Ingrese número del 1 al 9: ')
    if move in '123456789'  :
        return int(move)
    else:
        move=input('Ingrese número del 1 al 9: ')
    pass

def chooseRandomMoveFromList(board, movesList):
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    movimiento = []
    for i in movesList:
        if isSpaceFree(board, i):
            movimiento.append(i)
 
    if len(movimiento) != 0:
        return random.choice(movimiento)
    else:
        return None
    pass

def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    # 1. Verificar si la computadora puede ganar...

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...

    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...

    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...
    
    if computerLetter == 'X':
        usulet = 'O'
    else:
        usulet = 'X'
    newboard = []
 
    for i in board:
        newboard.append(i)
 
    for i in range(0, 10):
        
        if isSpaceFree(newboard, i):
            makeMove(newboard, computerLetter, i)
            if isWinner(newboard, computerLetter):
                return i
 
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
   

def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
    pass
