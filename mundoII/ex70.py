# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 20:24:53 2025

@author: Vanilson Manuel
"""
"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
    
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
    
    
"""

while True:
    print('Registar o produto')
    print('-'*30)
    nome =str(input('Nome do produto:'))
    preco = int(input('Preço do produto:'))
    op = ' '
    while op not in 'SN':
        op =str(input('Deseja continuar Adicionar [ S- N] ')).strip().upper()[0]
        if op not in 'SN':
            print('-'*30)
            print(' Opção Invalida digite')
        print('-'*30)
    if op == 'N':
        print('Saiu ')
        break