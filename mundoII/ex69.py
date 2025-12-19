# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:03:44 2025

@author: pt
"""

"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:"""

idades=[]
sexos =[]
cont_idade=0
cont_m=0
cont_h=0
while True :
    print('-'*30)
    idade =int(input("Informa a idade:"))
    if idade > 18:
        cont_idade +=1
    sexo = ' '
    while sexo  not in 'MF':
        sexo = str(input("Informa o Sexo [M-F] ")).strip().upper()[0]
    print('-'*30)
    
    
    if sexo=='F' and idade < 20:
       cont_m+=1
    elif sexo =='M':
        cont_h+=1
    idades.append(idade)
    sexos.append(sexo)
    op = ' '
    while op not in 'SN':
        op =str(input('Deseja continuar Adicionar [ S- N] ')).strip().upper()[0]
    
       
    if op == 'N':
        print('Voce saiu')
        break
print(f' Foram adicionados  {cont_m} mulheres com menos de 20 anos')   
print(f' Foram adicionados  {cont_idade} pessoas maior de 18 anos') 
print(f' Foram adicionados  {cont_h} homens')
#print(f' As idades adicionadas foram {idades}') 
#print(f'Os sexos adicionadas foram {sexos}') 
    



