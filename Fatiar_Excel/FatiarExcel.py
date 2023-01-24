import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
import tkinter.font as tkFont
import os

class App:
    def __init__(self, root):
        Arquivo = tk.StringVar()
        SalveLocal = tk.StringVar()
        Cabecalho = IntVar()
        quantidade = IntVar()

        def local_Save():
            SalveLocal.set(filedialog.askdirectory())
        def local_Arquivo():
            Arquivo.set(filedialog.askopenfilename(defaultextension=NONE)) 
        def Fatiar():
            try:
                with open(Arquivo.get(), 'r') as f:
                    csvfile = f.readlines() 
                    linesPerFile = quantidade.get()
                filename = 1
                for i in range(0,len(csvfile),linesPerFile):
                    with open(str(filename) + '.csv', 'w+') as f: #abrir um excel com nome [numero_contagem].csv na variavel f            
                        if filename > 1:
                            if Cabecalho.get() == True:
                                f.write(csvfile[0]) #escrever cabeçalho            
                        f.writelines(csvfile[i:i+linesPerFile]) #escreve o restante das linhas até o numero de linhas desejado.            
                        print(f) #print nome do arquivo        
                    os.rename(f.name,SalveLocal.get()+"/"+f.name) #move o arquivo para pasta desejada.        
                    filename += 1  
            except Exception as e:
                messagebox.showerror("error",e)
            

        #titulo
        root.title("Split Excel")
        #tamanho que quero a janela
        width=500
        height=100
        #criação de janela abaixo
        root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
        #não deixar expandir a janela.
        root.resizable(width=False, height=False)

        #################################################################################
        Label(root, text='Arquivo: ').grid(row=0,column=0, sticky="E") #stick= North, South, East, west == alinhamento N,S,E,W
        Label(root, text='Quantidade de linhas por arquivo: ').grid(row=1,column=0, sticky="E")
        Label(root, text='Cabeçalho em todos arquivos: ').grid(row=2,column=0, sticky="E")
        Label(root, text='Local de salvamento: ').grid(row=4,column=0, sticky="E")
        e1 = Entry(root, textvariable = Arquivo).grid(row=0, column=1)
        e2 = Entry(root,textvariable=quantidade).grid(row=1, column=1)
        e3 = Entry(root, textvariable = SalveLocal).grid(row=4, column=1)
        Radiobutton(root, text='Sim', variable=Cabecalho, value=True).grid(row=2, column=1,sticky=W)
        Radiobutton(root, text='Não', variable=Cabecalho, value=False).grid(row=2, column=2,sticky=W)
        Button(root,text='Selecionar Local',command = local_Save).grid(row=4,column=2)
        Button(root,text='Selecionar Arquivo',command = local_Arquivo).grid(row=0,column=2)
        Button(root,text='Executar',command= Fatiar).grid(row=4,column=3)
        #################################################################################

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
    