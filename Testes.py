"""
    Por que testar nosso código?
        - Reduzir bugs
        - Garantem que novos recursos da sua aplicação não quebren/alterem recursos antigos
        - Garantem que bugs que foram corrigidos, continuen corrigidos
        - Garantem que a refatoração que costumamos a fazer, não tragam novos bugs

TDD - Test Driven Development (Desenvolvimento Guiado por testes)
é utilizado estágios de desenvolvimeto
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')
felix.miar()
print(felix.nome)

"""
    Assertions
"""

def soma_num_positivos(a, b):
    assert a > 0 and b > 0, 'Tem que ser postivo o anta'
    return a + b

#ret = soma_num_positivos(-1,3)
#print(ret)
ret = soma_num_positivos(1,3)
print(ret)

def nume(num):
    assert num in [1,2,3,4,5], 'O numero tem que estar na lista'
    return f'Seu numero é {num}'

numero = input('Fala um numero ae pro pai ')
print(nume(int(numero)))

"""
    Doctests
    
    python -m doctest -v Testes.py
"""
def soma(a, b):
    """
        Vai somar a e b
        >>> soma(90,10)
        100
        >>> soma(80,10)
        90
        >>> soma(10,10)
        20
    """
    return a + b

print(soma(3,4))

def duplicar(valores):
    """
        Duplica valores em uma lista

        >>> duplicar([1,2,3,4,5])
        [2, 4, 6, 8, 10]

        >>> duplicar(['a','b','c'])
        ['aa', 'bb', 'cc']

        >>> duplicar([True, None])
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

        >>> duplicar([])
        []
    """
    return [2*i for i in valores]

"""
    Intro Unittest
    
"""

import unittest

def comer(comida, saudavel):
    if saudavel:
        return 'É Saudavel'
    else:
        return 'Não é saudavél'

def dormir(num_de_horas):
    if num_de_horas < 8:
        return 'Durmi mui pouco'
    else:
       return 'Durmi muito'

def is_funny(pessoa):
    comediantes = ['Nando Viana', 'Luca Mendes', 'Adam Sandler', 'Didi']
    if pessoa in comediantes:
        return True
    else:
        return False

class TesteFuncao(unittest.TestCase):
    def test_comer(self):
        self.assertEqual(
            comer('cenoura', True),
            'É Saudavel'
        )
    def test_comida_brava(self):
        self.assertEqual(
            comer(comida='Pizza', saudavel=False),
            'Não é saudavél'
        )
    def test_domir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Durmi mui pouco'
        )

    def test_domir_muito(self):
        self.assertEqual(
           dormir(10),
            'Durmi muito'
        )

    def test_engra(self):
        self.assertEqual(
            is_funny('Didi'), True
        )
        self.assertTrue(is_funny('Didi'))
        self.assertTrue(is_funny('Adam Sandler'))
#        self.assertFalse(is_funny('Luca Mendes'), 'Deveria ser.')

"""
    Antes e após hooks
"""

class TesteGato(unittest.TestCase):

    def gato_esta_miando(self):
        jordisnei = Gato('Jordisney')
        jordisnei.miar()
        self.assertEqual(jordisnei.miar())

if __name__ == '__main__':
    unittest.main()
