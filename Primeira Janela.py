from tkinter import *

'''
janela = Tk()
janela.title('Sitema EPR')
janela.geometry('800x300')
janela.resizable(False, False)
Label(janela, text='Olá mundo', bg='black', fg='orange', padx=30, pady=30).grid(row=0, column=0)
janela.mainloop()
***************************************
exemplo de campo de login e senha
Entry(janela).grid(row=0, column=0)
Entry(janela, show='*').grid(row=1, column=0)
***************************************
Mudando propriedade de Texto
def mostrar():
    armazenarLabel['text'] = 'Botão foi Clicado'

janela = Tk()
janela.title('Sitema EPR')
janela.geometry('300x300')
janela.resizable(False, False)

Entry(janela).grid(row=0, column=0)
Entry(janela, show='*').grid(row=1, column=0)
Button(janela, text='Clique aqui', command=mostrar).grid(row=2, column=0)

armazenarLabel = Label(janela, text='ainda não foi clicado')
armazenarLabel.grid(row=3, column=0)

janela.mainloop()

'''
def mostrar():
    armazenarLabel['text'] = 'Botão foi Clicado'

janela = Tk()
janela.title('Sitema EPR')
janela.geometry('300x300')
janela.resizable(False, False)

Entry(janela).grid(row=0, column=0)
Entry(janela, show='*').grid(row=1, column=0)
Button(janela, text='Clique aqui', command=mostrar).grid(row=2, column=0)

armazenarLabel = Label(janela, text='ainda não foi clicado')
armazenarLabel.grid(row=3, column=0)

janela.mainloop()