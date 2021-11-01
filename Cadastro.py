#import sqlite3
from tkinter import *
import tkinter as tk
import subprocess
#from time import sleep


def EXPRESS_GERA():
    def g_reactjs():

        res = en4.get()
        res2 = en5.get()
        gr = '--view=hbs'
        gr1 = '--view=ejs'
        gr2 = '--view=pug'
        gr3 = '--view=jade'
        r = 'hbs'
        r2 = 'ejs'
        r3 = 'pug'
        r4 = 'jade'
        cam = "cd {}".format(res)

        try:
            if res2 == r:
                cmd = ['gnome-terminal']  # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'echo ========== GERANDO UM PJ EXPRESS =========== &&'
                                                'express {} --css --git {} &&'
                                                '{} &&'
                                                'npm install cors nodemon dotenv --save &&'
                                                'code. &&'
                                                'sleep 5 &&'
                                                'exit; exec $SHELL'.format(gr, res, cam)])

                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8',
                            foreground='yellow')
                lb5.place(x=13, y=50)

            elif res2 == r2:
                cmd = ['gnome-terminal']  # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'echo ========== GERANDO UM PJ EXPRESS =========== &&'
                                                'express {} --css --git {} &&'
                                                '{} &&'
                                                'npm install cors nodemon dotenv --save &&'
                                                'code. &&'
                                                'sleep 5 &&'
                                                'exit; exec $SHELL'.format(gr1, res, cam)])

                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8',
                            foreground='yellow')
                lb5.place(x=13, y=50)

            elif res2 == r3:
                cmd = ['gnome-terminal']  # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'echo ========== GERANDO UM PJ EXPRESS =========== &&'
                                                'express {} --css --git {} &&'
                                                '{} &&'
                                                'npm install cors nodemon dotenv --save &&'
                                                'code. &&'
                                                'sleep 5 &&'
                                                'exit; exec $SHELL'.format(gr2, res, cam)])

                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8',
                            foreground='yellow')
                lb5.place(x=13, y=50)
            elif res2 == r4:
                cmd = ['gnome-terminal']  # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'echo ========== GERANDO UM PJ EXPRESS =========== &&'
                                                'express {} --css --git {} &&'
                                                '{} &&'
                                                'npm install cors nodemon dotenv --save &&'
                                                'code. &&'
                                                'sleep 5 &&'
                                                'exit; exec $SHELL'.format(gr3, res, cam)])

                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8',
                            foreground='yellow')
                lb5.place(x=13, y=50)

            else:

                cmd = ['gnome-terminal']  # Se estiver usando o GNOME
                cmd.extend(['-x', 'bash', '-c', 'echo ========== GERANDO UM PJ EXPRESS =========== &&'
                                                'express --no-view --git {} &&'
                                                '{} &&'
                                                'npm install cors nodemon dotenv --save &&'
                                                'code. &&'
                                                'sleep 5 &&'
                                                'exit; exec $SHELL'.format(res, cam)])

                subprocess.Popen(cmd, stdout=subprocess.PIPE)
                lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8',
                            foreground='yellow')
                lb5.place(x=13, y=50)

        except:
            lb5 = Label(dell, text='Houve um erro.', bg='#55cec8', foreground='red')
            lb5.place(x=13, y=50)

    def Sair():
        dell.destroy()

    dell = Tk()

    dell.title('DB_DELETE')
    dell['bg'] = '#55cec8'

    fr = Frame(dell, width=500, height=30, bg='#55cec8')
    fr.pack(side=TOP)

    lb0 = Label(fr, text='COLOQUE UM NOME PARA O SEU PROJETO', foreground='darkgreen', bg='#55cec8',
                font='Arial 13 bold')
    lb0.place(x=5, y=0)

    bt2 = Button(dell, text='GERA PROJETO', foreground='red', bg='yellow', command=g_reactjs)
    bt2.place(x=160, y=80)

    lb3 = Label(dell, text='   NOME DO PROJETO    TEMPLETE VIEW', foreground='darkgreen', bg='#55cec8', font='Arial 14 bold')
    lb3.place(x=10, y=120)

    lb3 = Label(dell, text='          |                                             |', foreground='darkgreen', bg='#55cec8', font='Arial 14 bold')
    lb3.place(x=10, y=142)

    en4 = Entry(dell, width=30, bg='white', foreground='black')
    en4.place(x=10, y=170)

    en5 = Entry(dell, width=7, bg='white', foreground='black')
    en5.place(x=265, y=170)

    bt6 = Button(dell, text='fecha', foreground='red', bg='yellow', command=Sair)
    bt6.place(x=332, y=165)

    dell.resizable(False, False)
    dell.geometry('400x200+500+100')
    dell.mainloop()

