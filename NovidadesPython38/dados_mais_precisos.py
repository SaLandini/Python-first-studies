
def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro('Geek'))

"""
- literal type
- union
- final 
- typed dict
- protocols
"""

from typing import Literal

def pegar_status(usuario: str) -> Literal['Conectado', 'Desconectado']:
    pass

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação invalida {operacao!r}')

calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
#calcula_v1('*', 6, 4)

def calcula_v2(operacao: Literal['+','-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação invalida {operacao!r}')

calcula_v2('+', 6, 4)
calcula_v2('-', 6, 4)
#calcula_v2('*', 6, 4)

from typing import Union

def soma(num1: int, num2: int) ->Union[str, int]:
    resultado = num1+num2

    if resultado > 50:
        return 'é um valor muito grande'
    else:
        return resultado

print(soma(4,10))

from typing import Final

Nome: Final = 'Gekk'
print(Nome)

from typing import final

@final
class pessoa:
    pass

class estudante(pessoa):
    pass

    @final
    def estudar(self):
        print('Estudando eu estou')

class estagiario(estudante):
    pass

    def estudar(self):
        print('O estagiario está estudando')

from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

print( geek := CursoPython(versao='3.8.5', atualizacao=2020))
print( outro := CursoPython(versao='Linux Python', atualizacao=3))

from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar (valor: Curso) -> None:
    print(f'Estou fazendo o curso {valor.titulo}')

class Venda:
    titulo = 'oi'

v1 = Venda()
c1 = Curso()
c1.titulo = 'Programação em python'

estudar(c1)
estudar(v1)