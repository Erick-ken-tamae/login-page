import time

inicio = int(input('Digite um número Inicial? '))
fim = int(input('Digite um número Final? '))
passo = int(input('Digite quantos passos? '))

if passo == 0:
    passo = 1

if inicio < fim and passo < 0:  #Esse laço é quando dar os passos para atras
    passo = -passo

if inicio > fim and passo > 0:  # Esse laço é para dar o passo para frente
    passo = -passo
    

print('\nContagem:\n')

for i in range(inicio, fim+1, passo):
    print(i)   
    time.sleep(1)

print("\nFinalizado!")

