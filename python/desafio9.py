while True:
  print("1- Calcular a Média Final: ")
  print("2- Ver a aprovação: ")
  print("3-Maior Nota: ")
  print("4-Menor Nota: ")
  print("5-Sair: ")

  opcao =  int(input("Escolhe uma opção (1/2/3/4/5): "))


  if opcao == 1:
      soma = 0
      for i in range(1,3):
          nota = float(input(f"Digite a {i}º nota: "))
          soma += nota
      media = soma/2
      print(f"MEDIA {media:.2f}")

  elif opcao == 2:
    media = float(input('Digite a média do aluno: '))
    if media >= 6:
      print(f"Você está aprovado. Parabéns. Sua média {media:.2f}")
    else:
      print(f"Você esta Reprovado, Sua média é {media:.2f}")
  elif opcao == 3:
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2:  "))
    print("maior valor: ", max(n1, n2))
  elif opcao == 4:
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2:  "))
    print("maior valor: ", min(n1, n2))
  elif opcao == 5:
    print("-=-" *50)
    print("-----------------------PROGRAMA ENCERRADO-----------------------------")
    print("-=-" *50)
