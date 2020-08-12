"""
    --Erros mais comuns--

#SyntaxeError -> Quando escreve errado

exemplo -1)

    def fun()
        print('AAA')

exemplo -2)

    none = None
    print(none)

    None = none
    print(None)

#NameError -> Quando não se define uma variável

exemplo -1)
    print(nomes)

exemplo - 2)
    a = 5

    if a<10:
        msg = True

    print(msg)      

#TypeError -> Quando uma função/operação/ação é aplicada a um tipo errado

exemplo -1)
    print(len(2))

exemplo -2)
    print('Jorge'+[])

#IndexError -> Quando tentamos acessar um elemento em uma lista ou outro dado indexado utilizando um indice errado

exemplo -1)
    lista = ['Velija']
    print(lista[2])

#ValueError -> Quando recebe um argumento com tipo correto mas valor inapropriado

exemplo -1)
    print(int('Venlafaxina'))

#KeyError -> Quando tentamos acessar um dicionário com uma chav inexistente

exemplo -1)
    dic = {'Num':123}
    print(dic['Xannax'])

#AtributeError -> Quando uma variável não tem um atributo/função

exemplo -1)
    tupla = (1,2,3,4,56,67,78,8)
    print(sort(tupla))

#IndentationError -> Quando não respeitamos os quatro espaços

exemplo -1)
    def fun():
    return('Clo')

exemplo -2)
    for i in range(10000):
    i = i+10
    print(i)
"""

"""
    Raise

Lança execeções, enão é uma função

A forma geral de utilização é:

raise TipoDoErro('mensagem do erro')
"""

def colore(text,cor):
    if type(text) is not str:
        raise TypeError ('NÃO É STRING')
    if type(cor) is not str:
        raise TypeError ('NÃO É STRING')
    print(f'Texto {text}, está na cor {cor}')

colore('ABACAXI','ROGERIO')
#colore('4',4)

"""
    Try & Execpt

utilizamos para tratar erros que podem ocorrer no nosso código. 

a forma geral de se usar é

try:
    //code
except:
    //code
"""
#erro genérico

try:
    gekk()
except:
    print('Num vai rolar')

try:
    len(23)
except:
    print('Num vai rolar')

#erro especifico

try:
    gekk()
except NameError:
    print('Usa uma função certo o corno')

try:
    len(3)
except TypeError as putin:
    print(f'Usa uma função certo o corno, deu o erro {putin}')
    
try:
    #len(832174)
    gekk('AAAAAAAAAAAA')
except NameError as batata:
    print(f'Deu NameError {batata}')

def get_value(dict,key):
    try:
        return dict[key]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'Nome':'Alprazolam'}

print('O Remédio é o ' + get_value(dic,'Nome'))
print(get_value(dic,'Nome_Comercial'))

"""
 Try / Except / Else & Finally
"""

try:
    num = int(input('Fala o número '))
except ValueError:
    print('É UM NÚMERO O ANIMAL')
else:
    print(f'Tá aqui o número {num}')
finally:
    print('O finally é meio sem graça')
#semi-genérico
def dividir(x,y):
    try:  
        return (((int(x) / int(y)) / int(x)) / int(y))
    except ValueError:
            print('N Ú M E R O')
    except ZeroDivisionError:
            print('CÊ QUÉ DIVIDIR POR 0?? QUER APANHAR TAMBÉM??')

num1 = input('Fala o número de X ')
num2 = input('Fala o número de Y ')

print(dividir(num1, num2))

#generico
def dividir(x,y):
    try:  
        return (((int(x) / int(y)) / int(x)) / int(y))
    except:
            print('Quer levar uma cadeirada??')

num1 = input('Fala o número de X ')
num2 = input('Fala o número de Y ')

print(dividir(num1, num2))

#brabo
def dividir(x,y):
    try:  
        return (((int(x) / int(y)) / int(x)) / int(y))
    except(ValueError, ZeroDivisionError) as erro:
            print(f'PUTA QUE PARIU VELHO, deu isso {erro}')

num1 = input('Fala o número de X ')
num2 = input('Fala o número de Y ')

print(dividir(num1, num2))

"""
    Debugando com Python Debugger
     
"""
import pdb

def dividir(x,y):
    try:  
        return (((int(x) / int(y)) / int(x)) / int(y))
    except(ValueError, ZeroDivisionError) as erro:
            print(f'PUTA QUE PARIU VELHO, deu isso {erro}')
pdb.set_trace()
print(dividir(123213,12312324))

