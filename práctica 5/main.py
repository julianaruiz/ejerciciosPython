#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 02:11:23 2020

@author: drai06
"""

import triqui 
t='intro.txt'
#triqui.printIntro(t)

turn ="Usuario" # Indica quién tiene el turno para jugar, el usuario o la computadora.
usulet, comlet=triqui.inputPlayerLetter()

while True:
    # 2. Crear el tablero
    board=['0','1','2','3','4','5','6','7','8','9']
    triqui.drawBoard(board)
    # 3. El usuario debe seleccionar la marca
    # 4. Quién va primero el usuario o la computadora?
    #turn=triqui.whoGoesFirst()
    print(turn + ' va primero.')
    jugando = True # El juego ha iniciado

    while jugando:
        
        if turn == 'Usuario': # 5. Turno del usuario
            
            # a. Mostrar tablero
            
            triqui.drawBoard(board)
            # b. Pedir jugada al usuario
            num=triqui.getPlayerMove(board)
            # c. Actualizar el tablero
            triqui.makeMove(board,usulet,num)
            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if triqui.isWinner(board, usulet):
                triqui.drawBoard(board)
                print('¡Has ganado!')
                jugando = False
            
            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            else:
                if triqui.isBoardFull(board):
                    triqui.drawBoard(board)
                    print('Hay un empate')
                    break
               
            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno
                else:
                
                    turn = 'Computadora'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            # b. Actualizar el tablero.
            mov = triqui.getComputerMove(board, comlet)
            print(mov)
            triqui.makeMove(board, comlet, mov)
            
            
            
            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            if triqui.isWinner(board, comlet):
                triqui.drawBoard(board)
                print('El computador ha ganado')
                jugando = False
            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            else:
                if triqui.isBoardFull(board):
                    triqui.drawBoard(board)
                    print('Hay empate')
                    break
            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.
                else:
                    turn = 'Usuario'
            

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa."""
    res=input('¿Jugar otra ves? Responder con si o no: ')
    if res=='no':
        print('¡Gracias por jugar!')
        break   
    else:
        triqui.drawBoard(board)
        print(turn + ' va primero.')
        