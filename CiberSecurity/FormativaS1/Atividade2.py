materiais = {}
materiais_2 = {}

n = 0

while True:
    n+=1

    chave = int(input("Codigo: "))
    valor = str(input('Nome do material: '))

    materiais[chave] = valor

    if n == 3:
        break

print("os materias adicionados no Dicionario são:")   

for chave, valor in materiais.items():  
    print(f"Código: {chave}, Item: {valor}")