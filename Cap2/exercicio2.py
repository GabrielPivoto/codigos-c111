op = int(input("Digite o número: "))
inicio = int(input("Digite de onde deseja iniciar: "))
fim = int(input("Digite de onde deseja parar: "))

for i in range(inicio,fim+1):
    print("{} * {} = {}".format(op,i,op*i))