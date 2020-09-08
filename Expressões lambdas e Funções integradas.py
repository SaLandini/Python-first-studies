"""
Filter

Serve para filtrar dados de uma determinada coleção.

recebe dois parametros, uma função e um interavel

assim com no map, após ser utilizado, os dados são excluídos da memória
"""
import statistics

varlores = 1, 2, 3, 4, 5, 6, 7

media = (sum(varlores)/len(varlores))
print(media)

dados = [1, 3,54.3 ,34.5, 564.43, 56.3,56.3,3675.328,4839.49]

media = statistics.mean(dados)
print(f'Média: {media}')

res = filter(lambda x: x> media, dados)
print(list(res))

print(f'Novamente:{list(res)}')

paises = ['', 'argentina','brasil','chile','','colombia','','','venezuela']

res = filter(lambda pais: len(pais)>0, paises)
print(list(res))
res = filter(lambda pais: pais != '', paises)
print(list(res))
res = filter(None, paises)
print(list(res))

usuarios = [
    {'username':'samuel', 'Tweets':['Flask é brabo']},
    {'username':'jorge', 'Tweets':['Cloridrato','venlafaxina']},
    {'username':'joca', 'Tweets':[]},
    {'username':'wesley', 'Tweets':['nego','ney','aaaaaaa']},
    {'username':'ricardo', 'Tweets':[]}
]
print(usuarios)

inativos = list(filter(lambda usuario: len(usuario['Tweets'])==0, usuarios))
print(inativos)

inativos = list(filter(lambda usuario: not usuario['Tweets'], usuarios))
print(inativos)

nomes = ['Vanessa','Ana','Maria','Laura']

instrutoras = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome)<5, nomes)))
print(instrutoras)



"""
Reduce

(A partir do python3, a função reduce não é mais uma função integrada)
"""
from functools import reduce

dados = [2,3,5,7,8,9,56,34,12,7,34,7,9,3,6]

multi = lambda x, y: x* y

res = reduce(multi, dados)
print(res)

res = 1
for i in dados:
    res = res * i

print(res)

"""
Any, All

all() retorna true se todos elementos forem verdadeiros ou se o interável está vazio

any() retorna true se qualquer elemento for verdadeiro, se for vazio, false
"""

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all([]))

nomes = ['Carlos', ' Camila', 'Cassio', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', ' Camila', 'Cassio', 'Wesley']
print(all([nome[0] == 'C' for nome in nomes]))


print(all([num for num in [4,3,2,6,3,54,3,1] if num % 2 ==1]))
print(all([num for num in [4,2,6,54] if num % 2 ==1]))

print(any([True,True,True,False]))
print(any([]))

print(any([nome[0]=='C' for nome in nomes]))

print(any([num for num in [2,4,10,8,6,9] if num % 2 ==0]))


"""
Generators

 tuple comprehensions == generators
"""

nomes = ['Carlos', ' Camila', 'Cassio', 'Wesley']

res = [nome[0] == 'C' for nome in nomes]
print(res)

res = (nome[0] == 'C' for nome in nomes)
print(res)

import sys

print(sys.getsizeof('gekk my friend'))
print(len('gekk my friend'))
print(sys.getsizeof('asjdghasldjghaslkjghasdkghaslkdgalçsdkjfasçdhgasljdhlgjhdaslkjfgasçlkghasljjghaslghasdlkghsalçkkvbndfljbnfasdjhaslçkhfgaowierhfgaçlksdejfaerfij'))
print(len('asjdghasldjghaslkjghasdkghaslkdgalçsdkjfasçdhgasljdhlgjhdaslkjfgasçlkghasljjghaslghasdlkghsalçkkvbndfljbnfasdjhaslçkhfgaowierhfgaçlksdejfaerfij'))

print('Se liga nesses bytes:')

lsit_comp = sys.getsizeof([x * 10 for x in range(1000)])
print(lsit_comp)

set_comp = sys.getsizeof({x * 10 for x in range(1000)})
print(set_comp)

dict_comp = sys.getsizeof({x:x * 10 for x in range(1000)})
print(dict_comp)

gen_comp = sys.getsizeof(x * 10 for x in range(1000))
print(gen_comp)

gen = (x * 10 for x in range(1000))

for i in gen:
    print(i)
"""
Sorted

Podemos usa-lo com qualquer interável, enquanto o .sort() é só pra listas

não é alterado os valores/ordem do interável, ele cria uma lista nova ordenada
"""

num = {2,6,3,86,2,4,67,2,9,54}
print(num)
print(sorted(num))

print(sorted(num, reverse=True))

usuarios = [
    {'username':'samuel', 'Tweets':['Flask é brabo'],'x':'y'},
    {'username':'jorge', 'Tweets':['Cloridrato','venlafaxina']},
    {'username':'joca', 'Tweets':[]},
    {'username':'wesley', 'Tweets':['nego','ney','aaaaaaa'], 'x':'y', 'a':2},
    {'username':'ricardo', 'Tweets':[]}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuarios: usuarios['username']))
