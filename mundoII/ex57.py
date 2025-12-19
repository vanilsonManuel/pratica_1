"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informa o Sexo:[M\F]:')).strip().upper()[0]

while sexo not in 'MF':
    sexo =str(input('Dados invalidos. Por favor digite novamente ')).strip().upper()[0]
print('Sexo {} registado  com sucesso'.format(sexo))
  
   
    
