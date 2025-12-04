pessoas = [
    {"nome": "Maria", "idade": 30},
    {"nome": "Johnny", "idade": 45},
    {"nome": "Josiane", "idade": 50},
    {"nome": "Carlos", "idade": 38},
    {"nome": "Diego", "idade": 17}
]
for pessoa in pessoas:
        nome = pessoa["nome"]
        idade = pessoa["idade"]
        print(f"Nome = {nome}, Idade = {idade}")