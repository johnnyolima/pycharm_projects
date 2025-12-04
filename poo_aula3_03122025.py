from poo_aula1 import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, sexo, matricula):
        super().__init__(nome, data_nascimento, sexo)
        self.matricula = matricula

aluno1 = Aluno("Johnny Lima","01/07/1988", "Masculino", "2021001")

print(aluno1.nome)
print(aluno1.data_nascimento)
print(aluno1.sexo)
print(aluno1.matricula)