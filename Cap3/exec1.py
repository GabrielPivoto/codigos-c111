colocados = ['Real Madrid','Liverpool','Bayern','Barcelona','Juventus']
print("Os três primeiros colocados: {}" .format(colocados[:3]))
print("Os dois últimos colocados: {}".format(colocados[3:]))
print("Os colocados em ordem alfabética: {}".format(sorted(colocados)))
print("Posição do Barcelona na colocação: {}".format(colocados.index('Barcelona')+1))
