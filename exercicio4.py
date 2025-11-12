altura = float(input("Altura da parede (m): "))
comprimento = float(input("Comprimento da parede (m): "))

area = altura * comprimento
litros = area / 3
latas = -(-litros // 3.6)  # arredonda pra cima sem precisar importar math
preco = latas * 107

print(f"\nLatas de tinta necessárias: {latas}")
print(f"Preço total: R$ {preco:.2f}")
