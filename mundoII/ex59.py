# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 23:01:21 2025

@author: Vanilson
"""

#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

from time import  sleep

n1 = int(input('Informa o numero:'))
n2 = int(input('Informa o numero:'))
op = 0

while op != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    op =int(input(' Qual a sua opção:'))
    if op ==1 :
        print('\nA soma dos numeros {}+{} ={}\n'.format(n1,n2,n1+n2))
    elif op ==2:
        print('CA Multiplicação dos numeros {}*{}={}\n'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1 > n2:
            print('\nEntre {} e {} o  maior {}\n'.format(n1,n2,n1))
        elif n2 > n1:
            print('\nEntre {} e {} o maior {}\n'.format(n1,n2,n2))
        else:
            print('\nOs numeros são aguais\n')
    elif op == 4:
        n1 = int(input('digite o novo numero:'))
        n2 = int(input('digite o novo numero'))
    elif op== 5:
        print('\nFIM DO PROGRAMA VOLTE SEMPRE')
    else:
        print('\nOpcao invalida Tente Novamente:')
        sleep(1)
        
            
            
    




    