
from tkinter import * # interfaçe grafica
from tkinter import ttk # traga a biblioteca do tkinter para ser direcionada para outra aba
from tkinter import messagebox # quero que apareca algmas caixas de funcionalidade

# Janela principal//// variavel que vai receber toda inteface
janela =Tk()
janela.title('Cadastro de cliente')
janela.geometry('700x400')

#notebook pra construir (abas)

abas = ttk.Notebook(janela)   # ttk construa abas dentro da janela
abas.pack(fill='both', expand=True)

#aba1 - cadastros

aba1 = Frame (abas)
abas.add(aba1, text='Cadastro')

#aba2- tabela

aba2= Frame (abas)
abas.add(aba2,text='Clientes Cadastrados')

#Função Cadastrar
def cadastrar(): # def obrigatorio////nome da função CADASTRAR PODE SER QUALQUER NOME
    nome =  entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    cidade = entry_cidade.get()    # get capta tudo o que for digitado

    if nome == '' or telefone == '' or email =='' or cidade == '':
        messagebox.showwarning('ERRO'),('Preencha todos os Campos!')
    else:
        tabela.insert('',END, values=(nome,telefone,email,cidade))
        entry_nome.delete(0,END)
        entry_telefone.delete(0,END)
        entry_email.delete(0,END)
        entry_cidade.delete(0,END)

        messagebox.showinfo('Sucesso','Cliente Cadastrado')

    
   

# aba de cadastro

Label(aba1, text='Nome').pack(pady=5)     #Label mesma coisa de uma legenda ///// NOME
entry_nome = Entry(aba1, width=40)        #entry minusculo variavel Entry Maiusculo FUNÇÃO///cria o quadradro pra colocar o nome
entry_nome.pack() # quero que fique logo abaixo do label/////NOME

Label(aba1, text='Telefone').pack(pady=5)     #Label mesma coisa de uma legenda ///// NOME
entry_telefone = Entry(aba1, width=40)        #entry minusculo variavel Entry Maiusculo FUNÇÃO///cria o quadradro pra colocar o nome
entry_telefone.pack()

Label(aba1, text='E-mail').pack(pady=5)     #Label mesma coisa de uma legenda ///// NOME
entry_email = Entry(aba1, width=40)        #entry minusculo variavel Entry Maiusculo FUNÇÃO///cria o quadradro pra colocar o nome
entry_email.pack()

Label(aba1, text='Cidade').pack(pady=5)     #Label mesma coisa de uma legenda ///// NOME
entry_cidade = Entry(aba1, width=40)        #entry minusculo variavel Entry Maiusculo FUNÇÃO///cria o quadradro pra colocar o nome
entry_cidade.pack()

Button(
    aba1,
    text='Cadastrar',
    bg='green',
    fg='white',
    width=20,
    command=cadastrar
).pack(pady=20)

####  aba tabela

colunas = ('Nome','Telefone','E-mail','Cidade')

tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show= 'headings'
)


for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill='both', expand=True, pady=20)



janela.mainloop()#sempre ultimo comando