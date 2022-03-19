sexo = input("Digite M ou F: ")

while(not(sexo == "M" or sexo == "F")):
    print("Entrada inválida! Tente novamente!")
    sexo = input("Digite M ou F: ")
    
if(sexo == "M"):
    print("Homem")
else:
    print("Mulher")