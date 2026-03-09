from random import randint
computador = randint(1,5)
print('Vou pensar em um numero, tente adivinhar')
print('-=-' *20)
n = int(input('Digite um numero: '))
print('O computador pensou no numero: ',computador)

if n == computador:
    print('Parabéns, Voce acertou')
else:
    print('Voce errou')