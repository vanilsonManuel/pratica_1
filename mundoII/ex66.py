# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:14:00 2025

@author: pt
"""
"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados e
 qual foi a soma entre elas (desconsiderando o flag)."""
 

cont =n =soma = 0



while True:
    n = int (input('Digite o numero:'))
    if n == 999:
        break
    soma += n
    cont+= 1
    
print(f' Foram digitados {cont} e a soma é de {soma}')
    
