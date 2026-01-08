numeros = []

print('\nDigite os 5 cincos números:\n ')

for i in range(1, 6):
    x = float(input(f'{i}º valor: '))
    numeros.append(x)
    
print(f"\nOs cinco Número digitados: {numeros}")

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))