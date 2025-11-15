quantidade = int(input("Quantos alunos a turma tem? "))

soma_medias = 0
for i in range(quantidade):
    print(f"\nAluno {i+1}:")
    nome = input("Nome do aluno: ")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    nota4 = float(input("Digite a 4ª nota: "))

    media = (nota1 + nota2+ nota3 + nota4) / 4
    soma_medias += media

    print(f"Média anual de {nome}: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

media_turma = soma_medias / quantidade

print("\n===== RESULTADOS DA TURMA =====")
print(f"Média da turma na disciplina: {media_turma:.2f}")