import tkinter as tk

#criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("400x300")

#CRIAR UM FRAME
frame = tk.Frame(janela, bg='black', padx=20, pady=20)
frame.pack(expand=True)

#Título
titulo =  tk.Label(frame, text="Cáculo de Média", font=("Arial", 16))
titulo.pack(pady=10)

#Campo Nota 1
tk.Label(frame, text="Nota1: ").pack()
nota1_entry = tk.Entry(frame)
nota1_entry.pack()

#Campo Nota 2
tk.Label(frame, text="Nota 2: ").pack()
nota2_entry = tk.Entry(frame)
nota2_entry.pack()

#Campo Nota 3
tk.Label(frame, text="Nota3: ").pack()  
nota3_entry = tk.Entry(frame)
nota3_entry.pack()

#Funções
def calcular_media():
    n1 = float(nota1_entry.get())
    n2 = float(nota2_entry.get())
    n3 = float(nota3_entry.get())
    
    media = (n1+ n2 + n3)/3
    
    if media >= 7:
        resultado.config(text=f"Aprovado! Média atiginda {media:.2f}", fg="green")
    elif media < 7:
        resultado.config(text=f"Recuperação! Média{media:.2}", fg="orange")
    else:
         resultado.config(text=f"Reprovado! Média: {media:.2f}", fg="red")

#Botões
botao = tk.Button(frame, text="Calcular", command=calcular_media)
botao.pack(pady=10)

# Resultado
resultado = tk.Label(frame, text="")
resultado.pack()

# Rodar a janela
janela.mainloop()