from tkinter import *


def bt_media():

     entrada1 = float(ent1.get())
     entrada2 = float(ent2.get())
     entrada3 = float(ent3.get())
     media = (entrada1 + entrada2 + entrada3)/2
     resultado['text']= media

     
janela = Tk()
janela.title('Programa para Calculo da  Média')
janela.geometry('500x350')
janela['bg'] = '#191970'

     
#Texto inicial
inicio = Label(janela, text='.... Informe suas notas...',fg='#D2691E', bg='#191970')
inicio.pack()

num1 = Label(janela, text=' Insira a primeira nota:',fg='#FFFFFF', bg='#191970')
num1.pack()
ent1 = Entry(janela,width=33)
ent1.pack()

num2 = Label(janela, text='Insira a segunda nota:',fg='#FFFFFF', bg='#191970')
num2.pack()
ent2 = Entry(janela,width=33)
ent2.pack()

num3 = Label(janela, text='Insira a terceira nota:',fg='#FFFFFF', bg='#191970')
num3.pack()
ent3 = Entry(janela,width=33)
ent3.pack()

#resultado
resultado = Label(janela,text='Sua nota nesse semestre foi:',fg='#FFFFFF', bg='#191970')
resultado.pack()

#botão
bt_media = Button(janela, text='Exibir Resultado', bg= '#D2691E', fg='white', width='30', command= bt_media)
bt_media.pack()


janela.mainloop()