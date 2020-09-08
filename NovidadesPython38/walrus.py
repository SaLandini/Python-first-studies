"""
permite fazer a atribuição e retorno de valor em uma única expressão
"""

nome = "Gesonel Mestre dos disfarces"
print(nome)

print(nome := 'Gesonel')


"""
cesta = []
fruta = input('Fala a fruta: ')
while fruta != 'Uva':
    cesta.append(fruta)
    fruta = input('Fala a fruta: ')
"""

cesta = []

while (fruta := input(' Fala a fruta: ')) != 'uva':
    cesta.append(fruta)