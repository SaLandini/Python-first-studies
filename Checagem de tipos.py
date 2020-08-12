class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Geeek University'
lista = [1,2,34,5465]
dicio = {'a':'a','b':'b'}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 43
peso = 8.2


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Joca'))


def cabecalho(texto: str, alinha: bool = True) -> str:
    if alinha:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')


print(cabecalho('Stephen Hawking'))
print(cabecalho('Stephen Hawking', alinha=False))


import math


def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circuferencia(12))
print(circuferencia.__annotations__)

nome: str = 'Joreg'
peso: float = 34.2
ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)


class Pessoa:

    def __init__(self, nome: str, peso: float = 34.2) -> None:
        self.__nome: str = nome
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Jprfe', peso= 234.3)
print(p.andar())
print(p.__dict__)
print(p.andar.__annotations__)
print(p.__init__.__annotations__)

def circuferencia(raio):
    #type: (float) -> float
    return 2 * math.pi * raio

print(circuferencia(12))
#print(circuferencia('geek'))

