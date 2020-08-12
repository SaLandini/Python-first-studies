
isso_ae = 1542603798

"""
Definição da função
"""
if isso_ae != 1542603798:
    cores = ['verde','azul','ermelho','aaaaaaaaa']
    print(cores)

    cores.append('parallax')
    print(cores)

    cores.clear()
    print(cores)

    print(help(print))

    def top():
        print('top!')

    top()

    def stephen_blackhole():
        texto = """A mensagem desta palestra é que buracos negros não são tão negros quanto se pensa.
            Eles não são as prisões eternas que um dia se acreditou que fossem.
            As coisas podem sair de um buraco negro tanto pelo lado de fora e possivelmente para outro universo.
            Então se você sente que está em um buraco negro, não desista – existe um caminho de saída"""
        print(texto)

    stephen_blackhole()

    bulacos_neglos = stephen_blackhole
    bulacos_neglos()
"""
Função com retorno
"""
if isso_ae != 1542603798:
    def quadrado_de_321():
        return 321*321

    ret = quadrado_de_321()

    print(f'Retorno {ret}')
    print(f'Retorno:{quadrado_de_321()}')

    def kkk():
        return ('retornado')

    o_que = 'O que foi '
    print(o_que + kkk())

    def f():
        print('f antes do return')
        return ('f')
        print('f depois do return')
    f()

    def new_year():
        var = True
        if var:
            return 3542089797238564790890238678789032624789023642546789037890324269703245697324572349867324908
        elif var is None:
            return 164-37
        return 532987923485793846**3425
    print(new_year())

    def old_year():
        return 2,67,34,65,423
    num1, num2, num3, num4, num5 = old_year()
    print(num1, num2, num3, num4, num5)

    from random import  random
    def plot_twist():
        if random() > 0.5:
            return True
        return 'True, por essa você não esperava'
    print(plot_twist())
"""
Funções com parametro
"""
if isso_ae != 1542603798:

    def L(na):
        return na**5555
    print(L(5))

    def N(a,b,e):
        return (a+b)/e
    print(N(123,3425,6435))

    def J(hg,asd,sda):
        return ((hg+sda)/asd)*sda
    print(J(21,12,14))

    def Jorge(string1,string2):
        return f'o Jorge é {string1} e {string2}'
    print(Jorge('gkfshjdj','lkfsahdjd'))

    print(Jorge(string1='aaaaaaa',string2='bbbbbbbb'))

    ### Parametro padrão (Default Parameters)

    def exp(numero,potencia):
        return numero ** potencia

    print(exp(21,45))
    print(exp(8,2))

    def exp(numero,potencia=2):
            return numero ** potencia
    
    print(exp(21,4))
    print(exp(8))

    def exp(potencia, numero=3):
            return numero ** potencia
    
    print(exp(21,4))
    print(exp(8))

    def exp(potencia=2, numero=3):
            return numero ** potencia
    
    print(exp(21,4))
    print(exp(8))
    print(exp())

    def monstra_inf(nome='Jorge', estudante=False):
        if nome == 'Jorge' and estudante:
            return 'Ola Jorge, beleza?'
        elif nome == 'Jorge':
            return 'Pensei que era o estudante'
        return f'Ola {nome}'

    print(monstra_inf())
    print(monstra_inf(estudante=True))
    print(monstra_inf('Ricardo'))
    print(monstra_inf(nome='Elizabeth'))

    def soma(n1, n2):
        return n1 + n2

    def mat(n1, n2, fun=soma):
        return fun(n1,n2)

    def subtração(n1, n2):
        return n1 - n2

    print(mat(34,4))
    print(mat(34, 35, subtração))

    estudante = 'Rafaelle'

    def diz_oi():
        estudante = 'Lisa'
        return f'oi {estudante}'

    print(diz_oi())

    total = 0

    def incre():
        global total
        total = total+1
        return total
    
    print(incre())
    print(incre())
    print(incre())
    print(incre())
    print(incre())
    print(incre())

    def fora():
        contador = 0

        def dentro():
            nonlocal contador
            contador = contador + 1
            return contador
        return dentro()

    print(fora())
    print(fora())
    print(fora())
    print(fora())
"""
Documentando funções com Docstrings
"""
if isso_ae != 1542603798:
    """
    isso é uma Docstrings
    """

    def diz_oi():
        """ Uma simples função que diz 'oi!'."""
        return 'oi!'

    print(diz_oi())
    print(help(diz_oi))

    def expo(numero, potencia=2):
        """
        faz a seguinte conta " n^P "
        """
        return numero ** potencia
    print(expo(32))
    print(help(expo))
