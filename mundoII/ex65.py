# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 23:48:20 2025

@author: pt
"""

"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
 
 
valores = []

soma = media =cont = 0
maior = -99999
menor = 99999
resp = 'S'

while  resp in 'Ss':
     n = int(input('Informa o valor:'))
     soma +=n
     cont +=1
     
     if   n > maior:
         maior = n
     if n < menor:
         menor = n
     resp = str(input('Deseja continuar [S-N]')).upper()
 
media = soma / cont
print('A soma e {} e media e {}'.format(soma,media))
print('maior {}'.format(maior))
print('Menor {}'.format(menor))
 