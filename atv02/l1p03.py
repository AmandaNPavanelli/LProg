### Programa para determinar o menor de três valores
### Amanda Pavanelli - UNIS - Outubro de 2021

### Entrada de dados
print("\n\tENTRADA DE DADOS - 3 NÚMEROS INTEIROS")
N1 = int( input("Digite o primeiro número: ") )
N2 = int( input("Digite o segundo número: ") )
N3 = int( input("Digite o terceiro número: ") )

### Construindo uma lista
Lista = [N1, N2, N3]
### Ordenando a lista
Lista.sort()

### Selecionando o menor
Menor = Lista.pop(0)

### Resultado proposto
print("\nO menor, dentre os 3 números digitados, é o %i." %Menor)

print("\nFIM")
### FIM