print(sorted(usuarios, key=lambda usuarios: usuarios['username'], reverse=True))
print(sorted(usuarios, key=lambda usuarios: len(usuarios['Tweets'])))

"""
Min e Max

max()  => retorna o maior valor

min()  => retorna o menor valor
"""
lista = [352078,438902,28345790906,39254870702986,23490588,23947855,34952788,6095234]
print(max(lista))
print(min(lista))

print(max(3418509707,417098232))
x = int(input('Manda o x:'))
y = int(input('Manda o Y:'))
print(max(x,y))

print(max('ABSJQWLÇKJASÇDMQÇVAXCACØÅÆPØASDØAPÆ'))


print(min(3418509707,417098232))
x = int(input('Manda o x:'))
y = int(input('Manda o Y:'))
print(min(x,y))

print(min('ABSJQWLÇKJASÇDMQÇVAXCACØÅÆPØASDØAPÆ'))

nomes =['Jorge', 'Wesley', 'Costa', 'Murilo', 'Miguel', 'Gabriel']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

print(max(nomes, key=lambda nome: len(nome))[0])
print(min(nomes, key=lambda nome: len(nome))[0])

"""
Reversed

Não confunda com a função reverse(), pois ela funciona só nas listas

sua função é inverter o interavél
"""
lista = [1,2,3,45,6,7,8,9,0]
res = reversed(lista)
print(res)

print(list(reversed(lista)))

for l in reversed('Cloridrato de Clomipramina'):
    print(l, end='')

print(''.join(list(reversed('Cloridrato de Clomipramina'))))

print('Cloridrato de Clomipramina'[::-1])

for n in reversed(range(0,10)):
    print(n)

for n in range(10, -1 , -1):
    print(n)

"""
Len, Abs, Sum & Round

len() -> Retorna o tamonho de um interável

Abs() -> Retorna o valor absoluto de um numero, resumindo = |x|

Sum() -> Retorna a soma total dos valores, incluido o valor default, no caos, 0

Round() -> Retorna um numero arredondado para n digito de precisão
"""

print(len('Cloridrato de Clomipramina'))

print('Cloridrato de Clomipramina'.__len__()) # dunder len

print(abs(-2))
print(abs(2))

print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],139820))

print(sum([1.3435463,9.38247890253709856], 9.3825896709823746))

print(round(0.1840671846719348672039))
print(round(0.840671846719348672039))
print(round(0.1580237344190825709734098157,9))
print(round(0.1580237344190825709734098157,1))

"""
Zip

zip() -> cria um interavel que agrega elemento de cada um dos interáveis passados como entradas em pares
"""

list1 = [1,3,6]
list2 = [2,5,9]

zip1 = zip(list1,list2)
print(list(zip1))

zip2 = zip(list1,list2,'abc','clo')
print(list(zip2))

zip3 = zip(list1,list2)
print(dict(zip3))

zip4 = zip(list1, list2, 'Cloridrato', 'de ', 'Clomipramina')
print(list(zip4))

tupla = 1,2,3,4,5,6,7,8,9
lista = [1,2,3,4,5,6,7,8,9]
set = {1,2,3,4,5,6,7,8,9}

zip5 = zip(tupla,lista,set)
print(list(zip5))

prova1 = [9.0, 7.0, 10.0]
prova2 = [3.0, 4.0, 9.0]
alunos =['Wesley','Gabriel','Miguel']

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos,prova1,prova2)}
print(final)

final = zip(alunos, map(lambda nota:max(nota),zip(prova2,prova1)))
print(dict(final))