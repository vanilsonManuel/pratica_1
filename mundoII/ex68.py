# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:08:21 2025

@author: pt
"""
"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
 
 
from  random import randint
vitoria =0

while True :
    jogador = int(input('Digite um valor:'))
    computador =randint(0, 10)
    total = jogador + computador
    tipo =' '
    while tipo  not in 'PI':
        tipo =str(input('Par ou Impar [P-I]')).strip().upper()[0]
    print(f' voce jogou {jogador} e o computador {computador}. Total é {total}',end='')
    print('DEU PAR' if total % 2 ==0 else ' DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE  VENCEU ')
            vitoria +=1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
         if total % 2 ==1:
             print('Voce venceu ')
             vitoria+=1
         else:
             print('Voce Perdeu')    
             break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCE VENCEU {vitoria} VEZES.')
              
    