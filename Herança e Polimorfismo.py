"""
    Herança
    (Inheritance)

A ideia de herança é a de reaproveitar  codigo. támbem para exetender nossas classes
"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Criente(Pessoa):
    """Herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome,sobrenome,cpf)
        self.__renda = renda

    def nome_completo(self):
        print(super().nome_completo())
        return f'Cliente: {self._Pessoa__nome} {self._Pessoa__sobrenome}, Renda: {self.__renda}'

class Funcionario(Pessoa):
    """Herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Nome: {self._Pessoa__nome} {self._Pessoa__sobrenome}, Funcionário: {self.__matricula}'


crien = Criente('Jorge','Ricardo', '123.432.123-00', 9900)
funcio = Funcionario('Ricardo', 'Jorge', '312.567.423-00', 143645)

print(crien.nome_completo())
print(funcio.nome_completo())

print(crien.__dict__)
print(funcio.__dict__)

"""
    Pripriedades
"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def valor_total(self):
        return self.__saldo + self.limite

    @limite.setter
    def limite(self, new_limit):
        self.__limite = new_limit

    def extrato(self):
        return f'{self.__titular} seu saldo é de {self.__saldo}'

    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def sacar(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor



conta1 = Conta('Jorge', 2000, 9000)
conta2 = Conta('Joaquim', 9000, 3000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos é {soma}')

print(conta1.__dict__)
conta1.limite = 41829077
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)

"""
    Método Super()
"""
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'Este animal da especie: {self.__especie} faz este som {som}')

class Guaxinim(Animal):

    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        self.__raca = raca

joca = Guaxinim('Joca','Procyon lotor', 'Guaxinim')
joca.faz_som('Katchau')

"""
    Herança Mútipla
"""

# Direta

class Base1:
    pass

class Base2:
    pass

class MultiDireta(Base1, Base2):
    pass

# Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiIndireta(Base3):
    pass

# ----- #

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} nadando está'

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self._Animal__nome} do mar'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} estar a andar'

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self._Animal__nome} da terra'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

baleia = Aquatico('Wallison')
print(baleia.nadar())
print(baleia.cumprimenta())

guaxinim = Terrestre('Geraldo')
print(guaxinim.andar())
print(guaxinim.cumprimenta())

pinguim = Pinguim('Bartolomeu')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimenta())

print(f'Bartolomeu é instancia de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Bartolomeu é instancia de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'Bartolomeu é instancia de Terrestre? {isinstance(pinguim, Terrestre)}')
print(f'Bartolomeu é instancia de Animal? {isinstance(pinguim, Animal)}')
print(f'Bartolomeu é instancia de Object? {isinstance(pinguim, object)}')

"""
    MRO - Method Resolution Order 
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} nadando está'

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self._Animal__nome} do mar'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} estar a andar'

    def cumprimenta(self):
        return f'Opa, bom? eu sou o {self._Animal__nome} da terra'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

pinguim = Pinguim('Bartolomeu')
print(pinguim.cumprimenta())

"""
    Polimorfismo
"""


class Animalia(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('É a classe filha que precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo')

class AuAu(Animalia):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animalia__nome} fala au au')

class Gatinho(Animalia):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animalia__nome} fala miau miua')

class Ratinho(Animalia):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animalia__nome} fala: Eai mano, blz?')

felix = Gatinho('Felix')
felix.comer()
felix.falar()

rex = AuAu('Rex')
rex.falar()
rex.comer()

rito = Ratinho('Rito')
rito.comer()
rito.falar()

"""
    Métodos Mágicos

São todos os métodos que usam dunder.
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
       return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        return (f'O livro {self.titulo} do autor {self.autor} foi apagado')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return  'Num vai rolar'

livro1 = Livro('Hamlet','W. Shakespere', 109)
livro2 = Livro('Endurance','Scott Kelly', 390)

print(livro1)
print(livro2)

print(repr(livro1))
print(repr(livro2))

print(len(livro1))
print(len(livro2))

print(livro2 + livro1)

print(livro1 * 10)
print(livro2 * 10)
