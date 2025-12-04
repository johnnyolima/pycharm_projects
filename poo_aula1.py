# Definição da classe Pessoa (Modelo/Blueprint)
# Em POO, a classe define as características e comportamentos de um tipo de objeto.
class Pessoa:

    # Método construtor (__init__)
    # É executado automaticamente quando um objeto da classe é criado.
    # Serve para inicializar os atributos do objeto.
    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome  # Atributo de instância
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    # Método da classe
    # Representa um comportamento (ação) que o objeto pode realizar.
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")


# Criação de objetos (instâncias) da classe Pessoa
# Cada objeto possui seus próprios dados, mas compartilha a estrutura definida na classe.
pessoa1 = Pessoa("José", "20/10/2025", "masculino")
pessoa2 = Pessoa("Maria", "20/10/2025", "feminino")

# Acesso aos atributos dos objetos
print("Nome:", pessoa1.nome, "Data de Nascimento:", pessoa1.data_nascimento)
print("Nome:", pessoa2.nome, "Data de Nascimento:", pessoa2.data_nascimento)
