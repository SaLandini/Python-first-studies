"""
    Entendendo Iterator e Iterables

Iterator -> Um objeto que pode ser iterado.
            Um objetor que retorna um dado, sendo um elemento por vez quando uma função netx() é chamada.

Interable -> Um objeto que irá retornar um iterator quando a função inter() for chamada.
"""

nome = 'Peste'
numeros = [1,2,3,4,5,6,7,8,9,10]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

for i in nome:
    print(i)

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for i in numeros:
    print(i)

"""
    Criando loops
    
"""
def min_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            print("Acabou, vai embora!")
            break

min_for('Cloridrato de Venlafaxina')
lista = [12,34,65,76,87,34,54,23,54,67]
min_for(lista)

"""
    Interador customizado
"""

class Cont:
    def __init__(self, menor,maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Cont(1,90)
print(con.maior)
print(con.menor)
it = iter(con)

for i in Cont(1,90):
    print(i)

"""
    Geradores

Generators são Iterators, mas nem todo Iterators é um Generators

- Podem ser criadas com funções geradoes;
- Funções geradoras utilizam a palavra reservada yield
- Podem ser criados com Expressôes Geradoras

"""
# exemplo de generator function
def conta_ate(v_max):
    contador = 1
    while contador <= v_max:
        yield contador
        contador = contador + 1
# Uma função generator gera um generator e não que ele é um

gen = conta_ate(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(12)
for i in gen:
    print(i)

gen = list(conta_ate(123))
print(gen)

"""
    Teste de Memória com Generators
"""
# usando listas - 400mb de ram
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a,b = b, a+b
    return nums

for i in fib_lista(1000):
    print(i)

# usando função geradores - 3mb de ram

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a+b
        yield a
        contador = contador + 1

for i in fib_gen(100000):
    print(i)

"""
 Teste de velocidade com expressões Geradoras
"""
def nums():
    for num in range(1,10):
        yield num
ge1 = nums()
print(ge1)

ge2 = (i for i in range(1, 10))
print(ge2)

print(sum(i for i in range(1, 10)))

import time

#gen expression
gen_init = time.time()
print(sum(i for i in range(1000000000)))
gen_tempo = time.time() - gen_init

#List Comprehension

list_init = time.time()
print(sum([i for i in range(1000000000)]))
list_tempo = time.time() - list_init

print(f'Gen levou {gen_tempo} pra terminar')
print(f'List Comprehensions levou {list_tempo} pra terminar')