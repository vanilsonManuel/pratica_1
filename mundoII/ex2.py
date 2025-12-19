""" 2: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
primitivo e todas as informações possíveis sobre ele. """

algo = str(input('digite algo:'))

if algo.isnumeric()==True:
    print('É numerico {}'.format(algo))
else:
        print('Não e numerico {}'.format(algo))

