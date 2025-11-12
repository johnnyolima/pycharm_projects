salariob = float(input("Digite salário bruto do funcioNÁRIO: "))
ir = salariob * 11/100
inss = salariob * 8/100
sindicato = salariob*5/100
desconto = ir + inss + sindicato
saliq = salariob - desconto

print("Salário Bruto: Valor R$", salariob)
print("Imposto de renda 11% : Valor R$ ", ir)
print("Inss 8% : Valor R$", inss)
print("Sindicato 5% : Valor R$", sindicato)
print("Total de Desconto: Valor R$", desconto)
print("Salário Líquido: Valor R$", saliq)