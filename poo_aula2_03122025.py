from poo_aula1 import Pessoa
def cadastrar():
    nome = input("Digite o Nome: ")
    dnasc = input("Digite a data de nascimento: ")
    sexo = input("Digite o Sexo: ")
    pessoa = Pessoa(nome, dnasc, sexo)
    print("Nome: ", pessoa.nome, "data de Nascimento: ", pessoa.data_nascimento)

resp = "s"
while resp=="s":
    cadastrar()
    resp = input("Deseja continuar? ")