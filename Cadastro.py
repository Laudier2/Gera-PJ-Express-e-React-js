import sqlite3
from tkinter import *
from os import system
import subprocess

def Brawse():
    system('sqlitebrowser')

def Dll():
    def Delelte():
        def db_delele(id):
            t = en4.get()
            return """
            DELETE FROM {} WHERE id='{}'
            """.format(t, id)

        con = sqlite3.connect('Database.db')
        cur = con.cursor()

        try:
            d = en5.get()

            cur.execute(db_delele(f'{d}'))
            con.commit()
            con.close()
            lb5 = Label(dell, text='Cliente Deletado do banco.    ', bg='gray', foreground='yellow')
            lb5.place(x=106, y=170)

        except:
            lb5 = Label(dell, text='Cliente Inesistente no banco.', bg='gray', foreground='red')
            lb5.place(x=106, y=170)

    def Sair():
        dell.destroy()

    dell = Tk()

    dell.title('DB_DELETE')
    dell['bg'] = '#55cec8'

    fr = Frame(dell, width=500, height=30, bg='#55cec8')
    fr.pack(side=TOP)

    lb0 = Label(fr, text='DELETAR CLIENTE DO BANCO', foreground='darkgreen', bg='#55cec8', font='Arial 15 bold')
    lb0.place(x=50, y=0)

    lb2 = Label(dell, text='PRIMEIRO VEJA O ID DO CLIENTE', foreground='darkgreen', bg='#55cec8', font='Arial 16 bold')
    lb2.place(x=20, y=40)

    bt2 = Button(dell, text='DELETAR', foreground='red', bg='yellow', command=Delelte)
    bt2.place(x=160, y=80)

    lb3 = Label(dell, text='Tabela', foreground='darkgreen', bg='#55cec8', font='Arial 14 bold')
    lb3.place(x=10, y=120)

    lb4 = Label(dell, text='ID', foreground='darkgreen', bg='#55cec8', font='Arial 14 bold')
    lb4.place(x=268, y=120)

    en4 = Entry(dell)
    en4.place(x=80, y=120)

    en5 = Entry(dell, width=5)
    en5.place(x=295, y=120)

    bt6 = Button(dell, text='fecha', foreground='red', bg='yellow', command=Sair)
    bt6.place(x=332, y=165)

    dell.resizable(False,False)
    dell.geometry('400x200+500+100')
    dell.mainloop()

