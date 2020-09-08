"""
    Função de maior Grandeza - Higher Order Function - HOF

- Quando uma linguagem de programação suportaHOF, indica que podemos ter
funções que retornam outras funções como resultado ou mesmo que podemos passar
funções como argumenstos para outras funções.
"""

def somar(a, b):
    return a + b

def subtra(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1,num2)

print(calcular(4, 3, somar))
print(calcular(4, 3, subtra))
print(calcular(4, 3, multi))
print(calcular(4, 3, divi))

# Funçoes alinhadas  -  Nested Function / funções dentro de funções
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Fala ','SOME DAQUI ','Opa, Bom?'))
    return humor() + pessoa

print(cumprimento('Jorge'))
print(cumprimento('Rodrigo'))

#retornando funções de outras

def alguma_risada():
    def rir():
        return choice(('kkkkkk','hahahaha','hehe','sdjhasjdhashajdda'))
    return rir
risada = alguma_risada()
print(risada())

def alguma_risada2(pessoa):
    def rir():
        risada1 = choice(('kkkkkk','hahahaha','hehe','sdjhasjdhashajdda'))
        return f'{risada1} {pessoa}'
    return rir
risada = alguma_risada2('Jorge')
print(risada())
print(risada())
print(risada())
print(risada())

"""
    Decoradores

O que são os decorators?

-são funções
-eles envolvem outras funções e aprimoram seus comportamentos
"""

def be_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um bom dia')
    return sendo

def saudacao():
    print('Bem Vindo')

teste = be_educado(saudacao)

teste()

# syntax sugar, forma recomendada

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um bom dia')
    return sendo

@seja_educado
def apresentando():
    print('Meu nome é Joca')

apresentando()

@seja_educado
def sleep():
    print('Eu estou com sono, vou apagar aqui, tchau')

sleep()

"""
   Decorators com diferentes assinaturas
"""

def gritar(função):
    def aumentar(*args, **kwargs):
        return função(*args,**kwargs).upper()
    return aumentar

@gritar
def pedido(principal, acompanhamento):
    return f'Eu queria {principal} acompanhado de {acompanhamento}, por favor meu consagrado'

print(pedido('Picanha','Batata frita com cheddar e bacon'))

@gritar
def indignação():
    return 'quero cafèééééééééeéé  éé'

print(indignação())

def verifica(valor):
    def interna(função):
        def outra (*args, **kwargs):
            if args and args[0] != valor:
                return f'TÁ ERRADO, TEM QUE SER {valor}'
            return função(*args, **kwargs)
        return outra
    return interna

@verifica('Pizza')
def comida(*args):
    print(args)

@verifica(10)
def soma(n, n2):
    return n + n2

print(comida('Pizza', 'Lasanha'))
print(comida('Lasanha'))

print(soma(10,23490))
print(soma(329,10))

"""
    Preservando Metadata com Wraps

"""

def see_log(função):
    def log(*args, **kwargs):
        """Um function inside outra function"""
        print(f'fuction chamada: {função.__name__}')
        print(f'Aqui esta a documentação: {função.__doc__}')
        return função(*args, **kwargs)
    return log

@see_log
def soma(a,b):
    """a+b"""
    return a + b

print(soma(12,48))
print(soma.__name__)
print(soma.__doc__)

from functools import wraps
def see_log(função):
    @wraps(função)
    def log(*args, **kwargs):
        """Um function inside outra function"""
        print(f'fuction chamada: {função.__name__}')
        print(f'Aqui esta a documentação: {função.__doc__}')
        return função(*args, **kwargs)
    return log

@see_log
def soma(a,b):
    """a+b"""
    return a + b

print(soma(12,48))
print(soma.__name__)
print(soma.__doc__)

"""
    Forçando tipos de dados com decoradores
"""

def força_tipos(*tipos):
    def decorador(funcao):
        def converte(*args,**kargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kargs)
        return converte
    return decorador

@força_tipos(str, int)
def repet(msg, vezes):
    for vezes in range(vezes):
        print(msg)

repet('J', '1234')

@força_tipos(float,float)
def dividir(a, b):
    print(a/b)

dividir('12',21341)