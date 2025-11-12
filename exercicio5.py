premio_total = float(input("Digite o valor total do prêmio (R$): "))

imposto = premio_total * 0.07
premio_liquido = premio_total - imposto


ganhador1 = premio_liquido * 0.46
ganhador2 = premio_liquido * 0.32
ganhador3 = premio_liquido - ganhador1 - ganhador2

print(f"\nValor total do prêmio: R$ {premio_total:.2f}")
print(f"Desconto do imposto (7%): R$ {imposto:.2f}")
print(f"Prêmio líquido após imposto: R$ {premio_liquido:.2f}")
print(f"\nGanhador 1 receberá: R$ {ganhador1:.2f}")
print(f"Ganhador 2 receberá: R$ {ganhador2:.2f}")
print(f"Ganhador 3 receberá: R$ {ganhador3:.2f}")
