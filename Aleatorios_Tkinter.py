import random
import tkinter as tk

def Aleatorios(): 
    limite_inferior = caixa1.get()
    limite_superior = caixa2.get()
    quantidade = caixa3.get()
    permitir_repetição = chkvalue.get()
    
    i = (limite_superior - limite_inferior) + 1
    lista = [limite_inferior]
    a = 1
    while a < i:
        lista.append(limite_inferior + a)
        a+=1

    if permitir_repetição == True:
        Aleatorios = list(random.choices(lista, k=quantidade))
        números["text"] = Aleatorios
    else: 
        x=0
        lista_resultado = []
        while x < quantidade:
            Aleatorio = list(random.choices(lista, k=1))
            lista_resultado.append(Aleatorio)
            z=set(lista)
            y = set(Aleatorio)
            lista = list(z.difference(y))
            x+=1
        números["text"] = lista_resultado


#Interface gráfica no tkinter
janela = tk.Tk()
janela.title("Números Aleatórios")
janela.configure (background = "cyan")
janela.columnconfigure(0, weight = 1, minsize = 80)
janela.columnconfigure(1, weight = 1, minsize = 20)

caixa1 = tk.IntVar()
caixa2 = tk.IntVar()
caixa3 = tk.IntVar()
chkvalue = tk.BooleanVar()

texto_introd = tk.Label(janela, text="Este programa sorteia, aleatóriamente, números "
                     "dentro do intervalo selecionado e na quantidade informadada",
                     background = "cyan", foreground = "black", relief = "solid", border = 2,
                     font = "Times 12 bold")
texto_introd.grid(row=0, column=0, padx=10, pady=10, sticky = "e")

texto_c1 = tk.Label(janela, text="Digite o limite inferior do intervalo:",
                 background = "cyan", foreground = "black", relief = "flat", border = 2,
                 font = "Arial 9 italic")
texto_c1.grid(row=1, column=0, padx = 10, pady = 10, sticky = "e")

texto_c2 = tk.Label(janela, text="Digite o limite superior do intervalo:",
                 background = "cyan", foreground = "black", relief = "flat", border = 2,
                 font = "Arial 9 italic")
texto_c2.grid(row=2, column=0, padx = 10, pady = 10, sticky = "e")

texto_c3 = tk.Label(janela, text="Digite a quantidade de números a serem sorteados:",
                 background = "cyan", foreground = "black", relief = "flat", border = 2,
                 font = "Arial 9 italic")
texto_c3.grid(row=3, column=0, padx = 10, pady=10, sticky = "e")
              
             
caixa_entrada1 = tk.Entry(janela, textvariable=caixa1, width = 10, background = "white",relief = "sunken", border = 5)
caixa_entrada1.grid (row=1, column=1, padx=10, pady=10)

caixa_entrada2 = tk.Entry(janela, textvariable=caixa2, width = 10, background = "white",relief = "sunken", border = 5)
caixa_entrada2.grid (row=2, column=1, padx=10, pady=10)

caixa_entrada3 = tk.Entry(janela, textvariable=caixa3, width = 10, background = "white",relief = "sunken", border = 5)
caixa_entrada3.grid (row=3, column=1, padx=10, pady=10)

caixa_checagem = tk.Checkbutton(janela, text='pode repetir nº', var=chkvalue) 
caixa_checagem.grid(row=4, column=1, padx=10, pady=10)
caixa_checagem.configure(font = "Arial 8", bg = "cyan")

números = tk.Label(janela, text="")
números.grid (row=5, column=0, padx = 10, pady = 10, sticky = "e")
números.configure (font = "Arial 10 bold",width = 88, background = "magenta", foreground = "black")

botão = tk.Button (janela, text = "Sortear", command = Aleatorios, background = "green")
botão.grid (row=5, column=1, padx=10, pady=10)
botão.configure(relief = "groove", border=5, font = "Times 12")

janela.mainloop()