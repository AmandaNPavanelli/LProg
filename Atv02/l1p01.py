### Programa para determinar minha idade em anos, meses e dias
### Amanda Pavanelli - UNIS - Outubro de 2021

### Biblioteca/Módulo -> Método:
from datetime import date

### Entrada de dados
Ano = input("Digite o ano que você nasceu (Exemplo: 1975): ")
Mes = input("Agora, digite o mês [01..12]: ")
Dia = input("Por fim, digite o dia [01..31]: ")

### Convertendo para inteiro
Ano = int(Ano)
Mes = int(Mes)
Dia = int(Dia)

### Construindo a data do seu Niver
niver = date(Ano,Mes,Dia)

### Data de hoje
hoje = date.today()

### Idade em quantidade de dias
IdadeDias = abs(hoje-niver).days

### Idade em anos
IdadeAnos = IdadeDias/365.25

### Idade em meses
IdadeMeses = IdadeDias/30.4

### Resultado Final:
print("\nResultado Final:")
print("Sua idade em anos = %.1f" %IdadeAnos)
print("Sua idade em meses = %.1f" %IdadeMeses)
print("Sua idade em dias = %.0f" %IdadeDias)

print("\nFIM!")
### FIM
