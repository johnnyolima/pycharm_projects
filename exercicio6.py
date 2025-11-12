paes = int(input("Digite a quantidade de pães vendidos: "))
broas = int(input("Digite a quantidade de broas vendidas: "))

preco_pao = 0.80
preco_broa = 2.50
cotacao_euro = 6.14

venda_total = (paes * preco_pao) + (broas * preco_broa)
custo_fabricacao = venda_total * 0.43
lucro_liquido = venda_total - custo_fabricacao

poupanca = lucro_liquido * 0.15
valor_em_euros = (lucro_liquido * 0.15) / cotacao_euro

print("\n--- RESUMO DO DIA ---")
print(f"Total arrecadado: R$ {venda_total:.2f}")
print(f"Custo de fabricação (43%): R$ {custo_fabricacao:.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:.2f}")
print(f"Valor guardado na poupança (15%): R$ {poupanca:.2f}")
print(f"Valor convertido em euros (15%): € {valor_em_euros:.2f}")