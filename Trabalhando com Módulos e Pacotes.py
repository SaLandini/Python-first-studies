"""
    Modulo Random e o que são modulos?

- São outros arquivos em Python

existem duas forma de uso:

1- importando tudo

import random

2 - importando apenas a função a ser utilizada

from random import random, weibullvariate
"""
from random import random, uniform, randint, choice, shuffle

for i in range(13):
    print(random())

for i in range(312):
    print(uniform(1, 354546))

for i in range(6):
    print(randint(1,61), end=', ')

jogadas = ['pedras','papel','tesoura']
print(choice(jogadas))

print(choice('Rivotril'))

cartas = ['K','Q','J','A','2','3','4','5','6','7']

print(cartas)
shuffle(cartas)

print(cartas.pop())

print(cartas)
shuffle(cartas)

print(cartas)

"""
    Built-In
"""

import random as aleatório

print(aleatório.weibullvariate(12,43))

#----

from random import *

print(random())

from random import randint as inteiro_aleatório
print(inteiro_aleatório(12, 89))

from random import (
    random,
    randint,
    weibullvariate,
    choice,
    shuffle)

print(random())
print(randint(1,4))
print(weibullvariate(1,3))

"""
    Módulos customizados
"""
from Funções import stephen_blackhole as discurso

print(discurso())

"""
    Instalando e usando modulos externos
    pip install <name_package>
"""
from colorama import Fore
print(Fore.CYAN + discurso())

"""
    Pacotes

É um diretório contendo uma coleção de módulos
"""

from Alprazolam import (
    frontal,
    xanax
)
from Alprazolam.benzos import (
    rivotril,
    diazepam
)

print(frontal.pesologia)
print(frontal.fun1(1,5297869287345))

print(xanax.constante)
print(xanax.fun2())

print(diazepam.fun4())
print(rivotril.fun3())

"""
    Dunder Main & Dunder Name
 
 Dunder Main -> __main__
 Dunder Name -> __name__
 
 são usados os dunder para criar funções, atributos, propriedades e etc, para não gerar confilto com o nomes
 desses elementos na programação.
"""

import Alprazolam.benzos.rivotril
