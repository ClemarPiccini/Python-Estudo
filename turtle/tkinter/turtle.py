import turtle
import tkinter as tk

def desenhar(event):
    x = event.x - canvas.winfo_rootx()  # Posição X relativa ao canvas
    y = event.y - canvas.winfo_rooty()  # Posição Y relativa ao canvas
    tartaruga.goto(x, y)

# Cria uma janela usando Tkinter
janela = tk.Tk()

# Cria um canvas dentro da janela
canvas = tk.Canvas(janela, width=500, height=500)
canvas.pack()

# Cria uma tartaruga usando o módulo Turtle
tartaruga = turtle.RawTurtle(canvas)
tartaruga.speed(0)  # Define a velocidade da tartaruga para a máxima

# Vincula o evento de clique do mouse ao desenho da tartaruga
canvas.bind("<B1-Motion>", desenhar)

# Função para limpar o desenho
def limpar():
    tartaruga.clear()

# Cria um botão para limpar o desenho
botao_limpar = tk.Button(janela, text="Limpar", command=limpar)
botao_limpar.pack()

# Inicia o loop principal da janela
janela.mainloop()
