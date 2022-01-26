# -*- coding: utf-8 -*-
### Prograna para calculadora IMC - Amanda Pavanelli

### Importando Módulos
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sq

### Conectando e preparando o banco de dados
con = sq.connect("IMC.db")   ## Conectando ao banco de dados
exe = con.cursor()           ## Criando o cursor (executor) do BD

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

### Classe para o Objeto Janela Principal
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ### Parâmetros da Janela Principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 594)
        MainWindow.setStyleSheet("background-color: rgb(191, 191, 143);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ### Line Edit 1 -> Entrada para o Nome
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 100, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        ### Line Edit 2 -> Entrada para o Endreço
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 170, 711, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        ### Line Edit 3 -> Entrada para a Altura (cm)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 240, 221, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        ### Line Edit 4 -> Entrada para o Peso (kg)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 310, 221, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        ### Text Edit -> Saída do programa: Resultado
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(520, 230, 461, 141))
        self.textEdit.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.textEdit.setObjectName("textEdit")
        ### Labels para referenciar o programa
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 60, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        ### Push Button 1 - Sair do programa
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 140, 130);\n" "color: rgb(0, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        ### Push Button 2 -> Realiza os cálculos
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 140, 130);\n" "color: rgb(0, 85, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        ### Push Button 3 -> Reinicia o programa
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 140, 130);\n" "color: rgb(0, 85, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        ### Push Button 4 -> Mostra a estatística dos dados
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(635, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 140, 130);\n" "color: rgb(0, 85, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        ### Configurações do Objeto Janela Principal 
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ### Ações dos Botões
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.calculo)
        self.pushButton_2.clicked.connect(self.saveDados)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_3.clicked.connect(self.textEdit.clear)
        self.pushButton_4.clicked.connect(self.lineEdit.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_4.clicked.connect(self.textEdit.clear)
        self.pushButton_4.clicked.connect(self.showDados)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ### Função para definir os labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora de IMC"))
        self.label.setText(_translate("MainWindow", "Nome do Paciente"))
        self.label_2.setText(_translate("MainWindow", "Endereço Completo"))
        self.label_3.setText(_translate("MainWindow", "Altura (cm)"))
        self.label_4.setText(_translate("MainWindow", "Peso (Kg)"))
        self.label_5.setText(_translate("MainWindow", "CALCULADORA DE IMC"))
        self.label_6.setText(_translate("MainWindow", "Determine o seu Índice de Massa Coporal"))
        self.pushButton.setText(_translate("MainWindow", "Sair"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcular"))
        self.pushButton_3.setText(_translate("MainWindow", "Reiniciar"))
        self.pushButton_4.setText(_translate("MainWindow", "IMC Médio"))

## Função para calcular o IMC do usuário
    def calculo(self):
        end = self.lineEdit_2.text()  ## Pegando o endereço
        Nome = self.lineEdit.text()   ## Nome completo
        NN = Nome.split()
        nome = NN[0]                  ## Primeiro Nome
        hm = float(self.lineEdit_3.text())/100.0   ## Altura
        wg = float(self.lineEdit_4.text())         ## Peso
        ps = Pessoa(nome, hm, wg)                  ## IMC da Pessoa
        self.textEdit.setText("%s, seu IMC = %.2f, você está %s\nNosso agente de saúde irá visitá-lo, no seguinte endereço:\n%s." %(ps.nome, ps.imc, ps.cond, end))

## Função para salvar os dados no meu banco de dados
    def saveDados(self):
        Nome = self.lineEdit.text()   
        Peso = float(self.lineEdit_4.text())
        Altura = float(self.lineEdit_3.text())/100.0
        IMC = Peso/(Altura*Altura)
        ### Conectando e preparando o banco de dados
        con = sq.connect("IMC.db")   ## Conectando ao banco de dados
        exe = con.cursor()           ## Criando o cursor (executor) do BD
        exe.execute("""INSERT INTO Pessoas(Nome, Peso, Altura, IMC) VALUES (?, ?, ?, ?);""", [Nome, Peso, Altura, IMC])
        con.commit()
        con.close()   ## Fechando a conexão com o Banco de Dados

## Função para analisar os dados armazenados no Banco de Dados
    def showDados(self):
        imcs = []
        ### Conectando e preparando o banco de dados
        con = sq.connect("IMC.db")   
        exe = con.cursor()           
        exe.execute("""SELECT * FROM Pessoas;""")
        dados = exe.fetchall()  ## Linhas da saída acima
        con.close()   
        for dado in dados:
            imcs += [dado[4]]
        soma = sum(imcs)
        media = soma/len(dados)
        self.textEdit.setText("O IMC médio dos dados armazenados é = %.1f, para maiores detalhes acesse o nosso banco de dados!" %media)


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
