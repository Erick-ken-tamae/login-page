while True:
    n = int(input("Digite um número (0 para sair): "))

    if n == 0:
        print("Programa encerrado.")
        break

    if n % 2 == 0:
        print(f"O número {n} é par")
    else:
        print(f"O número {n} é ímpar")
