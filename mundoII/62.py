# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 00:20:12 2025

@author: pt
"""

'''Exercício Python 62: Melhore o DESAFIO 61, 
perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''


print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao da PA:'))
termo = primeiro
cont =1
mais =10
total =0
while mais !=0:
    total = total + mais
    while  cont <=total:
        print('{}->'.format(termo), end='')
        termo +=razao
        cont+=1
    mais = int(input('Quanto termos voce quer mostrar mais:'))
print('progressão finalizada com {} termos mostrados.'.format(total))