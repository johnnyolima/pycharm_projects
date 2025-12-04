produtos = [
    {"produto": "Tv 50 poleg.", "marca": "Samsung"},
    {"produto": "micro-ondas", "marca": "Panasonic"},
    {"produto": "Iphone 15", "marca": "Apple"},
    {"produto": "Redmi Note 13", "marca": "Xiaomi"},
    {"produto": "Lavadora 10kg", "marca": "Brastemp"}
]

for produto in produtos:
        prod = produto["produto"]
        marca = produto["marca"]
        print(f"Produto = {prod}, Marca = {marca}")