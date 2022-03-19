loja1 = {'Galaxy S21', 'iPhone 12', 'Redmi 9', 'Galaxy A7', 'Zenfone 5', 'iPhone 11'}
loja2 = {'Galaxy A7', 'iPhone 10', 'Zenfone 4', 'iPhone 12', 'Redmi Note', 'Zenfone 3'}

print("É possível comprar os modelos: {}".format(loja1|loja2))
print("Estão disponíveis em ambas as lojas: {}".format(loja1&loja2))