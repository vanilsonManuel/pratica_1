# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 23:30:59 2025

@author: pt
"""

"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
 mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
 

n = cont = soma = 0
n =int(input('Informa o numero:'))
while n != 999:
    soma+=n
    cont +=1
    n =int(input('Informa o numero:'))
print('Voce dgitou {} e soma é {}'.format(cont,soma))
    