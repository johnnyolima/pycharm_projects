qth = 0   # quantidade de homens
qtm = 0   # quantidade de mulheres

for i in range(10):
    sex = int(input("Informe o sexo (homem 1, mulher 2): "))

    if sex == 1:
        qth += 1
    elif sex == 2:
        qtm += 1
    else:
        print("Valor inválido! Digite 1 ou 2.")

print(f"Quantidade de homens = {qth}")
print(f"Quantidade de mulheres = {qtm}")

'''
sexom = 0
sexof = 0

for i in range(10):
    nome = input("informe nome: ")
    sexo = input("informe sexo(feminino ou masculino): ")
    if sexo == "feminino":
        sexof += 1
    elif sexo == "masculino":
        sexom += 1
     else:
	print("Sexo Inválido!")

print("a quantidade de mulheres é:", sexof)
print("a quantidade de homens é:", sexom)

'''