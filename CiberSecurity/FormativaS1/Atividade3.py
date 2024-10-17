dados = []
alunos = {}
n=0

while True:
    n+=1
    print("Informe os dados do estudante")
    print('--'*15)

    nome = str(input("Nome do estudante:"))
    sobrenome = str(input("Sobrenome do estudante:"))
    email = str(input("Email do estudante:"))

    dados.extend([nome,sobrenome,email])
    alunos [n] = dados

    continuar = str(input('Deseja adiconar outro aluno? (S/N)')).upper()
    if continuar == 'N':
        print('--'*15)
        break

print(alunos)
print('--'*15)
