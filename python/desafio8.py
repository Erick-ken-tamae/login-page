print("\n1- Calcular a média final:  " 
"      \n2- Verificar aprovação  " 
"      \n3- Maior nota " 
"      \n4-Menor nota:  ")

opcoes = int(input("Digite uma opção entre(1,2,3,4,5): "))

if opcoes == 1:
    n1 = float(input("Digite a sua primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    media = (n1+n2)/2
    print(media)