def CDT():

    def cadastro():

        def pega(Nome, Idade, CPF, Email, Telefone, CEP, Enderesso):
            p = en7.get()

            conn = sqlite3.connect('Database.db')

            cursor = conn.cursor()

            cursor.execute(f"""
                   CREATE TABLE IF NOT EXISTS {p} (
                       Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       Nome TEXT NOT NULL,
                       Idade TEXT NOT NULL,
                       CPF TEXT NOT NULL,
                       Email TEXT UNIQUE NOT NULL,
                       Telefone TEXT NOT NULL,
                       CEP TEXT NOT NULL,
                       Enderesso TEXT NOT NULL

                   );
                   """)
            return """
            INSERT INTO {} (Nome, Idade, CPF, Email, Telefone, CEP, Enderesso)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(p, Nome, Idade, CPF, Email, Telefone, CEP, Enderesso)

        con = sqlite3.connect('Database.db')
        cur = con.cursor()

        r0 = en0.get()
        r1 = en1.get()
        r2 = en3.get()
        r3 = en2.get()
        r4 = en4.get()
        r5 = en5.get()
        r6 = en6.get()

        try:
            cur.execute(pega(f'{r0}', f'{r1}', f'{r2}', f'{r3}', f'{r4}', f'{r5}', f'{r6}'))
            con.commit()
            con.close()
            lb8 = Label(root, text='Dados inseridos com sucesso.', bg='white', foreground='green')
            lb8.place(x=75, y=280)

        except:
            lb9 = Label(root, text='Os dados Nao pode ser Inserido!', bg='white', foreground='red')
            lb9.place(x=75, y=280)

    def Sair():
        root.destroy()

    root = Tk()
    root['bg'] = '#5dc9aa'
    lb0 = Label(root, text='CADASTRO DE CLIENTES', foreground='blue', bg='#5dc9aa', font='Arial 15 bold')
    lb0.place(x=67, y=0)
    lb1 = Label(root, text='Nome', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb2 = Label(root, text='Idade', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb3 = Label(root, text='CPF', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb4 = Label(root, text='Email', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb5 = Label(root, text='Telefone', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb6 = Label(root, text='CEP', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb7 = Label(root, text='Enderesso', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')
    lb8 = Label(root, text='Nome Da Tabela', foreground='blue', bg='#5dc9aa', font='Arial 12 bold')

    lb1.place(x=5, y=30)
    lb2.place(x=5, y=60)
    lb3.place(x=5, y=90)
    lb4.place(x=5, y=120)
    lb5.place(x=5, y=150)
    lb6.place(x=5, y=180)
    lb7.place(x=5, y=210)
    lb8.place(x=5, y=250)

    en0 = Entry(root)
    en1 = Entry(root)
    en3 = Entry(root)
    en2 = Entry(root)
    en4 = Entry(root)
    en5 = Entry(root)
    en6 = Entry(root)
    en7 = Entry(root)

    en0.place(x=95, y=30)
    en1.place(x=95, y=60)
    en3.place(x=95, y=90)
    en2.place(x=95, y=120)
    en4.place(x=95, y=150)
    en5.place(x=95, y=180)
    en6.place(x=95, y=210)
    en7.place(x=5, y=270)

    bt = Button(root, text='ADICIONAR', foreground='red', bg='yellow', width=8, height=4, command=cadastro)
    bt.place(x=290, y=30)
    bt0 = Button(root, text='Fechar', foreground='red', bg='yellow', command=Sair)
    bt0.place(x=326, y=268)
    root.resizable(False,False)
    root.geometry('400x300+500+100')
    root.mainloop()

def VER():
    # Comando Para Lista Todas as Tabelas do Banco >> SELECT * FROM sqlite_master WHERE type='table';
    def VerInfo():
        def select(data, field):

            vr0 = en4.get()
            return """
            SELECT id, Nome, Idade, CPF, Email, Telefone, CEP, Enderesso 
            FROM {}
            WHERE {}={}
            """.format(vr0, field, data)
        try:

            con = sqlite3.connect('Database.db')
            cur = con.cursor()
            vr1 = en5.get()
            cur.execute(select('id', f'{vr1}'))

            data = cur.fetchall()
            for p in data:
                lb5 = Label(fr1, text=f'NOME : {p[1]}', bg='white', foreground='green', font='Arial 14 bold')
                lb5.place(x=2, y=5)
                lb6 = Label(fr1, text=f'IDADE : {p[2]}', bg='white', foreground='green', font='Arial 12 bold')
                lb6.place(x=2, y=25)
                lb7 = Label(fr1, text=f'CPF : {p[3]}', bg='white', foreground='green', font='Arial 12 bold')
                lb7.place(x=2, y=45)
                lb8 = Label(fr1, text=f'E-MAIL : {p[4]}', bg='white', foreground='green', font='Arial 12 bold')
                lb8.place(x=2, y=65)
                lb9 = Label(fr1, text=f'TELEFONE : {p[5]}', bg='white', foreground='green', font='Arial 12 bold')
                lb9.place(x=2, y=85)
                lb10 = Label(fr1, text=f'CEP : {p[6]}', bg='white', foreground='green', font='Arial 12 bold')
                lb10.place(x=2, y=105)
                lb11 = Label(fr1, text=f'ENDERESSO: {p[7]}', bg='white', foreground='green', font='Arial 9 bold')
                lb11.place(x=5, y=125)

        except:
            lb12 = Label(fr1, text='Cliente Inesistente no banco \nOu Nem uma Cixa preechida \nTente Novamente.', bg='white', foreground='red', font='Arial 14 bold')
            lb12.place(x=2, y=230)

    def Sair():
        upd.destroy()

    upd = Tk()

    upd.title('DB_UPDATE')
    upd['bg'] = '#5dc9aa'

    fr = Frame(upd, width=500, height=30, bg='#5dc9aa')
    fr.pack(side=TOP)

    fr1 = Frame(upd, width=270, height=300, bg='white')
    fr1.place(x=50, y=160)

    lb0 = Label(fr, text='VERIFICAR CLIENTE DO BANCO', foreground='blue', bg='#5dc9aa', font='Arial 15 bold')
    lb0.place(x=50, y=0)

    lb2 = Label(upd, text='INFORMAÇÕES DO CLIENTE', foreground='yellow', bg='#5dc9aa', font='Arial 16 bold')
    lb2.place(x=53, y=40)

    bt2 = Button(upd, text='VERIFICAR', foreground='red', bg='yellow', command=VerInfo)
    bt2.place(x=160, y=80)

    lb3 = Label(upd, text='Tabela', foreground='yellow', bg='#5dc9aa', font='Arial 14 bold')
    lb3.place(x=10, y=120)

    lb4 = Label(upd, text='ID', foreground='yellow', bg='#5dc9aa', font='Arial 14 bold')
    lb4.place(x=268, y=120)

    en4 = Entry(upd)
    en4.place(x=80, y=120)

    en5 = Entry(upd, width=5)
    en5.place(x=295, y=120)

    bt6 = Button(upd, text='fecha', foreground='red', bg='yellow', command=Sair)
    bt6.place(x=332, y=165)

    upd.resizable(False,False)
    upd.geometry('400x500+500+100')
    upd.mainloop()

def UPD():
    def update():
        def atualiza(Nome, Idade, CPF, Email, Telefone, CEP, Enderesso, id):
            t = en7.get()
            return """
            UPDATE {} SET Nome = '{}', Idade = '{}', CPF= '{}', Email = '{}', Telefone = '{}', CEP = '{}', Enderesso = '{}' WHERE id = '{}'
            """.format(t, Nome, Idade, CPF, Email, Telefone, CEP, Enderesso, id)

        con = sqlite3.connect('Database.db')
        cur = con.cursor()

        try:
            r0 = en0.get()
            r1 = en1.get()
            r2 = en2.get()
            r3 = en3.get()
            r4 = en4.get()
            r5 = en5.get()
            r6 = en6.get()
            r7 = en8.get()

            cur.execute(atualiza(f'{r0}', f'{r1}', f'{r2}', f'{r3}', f'{r4}', f'{r5}', f'{r6}', f'{r7}'))
            con.commit()
            con.close()

            lb11 = Label(root, text='''  Cliente 
Atualizado




     ''', bg='white', foreground='green')
            lb11.place(x=305, y=120)

        except:
            lb5 = Label(root, text='''Cliente 
Inesistente
Ou você
inserio
dados
invalido''', bg='white', foreground='red')
            lb5.place(x=304, y=120)

    def Sair():
        root.destroy()

    root = Tk()
    root['bg'] = '#5dee8f'
    lb0 = Label(root, text='ATUALIZA CLIENTES', foreground='blue', bg='#5dee8f', font='Arial 15 bold')
    lb0.place(x=67, y=0)
    lb1 = Label(root, text='Nome', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb2 = Label(root, text='Idade', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb3 = Label(root, text='CPF', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb4 = Label(root, text='Email', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb5 = Label(root, text='Telefone', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb6 = Label(root, text='CEP', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb7 = Label(root, text='Enderesso', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb8 = Label(root, text='Nome Da Tabela', foreground='blue', bg='#5dee8f', font='Arial 12 bold')
    lb9 = Label(root, text='ID', foreground='blue', bg='#5dee8f', font='Arial 12 bold')

    lb1.place(x=5, y=30)
    lb2.place(x=5, y=60)
    lb3.place(x=5, y=90)
    lb4.place(x=5, y=120)
    lb5.place(x=5, y=150)
    lb6.place(x=5, y=180)
    lb7.place(x=5, y=210)
    lb8.place(x=5, y=250)
    lb9.place(x=215, y=250)

    en0 = Entry(root)
    en1 = Entry(root)
    en3 = Entry(root)
    en2 = Entry(root)
    en4 = Entry(root)
    en5 = Entry(root)
    en6 = Entry(root)
    en7 = Entry(root)
    en8 = Entry(root, width=5)

    en0.place(x=95, y=30)
    en1.place(x=95, y=60)
    en3.place(x=95, y=90)
    en2.place(x=95, y=120)
    en4.place(x=95, y=150)
    en5.place(x=95, y=180)
    en6.place(x=95, y=210)
    en7.place(x=5, y=270)
    en8.place(x=200, y=270)

    bt = Button(root, text='ATUALIZA', foreground='red', bg='yellow', width=8, height=4, command=update)
    bt.place(x=290, y=30)
    bt0 = Button(root, text='Fechar', foreground='red', bg='yellow', command=Sair)
    bt0.place(x=326, y=268)
    root.resizable(False, False)
    root.geometry('400x300+500+100')
    root.mainloop()

def Sair():
    app.destroy()

app = Tk()
app['bg'] = 'white'

def Tabelas():
    w1.place(x=5000)
    bt4.place(x=5000)
    def Lista():

        vr = en0.get()
        conn = sqlite3.connect("Database.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM {}".format(vr))

        lst = Tk()
        lst.title('CLINTE DA TABELA')
        lst['bg'] = 'gray'
        r = cursor.fetchall()
        lb0 = Label(lst, text='{[0]}'.format(r), bg='gray', foreground='red')
        lb0.place(x=5, y=5)
        lb1 = Label(lst, text='{[1]}'.format(r), bg='gray', foreground='red')
        lb1.place(x=5, y=25)
        lb2 = Label(lst, text='{[2]}'.format(r), bg='gray', foreground='red')
        lb2.place(x=5, y=45)
        lb3 = Label(lst, text='{[3]}'.format(r), bg='gray', foreground='red')
        lb3.place(x=5, y=65)
        lb4 = Label(lst, text='{[4]}'.format(r), bg='gray', foreground='red')
        lb4.place(x=5, y=85)
        lb5 = Label(lst, text='{[5]}'.format(r), bg='gray', foreground='red')
        lb5.place(x=5, y=105)
        lb6 = Label(lst, text='{[6]}'.format(r), bg='gray', foreground='red')
        lb6.place(x=5, y=125)
        lb7 = Label(lst, text='{[7]}'.format(r), bg='gray', foreground='red')
        lb7.place(x=5, y=145)
        lb8 = Label(lst, text='{[8]}'.format(r), bg='gray', foreground='red')
        lb8.place(x=5, y=165)
        lb9 = Label(lst, text='{[9]}'.format(r), bg='gray', foreground='red')
        lb9.place(x=5, y=185)
        lb10 = Label(lst, text='{[10]}'.format(r), bg='gray', foreground='red')
        lb10.place(x=5, y=205)
        lb11 = Label(lst, text='{[11]}'.format(r), bg='gray', foreground='red')
        lb11.place(x=5, y=125)
        lb12 = Label(lst, text='{[12]}'.format(r), bg='gray', foreground='red')
        lb12.place(x=5, y=145)
        lb13 = Label(lst, text='{[13]}'.format(r), bg='gray', foreground='red')
        lb13.place(x=5, y=165)
        lb14 = Label(lst, text='{[14]}'.format(r), bg='gray', foreground='red')
        lb14.place(x=5, y=185)
        lb15 = Label(lst, text='{[15]}'.format(r), bg='gray', foreground='red')
        lb15.place(x=5, y=305)
        lst.geometry('1000x200+400+600')
        lst.mainloop()
        
    bt5 = Button(fr2, text='''VER LISTA 
DE CLIENTES''', foreground='yellow', bg='red', font='Arial 11 bold', command=Lista)
    bt5.place(x=25, y=25)
    en0 = Entry(fr2, width=16)
    en0.place(x=13, y=75)
    texto = StringVar()
    texto.set('TABELAS')
    var = subprocess.check_output('python3 tabelas.py', shell=True)
    lb3 = Label(fr2, text=var, foreground='blue', bg='white', font='Arial 14 bold')
    lb3.place(x=10, y=100)

im = PhotoImage(file="foto02.png") #/root/TK/Tkinter/imagens/test0.gif")
w = Label(app, image=im)
w.im = im
w.place(x=-50, y=-50)

fr = Frame(app, width=500, height=30, bg='gray')
fr.pack(side=TOP)

fr1 = Frame(app, width=3, height=400, bg='black')
fr1.place(x=314, y=30)

fr2 = Frame(app, width=180, height=400, bg='white')
fr2.pack(side=RIGHT)

im1 = PhotoImage(file="foto01.png") #/root/TK/Tkinter/imagens/p.png")
w1 = Label(fr2, image=im1)
w1.im1 = im1
w1.place(x=-100, y=-20)

lb3 = Label(fr2, text='TABELAS DO BANCO', foreground='blue', font='Arial 12 bold')
lb3.place(x=0, y=0)

bt4 = Button(fr2, text='VER TABELAS', foreground='yellow', bg='red', font='Arial 11 bold', command=Tabelas)
bt4.place(x=20, y=45)

lb1 = Label(app, text='GERENCIADOR DE BANCO_DB', foreground='yellow', bg='gray', font='Arial 15 bold')
lb1.place(x=50, y=0)

bt0 = Button(app, text='CADASTRA CLIENTE', font='Arial 13 bold', bg='yellow', foreground='blue', command=CDT)
bt0.place(x=75, y=50)

bt3 = Button(app, text='ATUALIZA  CLIENTE ', font='Arial 13 bold', bg='yellow', foreground='blue', command=UPD)
bt3.place(x=75, y=90)

bt1 = Button(app, text=' DELETAR  CLIENTE ', font='Arial 13 bold', bg='yellow', foreground='blue', command=Dll)
bt1.place(x=75, y=130)

bt2 = Button(app, text='VERIFICAR  CLIENTE', font='Arial 13 bold', bg='yellow', foreground='blue', command=VER)
bt2.place(x=75, y=170)

bt6 = Button(app, text='fecha', foreground='red', bg='gray', font='Arial 10 bold', width=3, command=Sair)
bt6.place(x=450, y=0)

bt6 = Button(app, text='sqlitebrowser', foreground='red', bg='yellow', command=Brawse)
bt6.place(x=155, y=250)

app.resizable(False,False)
app.geometry('500x300+700+100')
app.mainloop()
