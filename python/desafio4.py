while True:
     a = int(input("Qual número da tabuada (Digite 0 para sair)?  "))
     
     for i in range(1, 11):
        print(f'{a} X {i} = {a * i}')
        
        if a == 0:
            print("Programa Encerrado")
            break