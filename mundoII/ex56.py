'''Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


media_idade=0
soma_idade =0
nome_maisVelho = ''
homem_maisVelho=0
conta_mulher =0
for c in range(1,3):
    print('----- {}ª pessoa-----'.format(c))
    nome =str(input('Informe o nome:'))
    idade =int(input('Informe a idade:'))
  
    sexo = str(input('Informe o Sexo M ou F:')).upper().strip()
    soma_idade +=idade
    media_idade =soma_idade /2
    if c==1 and sexo =='M':
        homem_maisVelho = idade
        nome_maisVelho =nome
    if sexo =="F"and idade<20:
      conta_mulher+=1
    
    
print('A media do grupo e de {}'.format(media_idade))    
print('o homem mais velho é o {} tem de idade {}'.format(nome_maisVelho,homem_maisVelho))
print('Mulheres com menos de 20 anos são {}'.format(conta_mulher))