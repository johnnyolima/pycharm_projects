'''
Faça um programa que calcule o desconto de uma compra feita em uma loja. O programa deve ler o valor
das compras e calcular o valor do desconto obedecendo os seguintes percentuais:
2% de desconto se a compra for menor ou igual que R$2.000,00;
3% de desconto se a compra for maior que R$ 2.000,00 e menor ou igual a R$ 3.000,00;
5% de desconto se for maior que R$ 3.000,00 e menor ou igual a R$ 5.000,00;
10% de desconto para compras acima de R$ 5.000,00.
O programa deverá exibir o valor da compra, o valor do desconto e o total a pagar.'''

valor = float(input("Digite o valor da compra: "))

if valor <= 2000:
    desconto = valor * 0.02
elif valor <= 3000:
    desconto = valor * 0.03
elif valor <= 5000:
    desconto = valor * 0.05
else:
    desconto = valor * 0.10

total = valor - desconto

print(f"Valor da compra: R${valor:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total:.2f}")