"""
 *args
"""
if isso_ae != 1542603798:
    """
    é um parâmetro igual qualquer outro, pode chamar de qualquer outra deste que tenha *

    o parametro *args coloca os valores exteras informados como entrada em uma tupla, logo são imutáveis.

    """

    def somatudo(*args):
        total = 0
        for i in args:
            total = total+i
        return total

    print(somatudo())
    print(somatudo(1))
    print(somatudo(1,3))
    print(somatudo(1,34,54))
    print(somatudo(1,4,3,5))
    print(somatudo(1,3,5,7,5))
    print(somatudo(1,7,3,5,7,6))
    print(somatudo(12,45,764,567,34,654,5))
    print(somatudo(56,23,56,213,76,3,65,3))
    print(somatudo(867,32,5,3,562,356,4))

    def somatudo(*args):
        return sum(args)

    print(somatudo())
    print(somatudo(1))
    print(somatudo(1,3))
    print(somatudo(1,34,54))
    print(somatudo(1,4,3,5))
    print(somatudo(1,3,5,7,5))
    print(somatudo(1,7,3,5,7,6))
    print(somatudo(12,45,764,567,34,654,5))
    print(somatudo(56,23,56,213,76,3,65,3))
    print(somatudo(867.2,32.43,5.345,3.6354,562.634,356.4653,4.3546))

    def jaspion(nome, sobrenome, *args):
        return sum(args)
    
    print(jaspion('Elisa', 'Morgetti'))
    print(jaspion('Elisa', 'Morgetti',2,3))
    print(jaspion('Elisa', 'Morgetti',4,5))
    print(jaspion('Elisa', 'Morgetti',6,4))
    
    def veracidade_info(*args):
        if 'Geek' in args and 'University' in args:
            return 'Bem-vindo Geek'
        return 'Quem és tú?'
        
    print(veracidade_info('Geek', 'University'))
    print(veracidade_info('Concorrencia'))
    print(veracidade_info('Geek',123123, 'University'))
    print(veracidade_info( ))
    print(veracidade_info('University'))

    def somaALL(*args):
        return sum(args)

    print(somaALL(23,23))
    print(somaALL(23,23,4,456,324,5,46,456,345,345,34,5,3))

    num = [21,32,45,45,654,5,6,576,67,4,56,4,5]

    print(somaALL(*num)) 
    """o '*' serve para que informemos que terá que desempacotar os dados """
"""
 **kwargs
"""
if isso_ae == 1542603798:
    """
    **kwargs

    exige que usamos parametros nomeados, e transforma em um dicionário
    """

    def cores_fav(**kwargs):
        for p, c in kwargs.items():
            print(f'A cor de {p.title()} é {c}')

    cores_fav(p1 = 'azul', p2 = 'amarelo', p3 = 'vermelho', p4 = 'cinza')
    cores_fav()
    cores_fav( jorge = 'Preto e Vermelho', ricard = 'azul')

    def cumpri_esp(**kwargs):
        if 'geek' in kwargs and kwargs['geek'] == 'Python':
            return 'Você recebeu um comprimento Pythonico'
        elif 'geek' in kwargs:
            return f'{kwargs["geek"]} Geek!'
        return 'Quem és Tú?'

    print(cumpri_esp())
    print(cumpri_esp(geek='Python'))
    print(cumpri_esp(geek='oi'))
    print(cumpri_esp(geek='jedaI'))

    """
    Temos que ter nessa ordem:
    1- Parâmetros obrigatórios
    2- *args
    3- Parâmetros default(não obrigatórios)
    4- **kwargs
    """

    def minha_funcao(num,nome,*args,solteiro=False,**kwargs):
        print(f'{nome} com {num} anos')
        print(args)
        if solteiro:
            print('Solteiro')
        else:
            print('Casado')
        print(kwargs)

    minha_funcao(9, 'Kaio' )
    minha_funcao(12, 'Lysa',43 ,34 ,54, solteiro=True)
    minha_funcao(209, 'Lorgi', eu='não', voce='vai')
    minha_funcao(90, 'Gionio', 34, 45, 64, 76, java=False,python=True )

    def show_names(**kwargs):
        return f"{kwargs['nome']} {kwargs['sobrenome']}"

    nomes = {'nome':'Ricardo','sobrenome':'Falabela'}
    print(show_names(**nomes))

    def soma_muita_coisa(a,b,c, **kwargs):
        print(a+b+c)

    list = [43124,321423412341234,1234123412341234]
    tupla = (43124,321423412341234,1234123412341234)
    conj = {43124,321423412341234,1234123412341234}
    dicio = dict(a=1, b=43523452345, c=1322152345124512, nome='Jorge')


    soma_muita_coisa(*list)
    soma_muita_coisa(*tupla)
    soma_muita_coisa(*conj)
    soma_muita_coisa(**dicio)
    soma_muita_coisa(**dicio, lang='Python')

def stephen_blackhole():
    texto = """A mensagem desta palestra é que buracos negros não são tão negros quanto se pensa.
        Eles não são as prisões eternas que um dia se acreditou que fossem.
        As coisas podem sair de um buraco negro tanto pelo lado de fora e possivelmente para outro universo.
        Então se você sente que está em um buraco negro, não desista – existe um caminho de saída"""
    return (texto)

stephen_blackhole()