import tkinter as tk

# função que consomeuma api pública
from moeda import apidolar

def dolar():
    cotacao = float(apidolar())
    reais = float(valor.get())
    conta = round(reais / cotacao,2)
    mensagem = f'Com R$ {reais} reais compra-se $ {conta} dolares'
    resposta.config(text=mensagem)
    #return mensagem

janela = tk.Tk()

janela.geometry('450x300+50+50')
janela.title('Aula 04 - Tkinter')
janela.configure(bg='#042940')

titulo = tk.Label(janela, text='Conversor de Reais para Dólar', font =('Verdana', 16), fg='#DBF227', bg='#042940')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digte o valor em reais para Converter', font=('Verdana', 12),  fg='#DBF227', bg='#042940')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#D6D58E', fg='#005C53')
valor.pack(pady=10)

botao = tk.Button(janela, text='CONVERTER', command=dolar, bg='#9FC131', fg='#042940')
botao.pack(pady=10)

resposta = tk.Label(janela, text='', font=('Verdana', 12),  fg='#DBF227', bg='#042940')
resposta.pack(pady=10)

janela.mainloop()