def CRETE_REACT():
    def g_reactjs():

        res = en4.get()
        cam = "cd {}".format(res)

        try:
            cmd = ['gnome-terminal']  # Se estiver usando o GNOME
            cmd.extend(['-x', 'bash', '-c', 'echo ========== INSTALANDO O EXPRESS-GENERATOR VIA NPM =========== &&'
                                            'create-react-app {} &&'
                                            'echo O projeto esta pronto, e agora instalaremos o react-router-dom &&'
                                            '{} &&'
                                            'cd src/ &&'
                                            'rm App.css &&'
                                            'rm index.css &&'
                                            'rm reportWebVitals.js &&'                                            
                                            'rm setupTests.js logo.svg &&'
                                            'cd ../ &&'
                                            'cp ../bk_reactjs/.prettierrc . &&'
                                            'cp ../bk_reactjs/index.html public/ &&'
                                            'cp ../bk_reactjs/index.js src/ &&'
                                            'cp ../bk_reactjs/App.js src/ &&'                                            
                                            'yarn add nodemon react-router-dom --save &&'
                                            'code. &&'                                         
                                            'sleep 10 &&'
                                            'exit; exec $SHELL'.format(res, cam)])

            subprocess.Popen(cmd, stdout=subprocess.PIPE)
            lb5 = Label(dell, text='O prjeto já ta sendo criado, veja o progreço no terminal. ', bg='#55cec8', foreground='yellow')
            lb5.place(x=13, y=50)

        except:
            lb5 = Label(dell, text='Houve um erro.', bg='#55cec8', foreground='red')
            lb5.place(x=13, y=50)

    def Sair():
        dell.destroy()

    dell = Tk()

    dell.title('DB_DELETE')
    dell['bg'] = '#55cec8'

    fr = Frame(dell, width=500, height=30, bg='#55cec8')
    fr.pack(side=TOP)

    lb0 = Label(fr, text='COLOQUE UM NOME PARA O SEU PROJETO', foreground='darkgreen', bg='#55cec8', font='Arial 13 bold')
    lb0.place(x=5, y=0)

    bt2 = Button(dell, text='GERA PROJETO', foreground='red', bg='yellow', command=g_reactjs)
    bt2.place(x=160, y=80)

    lb3 = Label(dell, text='NOME DO PROJETO', foreground='darkgreen', bg='#55cec8', font='Arial 14 bold')
    lb3.place(x=10, y=120)

    en4 = Entry(dell, bg='white', foreground='black')
    en4.place(x=200, y=120)

    bt6 = Button(dell, text='fecha', foreground='red', bg='yellow', command=Sair)
    bt6.place(x=332, y=165)

    dell.resizable(False,False)
    dell.geometry('400x200+500+100')
    dell.mainloop()

def NODE():

    cmd = ['gnome-terminal']  # Se estiver usando o GNOME
    cmd.extend(['-x', 'bash', '-c',
                'echo ========== ATUALIZANDO O SISTEMA E INSTLANDO DEPENDENCIAS =========== &&'
                'echo "" &&'
                'sleep 5 &&'
                '&& apt-get update -y && apt install -y wget && apt install -y gnome-terminal &&'
                'echo ================= AGORA INSTALAREMOS NODEJS VIA NVM ================= &&'
                'wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash &&'
                'apt-get update -y &&'
                'source ~/.profile &&'
                'nvm ls-remote &&'
                'nvm install 10.15.1 &&'
                'echo node instalado && node -v &&'
                'echo npm &&'
                'npm -v &&'
                'echo npx &&'
                'npx -v &&'
                'echo O NODE FOI ISNTALADO CORRETAMENTE &&'
                'sleep 8 &&'
                'exit; exec $SHELL'])

    subprocess.Popen(cmd, stdout=subprocess.PIPE)

    #system('wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash')
    #curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

def EXPRESS():
    cmd = ['gnome-terminal']  # Se estiver usando o GNOME
    cmd.extend(['-x', 'bash', '-c', 'echo ========== INSTALANDO O EXPRESS-GENERATOR VIA NPM =========== &&'
                                    'echo "" &&'
                                    'npm install -g express-generator &&'
                                    'sleep 8 && exit; exec $SHELL'])

    subprocess.Popen(cmd, stdout=subprocess.PIPE)

def REACT():
    cmd = ['gnome-terminal']  # Se estiver usando o GNOME
    cmd.extend(['-x', 'bash', '-c', 'echo ========== INSTALANDO O CREATE-REACT-APP VIA NPX =========== &&'
                                    'npx create-react-app -g &&'
                                    'echo "" &&'
                                    'sleep 5'
                                    'O create-react-app foi instalado com sucesso &&'
                                    'sleep 8 &&'
                                    'exit; exec $SHELL'])

    subprocess.Popen(cmd, stdout=subprocess.PIPE)
def Sair():
    app.destroy()

app = Tk()
app['bg'] = 'white'
app.title('Gera PJ Express e React-js')
#app.iconbitmap('i.icon')

im = PhotoImage(file="imagens/foto02.png") #/root/TK/Tkinter/imagens/test0.gif")
w = Label(app, image=im)
w.im = im
w.place(x=-50, y=-50)

bt0 = Button(app, text='INSTALA O NONEJS', font='Arial 13 bold', bg='yellow', foreground='blue', command=NODE)
bt0.place(x=75, y=50)

bt3 = Button(app, text='INSTALA CREATE_REACT_APP -G', font='Arial 13 bold', bg='yellow', foreground='blue', command=REACT)
bt3.place(x=75, y=90)

bt1 = Button(app, text='INSTALA EXPRESS-GENERATOR -G ', font='Arial 13 bold', bg='yellow', foreground='blue', command=EXPRESS)
bt1.place(x=75, y=130)

bt2 = Button(app, text='GERANDO UM PROJETO REACTJS', font='Arial 13 bold', bg='yellow', foreground='blue', command=CRETE_REACT)
bt2.place(x=75, y=170)

bt6 = Button(app, text='GERANDO UM PROJETO EXPRESS', font='Arial 13 bold', bg='yellow', foreground='blue', command=EXPRESS_GERA)
bt6.place(x=75, y=210)

bt6 = Button(app, text='fecha', foreground='red', bg='#55cec8', font='Arial 10 bold', width=3, command=Sair)
bt6.place(x=446, y=266)

app.resizable(False,False)
app.geometry('500x300+700+100')
app.mainloop()
