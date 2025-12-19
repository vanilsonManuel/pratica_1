# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:22:49 2025

@author: pt
"""
"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo."""
 
 
n=0
c =1

contador =0

while True:
 n =int(input('informe o numero:'))
 if n <= 0:
  break
 print('-'*30)
 for c in range (1,11):
   print(f'{n}X{c}={n*c}')
 print('-'*30) 
  
    
    
print('acabou')

       
       
       