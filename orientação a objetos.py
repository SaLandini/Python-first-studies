"""
    Programação Orientada a Objetos

-é um pradigma de programação que utiliza mapeamento de
objetos  do mundo real para modelos computacionais
"""
num = 100

print(num)
print(type(num))

num = '100'

print(num)
print(type(num))

class prod:
    pass

ps4 = prod()

print(ps4)
print(type(ps4))

"""
    Classes
São modelos dos objetos do mundo real sendo representados computacionalmente.
"""

idade = 32
preco = 1243.23
nome = 'Jorge'

print(type(idade))
print(type(preco))
print(type(nome))

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))

"""
    Atributos

Representam as caracteristicas do objeto. Ou seja, pelos atributos, nós conseguimos representar
computacionalmente os estados de um objeto
"""
#Atributos de instância
#Publicos
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

#Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
            print(self.__senha)

    def mostra_email(self):
            print(self.email)
user = Acesso('user@email.com','123342')

print(user.email)
#print(user.senha) #Atribute error
print(dir(user))
print(user._Acesso__senha)
user.mostra_senha()
user.mostra_email()

user1 = Acesso('user@email.com','35487342')
user2 = Acesso('jorge@email.com','123342')

user1.mostra_senha()
user2.mostra_email()

#Atributos de classe

p1 = Produto('Ryzen7', 'Processador', 2900)
p2 = Produto('Ryzen3', 'Processador', 900)

class ProdutoComImposto:

    imposto = 1.05

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoComImposto.imposto)

p1 = ProdutoComImposto('Ryzen7', 'Processador', 2900)
p2 = ProdutoComImposto('Ryzen3', 'Processador', 900)

print(p1.valor)
print(p2.valor)

class ProdutoComImpostoEContador:

    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = ProdutoComImpostoEContador.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoComImpostoEContador.imposto)
        ProdutoComImpostoEContador.contador = self.id

p1 = ProdutoComImpostoEContador('Ryzen7', 'Processador', 2900)
p2 = ProdutoComImpostoEContador('Ryzen3', 'Processador', 900)

print(p1.nome, p1.id)
print(p2.nome, p2.id)

#Atributos Dinâmicos

p3 = Produto('Ryzen7', 'Processador', 2900)
p1.peso = '50g'

print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Preço: {p1.valor}, Peso: {p1.peso}')

print(p2.__dict__)
print(ProdutoComImpostoEContador.__dict__)

print(p1.__dict__)
del p1.peso
print(p1.__dict__)

"""
    Métodos
Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema
"""

class Lampada:

    contador_porta = 0

    def __init__(self, cor, voltagem, luminosidade):
        self.__interruptor = Lampada.contador_porta + 1
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
        Lampada.contador_porta = self.__interruptor


class ProdutoComImpostoEContadorEAgoraDamosDescontos:

    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = ProdutoComImpostoEContadorEAgoraDamosDescontos.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoComImpostoEContadorEAgoraDamosDescontos.imposto)
        ProdutoComImpostoEContadorEAgoraDamosDescontos.contador = self.id

    def desconto(self, porcentagem):
        """Retorna o valor com um desconto"""
        return (self.valor * (100 - porcentagem))/100

p1 = ProdutoComImpostoEContadorEAgoraDamosDescontos('Ryzen7', 'Processador', 2900)
print(p1.desconto(12))

from passlib.hash import pbkdf2_sha256 as cryp

class Acesso:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(cls.contador)

    @classmethod
    def ver(cls):
        print('Aqui é static trouxa')
    def __init__(self, nome, email, senha):
        self.__id = Acesso.contador + 1
        self.nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 2530871, salt_size=10)
        Acesso.contador = self.__id
        print(f'Usuario criado: {self.__gera_user()}')
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_user(self):
        return self.__email.split('@')[0]

user = Acesso('Ricardo','email.com.br','Jorge123')
print(user.checa_senha('Jorge123'))
print(user._Acesso__senha)
Acesso.conta_usuario()
user.conta_usuario()
print(user._Acesso__gera_user)
Acesso.ver()

"""
    Objetos
"""
"""

class Medicamento:

    def __init__(self, dosagem, nome, formula, tarja, receita):
        self.dosagem =  dosagem
        self.nome = nome
        self.formula = formula
        self.tarja = tarja
        self.receita = receita

    def vender(self):
        if self.receita == 'Sim':
            print(f'Ok, vou pegar o {self.nome} de {self.dosagem}mg')
        else:
            print(f'O {self.formula} precisa da receita, volta mais tarde')

    def notinha(self):
        print('Aqui está a notinha:')
        print(f'|Remédio: {self.nome} - {self.formula} de {self.dosagem}mg|')
        print(f'|Tarja: {self.tarja}, tem receita? {self.receita}|')

remedio = input('Qual o remédio? ')
form = input('Sabe a formula? ')
tarja = input('Sabe qual tarja que é? ')
dosagem = input('Quantos mg? ')
receita = input('tem receita? ')

rmedio = Medicamento(dosagem,remedio,form,tarja,receita)
Medicamento.vender(rmedio)
Medicamento.notinha(rmedio)

"""
"""
    Abstração e Encapsulamento
"""

class Conta:

    contador = 300

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}, com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Vai sacar negativo?')
    def sacar(self,valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('CÊ num tem dinheiro carajo')
        else:
            print('Num fode cara')

    def tranferencia(self, valor, conta_final):
        self.__saldo -= valor
        self.__saldo -= valor * 0.02
        conta_final.__saldo += valor

conta1 = Conta('Jorge',2.0,3124)
print(conta1.__dict__)

conta2 = Conta('Ricardo',2321.0,3124)
print(conta2.__dict__)

conta2.tranferencia(213, conta1)
print(conta2.__dict__)
print(conta1.__dict__)