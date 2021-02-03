from random import random,uniform #importamos de la biblioteca estandar la funcion random del modulo random 
import math as m
import matplotlib.pyplot as plt     
import tkinter as tk
from tkinter import ttk #Importamos el modulo ttk
from tkinter import * #importamos todos los modulos restantes

class Aplicacion:
    def __init__(self):
        self.lx=[]
        self.ly=[]
        self.ly1=[]
        self.ventana1=tk.Tk()
        self.ventana1.title("Aproximacion de raiz con simulacion")
        self.ventana1.geometry("300x200")
        self.ventana1.resizable(0,0)
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Datos",width=20)        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)           
        self.login()    
        self.ventana1.mainloop()
        self.ventana2=tk.Tk()

    def login(self):
        self.label1=ttk.Label(self.labelframe1, text="Numero de dardos:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dato1=tk.IntVar(value=100000)
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.labelN=ttk.Label(self.labelframe1, text="Numero a aproximar:")
        self.labelN.grid(column=0, row=2, padx=5, pady=4)
        self.dato2=tk.DoubleVar(value=3)
        self.entryN=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entryN.grid(column=1, row=2, padx=5, pady=10)
        self.labelIn=ttk.Label(self.labelframe1, text="Indice de la raiz:")
        self.labelIn.grid(column=0, row=3, padx=5, pady=4)
        self.dato3=tk.DoubleVar(value=2)
        self.entryIn=ttk.Entry(self.labelframe1, textvariable=self.dato3)
        self.entryIn.grid(column=1, row=3, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Iniciar",command=self.operacion)
        self.boton1.grid(column=0, row=10, padx=5, pady=10)
        self.boton4=ttk.Button(self.labelframe1,text="Salir",command=self.salirV1)
        self.boton4.grid(column=1,row=10,padx=5,pady=5)

    def operacion(self):
        #############
        num=float(self.dato2.get())
        indice=int(self.dato3.get())
        r=num**(1/indice)
        z,s=m.modf(r)
        n=0
        N=int(self.dato1.get())
        for i in range(1,N+1):
            x=(s+1)*random()
            if x**indice<num:
                n+=1
            if i%10000==0:
                self.lx.append(i)
                self.ly.append((s+1)*n/i)
                self.ly1.append(m.sqrt(num)) 
        ###############
        self.ventana2=Toplevel()
        self.ventana2.geometry("870x110")
        self.ventana2.resizable(0,0)
        self.labelframe2=ttk.LabelFrame(self.ventana2, text="La aproximacion es:")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=6)
        self.label2=tk.Label(self.labelframe2,text=(s+1)*n/N,bg="black",fg="white",font=("Verdana",14))    
        self.label2.grid(row=2, column=2, padx=10,pady=5)
        self.labelframe3=ttk.LabelFrame(self.ventana2,text="Error porcentual: ")
        self.labelframe3.grid(column=2,row=0,padx=10,pady=6)
        self.label3=tk.Label(self.labelframe3,text=abs((r-(s+1)*n/N)/r)*100,bg="blue",fg="white",font=("Verdana",14))
        self.label3.grid(row=2,column=2,padx=10,pady=10)
        self.labelframe4=ttk.LabelFrame(self.ventana2,text="Valor real: ")
        self.labelframe4.grid(column=8,row=0,padx=10,pady=6)
        self.label4=tk.Label(self.labelframe4,text=r,bg="yellow",fg="black",font=("Verdana",14))
        self.label4.grid(row=2,column=2,padx=5,pady=5)
        self.boton2=ttk.Button(self.ventana2,text="Graficar",command=self.grafico)
        self.boton2.grid(column=15,row=0,padx=5,pady=5)
        self.boton3=ttk.Button(self.ventana2,text="Atras",command=self.salirV2)
        self.boton3.grid(column=18,row=0,padx=5,pady=5)

    def grafico(self):
        plt.subplots(figsize=(8, 6))
        plt.suptitle('Aproximacion de raiz de 3', fontsize=15)
        plt.plot(self.lx, self.ly, 'r-', label='Aproximacion')
        plt.plot(self.lx, self.ly1, 'g-', label='Valor real')
        plt.xlabel('Numero de iteraciones')
        plt.ylabel('Valor de y')
        plt.legend(['Aproximacion','Valor real'])
        plt.show()

    def salirV1(self):
        self.ventana1.quit()
        
    def salirV2(self):
        self.ventana2.destroy()  
#bloque
aplicacion1=Aplicacion()
