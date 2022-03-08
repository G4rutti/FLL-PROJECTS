from tkinter import *
from tkinter import ttk

class Tela1():
    cor_fundo = '#CDCDCD'

    def __init__(self):
        self.root = root
        self.configura_tela()
        self.widgets()

        root.mainloop()

    def configura_tela(self):
        self.root.geometry('320x480')
        self.root.resizable(False,False)
        self.root.configure(bg=self.cor_fundo)
        self.root.title('FLL PROJECT 1')


    def widgets(self):
        frame1 = Frame(root, width=320, height=50, bg='#49d462')
        frame1.pack()

        btn1 = Button(root, text='Conta', font='Helvetica 12', border=0, bg='#49d462')
        btn1.place(x=179,y=12)

        btn2 = Button(root, text='Sair', font='Helvetica 12', border=0, bg='#49d462')
        btn2.place(x=263,y=12)

        txt1 = Label(root, text='Boa tarde, Nome!', font='Helvetica 12', bg=self.cor_fundo)
        txt1.place(x=30,y=87)

        txt2 = Label(root, text='00 viagens | 00 problemas', font='Helvetica 8', bg=self.cor_fundo)
        txt2.place(x=30,y=110)

        self.cbox = ttk.Combobox(root, values=['Vaca','Galinha','Bezerro','Cavalo','Porco','Boi'])
        self.cbox.place(x=30,y=312, width=100, height=20)

        btn3 = Button(root, text='Escolher', font='Helvetica 12', border=0, bg='#49d462', command=self.function)
        btn3.place(x=30,y=355)
    
    def function(self):
        animal = self.cbox.get()
        
        if animal == 'Vaca':
            imagem = PhotoImage(file="images/Vaca-PNG-1280x720 (1).png")
            w = Label(root, image=imagem)
            w.imagem = imagem
            w.place(x=10,y=165)

            txt3 = Label(root, text=f'Você escolheu vaca.', font='Helvetica 12', bg=self.cor_fundo)
            txt3.place(x=150,y=160)

        elif animal == 'Galinha':
            imagem = PhotoImage(file="images/Galinha-Ares (1).png")
            w = Label(root, image=imagem)
            w.imagem = imagem
            w.place(x=20,y=146)

            txt3 = Label(root, text=f'Você escolheu galinha.', font='Helvetica 12', bg=self.cor_fundo)
            txt3.place(x=140,y=160)

        elif animal == 'Cavalo':
            imagem = PhotoImage(file="images/horse (1).png")
            w = Label(root, image=imagem)
            w.imagem = imagem
            w.place(x=0,y=122)

            txt3 = Label(root, text=f'Você escolheu cavalo.', font='Helvetica 12', bg=self.cor_fundo)
            txt3.place(x=140,y=160)

root = Tk()
Tela1()