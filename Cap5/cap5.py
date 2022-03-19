import pandas as pd
import numpy as np

#Exercício 1:
seriesAno1 = pd.Series({'Java':16.25,'C':16.04,'Python':9.85})
seriesAno2 = pd.Series({'C':16.21,'Python':12.12,'Java':11.68})


#Exercício 2:
print(f"Porcentagem total das linguagens no ano 1: {np.sum(seriesAno1)}%")
print(f"Porcentagem total das linguagens no ano 2: {np.sum(seriesAno2)}%")
print("")

#Exercício 3:
print("Crescimento/Declínio das linguagens:")
print("Valor negativo = Declínio, Valor positivo = Crescimento")
seriesA = seriesAno2 - seriesAno1
print(seriesA)
print("")

#Exercício 4:
print("Linguagens que obtiveram crescimento:")
seriesAux = seriesAno2-seriesAno1[(seriesAno2-seriesAno1) > 0]
print(seriesAux.dropna())
print("")

#Exercício 5:
seriesB = seriesA + seriesA + seriesAno2
print(seriesB)
