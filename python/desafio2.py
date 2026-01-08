nota1 = int(input("Digite a sua 1º nota: "))
nota2 = int(input("Digite a sua 2º nota: "))
nota3 = int(input("Digite a sua 3º nota: "))


media_notas =  (nota1 + nota2 + nota3)/3


if media_notas >= 7:
    print(f'Aprovado! Meus parabéns você tirou {media_notas:.2f}')

elif media_notas >= 5:
    nota_urgente = 14 - media_notas
    
    if nota_urgente > 10:
        print('Mesmo com recuperação, não é possivel passar.')
    else:
        print(f'Sua média foi {media_notas:.2f}')
        print(f'A sua nota da média não foi atingida, você precisa tirar {nota_urgente:.2f} ')
else:
    print(f'Reprovado direto. Sua média foi {media_notas:.2f}')
    
