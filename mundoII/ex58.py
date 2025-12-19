# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 23:51:57 2025

@author: Vanilson Manuel
"""

"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
computador = randint(0,10) 
print('*****Tenta adivinhar um numero entre 0  e 10****')
acertou =False
palpites =0
while not acertou:
    jogador = int(input('Qual o seu Palpite:'))
    palpites +=1
    if jogador ==computador:
        acertou = True
    else:
        if jogador < computador:
         print('Mais... tente mais uma vez.')
        elif jogador > computador:
         print('Menos... tente mais uma vez.')
         
                
print(' Parabens Acertou com {} Tentativas'.format(palpites))        