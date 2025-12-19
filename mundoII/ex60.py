# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 13:35:26 2025

@author: pt
"""

# Exercício Python 060: Faça um programa que leia um número 
#qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''from math  import factorial

n = int(input('Informa o numero:'))

f = factorial(n)
print('O Factorial do {} = {}'.format(n,f))'''


'''n = int(input('Digite o numero para calcular:'))

f = 1
print('Calculando {}!='.format(n), end='')

while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c> 1 else  ' = ' ,end='')
    f*=c
    c-=1

print ('{}'.format(f))'''

n = int(input('Informa o numero:'))
f = 1

for c in range (n,0,-1):
    print('{} '.format(c), end='')
    print(' X ' if c> 1 else  ' = ' ,end='')
    f*=c
    
print ('{}'.format(f))    








