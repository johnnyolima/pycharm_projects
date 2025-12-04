alunos = []

resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
while resp == "S":
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos.append({"aluno":aluno, "nota": nota})
    resp = (input("continuar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()

qt_nota = 0
for aluno in alunos:
    alun = aluno["aluno"]
    nota = aluno["nota"]

    qt_nota += 1
    qt_nota += qt_nota

    print(f"Aluno = {alun} - nota = {nota}")



    print(f'Média da turma é = 'qt_nota)