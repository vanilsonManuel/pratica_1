# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 21:30:35 2025

@author: pt
"""

"""Nessa aula, vamos aprender como utilizar a instrução break e
 os loopings infinitos a favor das nossas estratégias de código.
 É muito importante saber usar o break no Python, 
 já que em alguns casos precisamos interromper um laço no meio do caminho."""
 

"""
cont = 0
while cont <=10:
    print(cont,'->',end='')
    cont +=1
print('Acabou')""" 

n= cont =0
s = 0

while True:
  n = int(input('Digite o numero:'))
  if n== 999:
      break
  s +=n
#print(' A soma {}'.format(s))
print(f' A soma e {s}')






