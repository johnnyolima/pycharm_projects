from AulaProduto1 import Produto
def cadastrar():
    cod = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")
    tamanho = input("Digite o tamanho: ")
    preco = float(input("Digite o preço: "))

    return Produto(cod, nome, descricao, tamanho, preco)

produto = cadastrar()

print(f"Código: {produto.codproduto}")
print(f"Nome: {produto.nome}")
print(f"Descrição: {produto.descricao}")
print(f"Tamanho: {produto.tamanho}")
print(f"Preço original: R$ {produto.preco:.2f}")
print(f"Preço com 10% de desconto: R$ {produto.desconto():.2f}")