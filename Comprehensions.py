
jooj = 124332
 
"""
List Comprehensions, Parte 1 e 2
"""
if jooj != 124332:
    
    """
    - utlizando list comprehensions nós podemos gerar novas listas com dados processados a partir de outro
    """
    numeros = [1,2,3,4,5,6,7,8,9]

    res = [i * 10 for i in numeros]
    print(res)

    res = [i / 0.5 for i in numeros]
    print(res)

    def f(valor):
        return valor * valor

    res = [f(i) for i in numeros]
    print(res)

    num = [1,2,3,4,5,6,8,9,10]
    num_dobrado = []

    num_dobrado = [i * 2 for i in numeros]
    print(num_dobrado)

    nome = 'Jorge Ricardo'
    print([i.upper() for i in nome])



    def caixa_alta(i):
        i = i.replace(i[0], i[0].upper())
        return i

    amigos = ['jorge', 'ricado', 'levi', 'scharz', 'årge', 'strøng']
    print([caixa_alta(i) for i in amigos])


    print([i*9 for i in range(1,10)])

    print([bool(i) for i in [0,[],'',True,1,23,4,False]])

    print([str(i) for i in [1,2,3,4,5,6,7,8,9]])

    #parte 2

    nume = [1,2,3,4,5,6,7,8,9,10]

    pares = [i for i in nume if i % 2 == 0]
    impares = [i for i in nume if i % 2 != 0] 

    print(nume)
    print(pares)
    print(impares)

    pare = [i for i in nume if not i % 2]
    impare = [i for i in nume if i % 2]
    print(pare)
    print(impare)

    res = [i * 2 if i % 2 == 0 else i / 2 for i in nume]
    print(res)
"""
Linhas aninhadas (Nested Lists)
"""
if jooj != 124332:
    """
    algumas liguagens de programação possuem uma estrutura de dados chamados de arrays
        -Unidimensionais (Arrays/Vetores);
        -Multidimensionais (Matrizes);
    """
    lista = [[1,2,3], [4,5,6], [7,8,9]]
    print(lista)

    print(lista[0])
    print(lista[2][2])
    print(lista[2][-2])

    for L in lista:
        for N in L:
            print(N)
    
    [[print(N) for N in L] for L in lista]

    tabuleiro = [[i for i in range(1,9)] for v in range(1,9)]
    print(tabuleiro)

    velha = [['X' if i % 2 == 0 else 'O' for i in range(1,4)] for valor in range(1,4)]
    print(velha)

    print([['*' for i in range(1,4)] for j in range(1,4)])

"""
Dicionary Comprehension
"""
if jooj != 124332:
    
    numd = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5} 
    quadrado = {c:v ** 2 for c, v in numd.items()}
    print(numd)
    print(quadrado)

    numeros = [1,2,3,4,5,6,7,8,9,10]
    quadrado = {v:v **2 for v in numeros}
    print(numeros)
    print(quadrado)

    chaves = 'abcdef'
    valores = [1,2,3,4,5,6]

    mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
    print(mistura)

    num = [1,2,3,4,5,6,7,8,9,10,11]

    res = {i: {'par' if i%2 == 0 else 'impar'} for i in num}
    print(res)
"""
Set Comprehension
"""
if jooj == 124332:

    numeros = {num for num in range(1,20)}
    print(numeros)

    numeros = {i ** 32 for i in range(10)}
    print(numeros)

    numeros = {i:i ** 32 for i in range(10)}
    print(numeros)

    letra = {l for l in 'Stronghold'}
    print(letra)