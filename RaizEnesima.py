import sys  
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from DialogoRaizEnesima import RaizEnesima
from random import random
import matplotlib.pyplot as plt   
import math as m

class raiz(QDialog):
    def __init__(self):
        super().__init__()
        self.error=''
        self.valor=''
        self.lx=[]
        self.ly=[]
        self.ly1=[]
        self.ui=RaizEnesima()
        self.ui.setupUi(self)
        self.ui.btn_calcular.clicked.connect(self.calcular) 
        self.show()
    
    def calcular(self):
        suma=0
        try:
            if len(self.ui.txt_raiz.text())>0 and len(self.ui.txt_grado.text())>0 and len(self.ui.lineEdit.text())>0:
                grado=int(self.ui.txt_grado.text())
                assert type(grado)==int 
                raiz=int(self.ui.txt_raiz.text())
                r=raiz**(1/grado)
                real=m.sqrt(raiz)
                z,s=m.modf(r)
                N=int(self.ui.lineEdit.text())
                for i in range(1,N+1):
                    x=(s+1)*random()
                    if x**grado<raiz:
                        suma+=1
                    if i%10000==0:
                        self.lx.append(i)
                        self.ly.append((s+1)*suma/i)
                        self.ly1.append(m.sqrt(raiz))
                self.valor=(s+1)*suma/N
                self.error=abs((r-self.valor)/r)*100
                if self.ui.cbx_error.isChecked()==1:
                    #self.ui.cbx_error.stateChanged.connect(self.errorr) 
                    self.ui.txt_error_print.setText(str(self.error))   
                else:
                    self.ui.txt_error_print.setText("None")
                if self.ui.cbx_grafica.isChecked()==1:
                    
                    plt.subplots(figsize=(8, 6))
                    plt.suptitle(f'Aproximacion de raiz de {raiz}', fontsize=15)
                    plt.plot(self.lx, self.ly, 'r-', label='Aproximacion')
                    plt.plot(self.lx, self.ly1, 'g-', label='Valor real')
                    plt.xlabel('Numero de iteraciones')
                    plt.ylabel('Valor de y')
                    plt.legend(['Aproximacion','Valor real'])
                    plt.show()    
                self.ui.txt_resultado.setText(str(self.valor))
                self.ui.txt_real.setText(str(real))
            else:
                QMessageBox.about(self,"** ERROR ** ","Escriba un numero, no sea pelotudo")  
        except:
            QMessageBox.about(self,"** ERROR ** ","AMLOVER Tenia que ser")        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    ventana=raiz()
    ventana.show()
    sys.exit(app.exec_())