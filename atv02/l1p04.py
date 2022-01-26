### Programa para determinar números primos
### Amanda Pavanelli - UNIS - Outubro de 2021

### Biblioteca/Módulo
import time

### Função para determinar número primo
def meuPrimo(N):
  N2 = N/2    ### Limite para varredura
  D = 1       ### Denominador inicial
  R = 1       ### Valor inicial para o resto 
  while (D <= N2 and R != 0):  ### Buscando um denominador
    D += 1        ### Variando o denominador
    R = N%D       ### Determinando o Resto da divisão
  if (D > N2 and N > 1):   ### Se não houve denominador
    return True            ### O número é primo
  else:                    ### Se houver denominador sem resto
    return False           ### O número não é primo

### Entrada de dado, um valor inteiro:
M = int( input("Digite um número inteiro: ") )
S = meuPrimo(M)

### Resposta para o valor digitado -> Sugestão: 1296817
if (S == True):
  print("Esse número é primo!")
else:
  print("Esse número não é primo!")

### Tempo para ver a resposta acima - 2 segundos
time.sleep(2)

### Varredura sugerida na questão
print("\nVarredura sugerida:")
C = 0
for i in range(100):
  T = meuPrimo(i+1)
  if (T == True):
    print("O número %i é primo." %(i+1))
    C += 1
  else:
    print("O número %i não é primo." %(i+1))

print("\nObservamos ", C, " números primos até 100.")

print("\nFIM")
### FIM
