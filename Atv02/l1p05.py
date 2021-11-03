### Programa para inverter as palavras de uma sentença
### Amanda Pavanelli - UNIS - Outubro de 2021

### Função para inverter strings: palavras e frases
def inVerte(texto):
  N = len(texto)      ### Tamanho do texto - caracteres
  invertido = ''      ### Pra armazenar o texto invertido
  ### Loop de inversão
  for i in range(N):
   N1 = N-(i+1)              ### Índice da última letra
   invertido += texto[N1]    ### Que vai ser a primeira
  return invertido           ### Retornando o texto invertido

### ENTRADA DE DADOS
frase = input("Entre com uma frase simples:\n")

### Revertendo a frase toda
esarf = inVerte(frase)
print("\nFrase completamente invertida:")
print(esarf)

### Lista de palavras da frase
Lista = frase.split()

### Determinando a resposta para a questão proposta
resposta = ''
for W in Lista:
  resposta += inVerte(W) + ' '

### Resposta obtida
print("\nFrase com palavras invertidas:")
print(resposta)

print("\nFIM")
### FIM
