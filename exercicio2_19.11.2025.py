quantidade_homens = 0
quantidade_mulheres = 0
mulheres_altas = 0
homens_altos = 0
alturas_baixas = 0

resp = input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não: ").strip().upper()

while resp == "S":
    nome = input("Digite o nome da pessoa: ").strip()
    sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
    altura = float(input("Digite a altura da pessoa (em metros): ").replace(",", "."))

    # Contabilização por sexo
    if sexo == "M":
        quantidade_homens += 1
        if altura > 1.70:
            homens_altos += 1
    elif sexo == "F":
        quantidade_mulheres += 1
        if altura > 1.65:
            mulheres_altas += 1
    else:
        print("Sexo inválido. Registro ignorado.")
        resp = input("Continuar no Cadastro? Digite S para sim ou qualquer tecla para não: ").strip().upper()
        continue

    # Contagem de alturas abaixo de 1.60
    if altura < 1.60:
        alturas_baixas += 1

    resp = input("Continuar no Cadastro? Digite S para sim ou qualquer tecla para não: ").strip().upper()


print(f"\nQuantidade de homens: {quantidade_homens}")
print(f"Quantidade de mulheres: {quantidade_mulheres}")
print(f"Mulheres com altura > 1.65: {mulheres_altas}")
print(f"Homens com altura > 1.70: {homens_altos}")
print(f"Pessoas com altura < 1.60: {alturas_baixas}")
