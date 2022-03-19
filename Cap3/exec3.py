dic_aluno = {}

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

dic_aluno["nome"] = nome
dic_aluno["media"] = media

if dic_aluno["media"] >= 60:
    dic_aluno["estado"] = 'AP'
else:
    dic_aluno["estado"] = 'RP'

print(dic_aluno)