# -*- coding: utf-8 -*-
### Programa da Calculadora IMC - Amanda Pavanelli

### Importando os Módulos
from PyQt5 import QtCore, QtGui, QtWidgets

### Classe para cada pessoa que interagir com a calculadora
class Pessoa:
    def __init__(self, N, H, W):
        self.nome = N
        self.altura = H
        self.peso = W
        self.imc = (W)/(H*H)
        if self.imc < 17:
            self.cond = "muito abaixo do peso ideal."
        elif self.imc >= 17 and self.imc < 18.49:
            self.cond = "abaixo do peso ideal."
        elif self.imc >= 18.49 and self.imc < 24.99:
            self.cond = "no seu peso ideal."
        elif self.imc >= 24.99 and self.imc < 29.99:
            self.cond = "acima do peso ideal."
        elif self.imc >= 29.99 and self.imc < 34.99:
            self.cond = "com obesidade nível 1."
        elif self.imc >= 34.99 and self.imc < 39.99:
            self.cond = "com obesidade nível 2."
        elif self.imc >= 39.99:
            self.cond = "com obesidade mórbida."

### Classe do Objeto da Janela Principal
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ### Parâmetros da janela principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 551)
        MainWindow.setStyleSheet("background-color: rgb(203, 172, 255);\n" "color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ### Line Edit 1 ->  Entrada para o Nome
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 120, 641, 32))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        ### Line Edit 2 -> Entrada para o Endereço
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 170, 641, 32))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        ### Line Edit 3 -> Entarda para Altura (cm)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 230, 191, 32))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        ### Line Edit 4 -> Entrada para o Peso (kg)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 280, 191, 32))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        ### TextEdit -> Saída do programa: Resiltado
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 220, 411, 101))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        ### Labels para referenciar o programa
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 40, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(214, 26, 124);")
        self.label_6.setObjectName("label_6")
        ### Push Button 1 - Sair do programa
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 370, 88, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n" "background-color: rgb(214, 26, 124);")
        self.pushButton.setObjectName("pushButton")
        ### Push Button 2 - Realiza Cálculos
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 370, 88, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(214, 26, 124);\n" "color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        ### Push Button 3 - Reinicia o programa
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 370, 88, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(214, 26, 124);\n" "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        ### Configurações do Objeto Janela Principal
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ### Ações dos botões
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.calculo)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_3.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

### Função para definir os labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome do Paciente"))
        self.label_2.setText(_translate("MainWindow", "Endereço Completo"))
        self.label_3.setText(_translate("MainWindow", "Altura (cm)"))
        self.label_4.setText(_translate("MainWindow", "Peso (KG)"))
        self.label_5.setText(_translate("MainWindow", "CALCULADORA DE IMC"))
        self.label_6.setText(_translate("MainWindow", "Determine o seu Indice de Massa Corporal"))
        self.pushButton.setText(_translate("MainWindow", "Sair"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcular"))
        self.pushButton_3.setText(_translate("MainWindow", "Reiniciar"))

## Função para calcular o IMC do usuário
    def calculo(self):
        end = self.lineEdit_2.text() ## Pegando o endereço
        Nome = self.lineEdit.text()  ## Nome Completo
        NN = Nome.split()            
        nome = NN[0]                 ## Primeiro Nome
        hm = float(self.lineEdit_3.text())/100.0  ## Altura
        wg = float(self.lineEdit_4.text())        ## Peso
        ps = Pessoa(nome, hm, wg)                 ## IMC da Pessoa
        self.textEdit.setText("%s, seu IMC = %.2f, você está %s\nNosso agente de saúde irá visitá-lo, no seguinte endereço:\n%s." %(ps.nome, ps.imc, ps.cond, end))

### Função principal de execução do programa 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

### FIM    
