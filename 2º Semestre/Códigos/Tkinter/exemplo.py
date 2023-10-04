from tkinter import messagebox, Tk, Label, Entry, Button



def insert():
    if (cod_field.get() == "" and
            nome_field.get() == "" and
            end_field.get() == ""):
        messagebox.showinfo(
            title="Alerta",
            message="Por favor, insira dados!")


if (__name__ == "__main__"):
    lista_usuarios = []
    #criação do objeto Tk (formulário)
    form = Tk()
    form.title("Cadastro de Usuários")
    form.geometry("400x100")
    #criação das Labels
    cod = Label(form, text="Código")
    nome = Label(form, text="Nome")
    end = Label(form, text="Endereço")
    cod.grid(row=1, column=0)
    nome.grid(row=2, column=0)
    end.grid(row=3, column=0)
    cod_field = Entry(form)
    nome_field = Entry(form)
    end_field = Entry(form)
    #criação das caixas de texto
    cod_field.grid(row=1, column=1, ipadx="100")
    nome_field.grid(row=2, column=1, ipadx="100")
    end_field.grid(row=3, column=1, ipadx="100")
    #criação dos botões
    conf = Button(form, text="Confirmar", command=insert)
    conf.grid(row=8, column=0)
    conf = Button(form, text="Gravar em arquivo texto", command=insert)
    conf.grid(row=8, column=1)

    form.mainloop()