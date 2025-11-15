"""A escola “APRENDER” faz o pagamento de seus professores por hora/aula mais 15% do
salário referente ao Descanso Semanal Remunerado (DSR). Faça um programa que leia o
nível do professor (1 ou 2) e a quantidade de horas de aula dadas no Mês, calcule e
exiba o salário de um professor. Sabe-se que o valor da hora/aula segue a tabela abaixo:

Professor Nível 1 R$56,00 por hora/aula
Professor Nível 2 R$66,00 por hora/aula"""

nivel = int(input("Digite o nível do professor (1 ou 2): "))
horas = float(input("Digite a quantidade de horas/aula dadas no mês: "))

if nivel == 1:
    valor_hora = 56.00
elif nivel == 2:
    valor_hora = 66.00
else:
    print("Nível inválido! Use 1 ou 2.")
    exit()

salario_base = valor_hora * horas

dsr = salario_base * 0.15

salario_final = salario_base + dsr

print(f"Salário base: R${salario_base:.2f}")
print(f"DSR (15%): R${dsr:.2f}")
print(f"Salário final: R${salario_final:.2f}")