### Programa para verificar se três valores constituem um triângulo
### Amanda Pavanelli - UNIS - Outubro de 2021

### Biblioteca/Módulo -> Método
from math import sqrt

### Entrada de dados
print("\nEntrada de dados - Defina 3 valores.")
N1 = input("\nDigite o primeiro valor: ")
N2 = input("Digite o segundo valor: ")
N3 = input("Digite o terceiro valor: ")

### Construindo a lista
Lista = [float(N1), float(N2), float(N3)]
### Ordenando a lista [menor .. maior]
Lista.sort()

### Pegando o último (maior) elemento da lista
A = Lista.pop()   ## O maior vai ser o A
B = Lista.pop()   ## O médio vai ser o B
C = Lista.pop()   ## O menor vai ser o C

## Soma dos menores lados
D = B+C

### Semiperímetro do possível triângulo
P = (A+B+C)/2

### RESULTADO FINAL - Descobrindo se é um triângulo
print("\n\tResultado Final")
print("Considerando que os valores digitados")
print("representam os lados de um triângulo,")
if (A < D):     ### Desigualdade triangular de Cauchy-Schwarz
  ### Área do triângulo - Fórmula de Heron
  S = sqrt( P*(P-A)*(P-B)*(P-C) )
  print("então, temos um triângulo, com área = %.2f m²" %S)
else:           ### Se A >= D, não temos triângulo, nem pontes
  print("então, não temos um triângulo!")

print("\nFIM")
### FIM
