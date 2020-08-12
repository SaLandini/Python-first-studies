
JORGE =123

"""
Listas
"""
if JORGE == 123:
    list1 = [18, 9, 6, 3, 21, 15, 0, 12]
    list2 = ['P','h','y','s','i','c','i','s','t']
    list3 = []
    list4 = list("physicist")
    list5 = list(range(0, 100))

    num = 1
    if num in list5:
        print("sim")
    else:
        print("não")

    letra = 'o'
    if letra in list4:
        print("sim")
    else:
        print("não")

    list1.sort()
    print(list1)

    print(list2.count('i'))

    list1.append(99102903912039123910239412848209190238194812948 - 121212)
    print(list1)

    list1.append("Astrophysicist")
    print(list1)
    if ["Astrphysicist"] in list1:
        print("sim")
    else:
        print("não")

    list1.extend(["Astrophysicist", "Neil D. Tyson"])
    print(list1)

    list1.insert(4, "Astrophysicist")
    print(list1)

    list6 = list1 + list2 + list3 + list4 + list5
    print(list6)

    list6.reverse()
    print(list6)

    print(list6[::-1])

    print(len(list6))

    list5.pop(2)
    print(list5)

    list1.clear()
    print(list1)

    nova = [12, 12341, 20392]
    nova = nova*3
    print(nova)

    nova1 = "O que aprendi com hamlet"
    nova1 = nova1.split()
    print(nova1)

    nova1 = "O que aprendi com hamlet"
    nova1 = nova1.split('e')
    print(nova1)

    nova2 = ['O', 'que', 'aprendi', 'com', 'hamlet']
    nova3 = ' '.join(nova2)
    print(nova3)

    nova4 = [1, 0.2831238, True, "Endurance", 'a', [1, 2, 45, 654, 3532453, 675445], 102939128302938109238901283290481209389]
    print(nova4)

    for x in nova4:
        print(x)

    carrinho = []
    produtos = ' '

    while produtos != 'sair':
        print('adicione um produto no carrinho de compras')
        produtos = input()
        if produtos != 'sair':
            carrinho.append(produtos)

    for produtos in carrinho:
        print(produtos)

    v1 = 92391293121923129319231249124981249808752347592345928736459823756327456
    v2 = 12398019028403928409841983209178248759017095613429765123956729083751902
    v3 = 12980312830174912838492222223492034820984028304089509238509235790330275
    v4 = 94892839128398429128349012389018301982309128390183091830123810938407581

    NumberinV = [v1,v2,v3,v4]
    print(NumberinV)
    print(NumberinV[2])
    print(NumberinV[-2])

    for NUM in NumberinV:
        print(NUM)

    indice = 0
    while indice < len(NumberinV):
        print(NumberinV[indice])
        indice = indice+1
    for indice, NUM in enumerate(NumberinV):
        print(indice, NUM)

    Number = [1, 3435, 52, 5653, 123, 12412, 563, 1, 23, 34, 5, 24, 14, 2546, 2, 326, 245, 623, 6324, 5, 34, 5, 2346, 23, 35, 23, 5]
    print(sum(Number))
    print(max(Number))
    print(min(Number))
    print(len(Number))

    ny = [1, 9, 89, 1203, 10293]
    print(ny)

    ny2 = ny.copy()

    print(ny2)

    ny2.append(10239210331123982839213)
    print(ny2)
    print(ny)

    ny = [1, 9, 89, 1203, 10293]
    print(ny)

    ny2 = ny

    print(ny2)

    ny2.append(99999999999999999999999999999999999999999999)
    print(ny2)
    print(ny)
"""
tuplas
"""
if JORGE == 123:
    tupla1 = (1, 4, 76, 3, 543)
    tupla2 = 1, 4, 76, 3, 543
    tupla3 = (3)
    tupla4 =(3,)
    tupla5 = 9230231,
    tupla6 = tuple(range(100))

    print(tupla1)
    print(tupla2)
    print(tupla3)
    print(tupla4)
    print(tupla5)
    print(tupla6)

    print(type(tupla1))
    print(type(tupla2))
    print(type(tupla3))
    print(type(tupla4))
    print(type(tupla5))
    print(type(tupla6))

    T1 = 1, 3, 54, 12

    print(sum(T1))
    print(max(T1))
    print(min(T1))

    tuplinha = tuple([12,34,534,1235,47356])
    print(tuplinha[0])
    print(tuplinha[2])
    print(tuplinha[2:5])
"""
dicionários
"""
if JORGE == 123:
    Dic1 = {123:True, 456:False, 7890:True}
    print(Dic1)
    Dic2 = {'BR':"Brasil",'NO':"Noruega",'RU':"Russía"}
    print(Dic2)

    print(Dic2['RU'])
    print(Dic2['NO'])
    print(Dic2['BR'])

    print(Dic1.get(7890))
    print(Dic1.get(123))
    print(Dic1.get(456))

    print(Dic2.get('USA'))

    Dic2.update({'SE':"Suécia"})
    Dic2.update({'USA':"United States"})
    Dic1.update({123:False})
    print(Dic1)
    print(Dic2)

    Dic2.pop('SE')
    del Dic2['USA']
    print(Dic2)

    Dic3 = Dic2.copy()
    print(Dic2)
    print(Dic3)

    Dic2.clear()
    print(Dic2)
    print(Dic3)

    Dic4 = Dic3.fromkeys({123, 534, 389021},{True ,False ,None})
    print(Dic4)
"""
conjuntos
"""
if JORGE == 123:
    conj = {1,23,45,54,3,5,32,32}
    conju = {3, 12, 54, 21, 345, 1, 4, 5, 6, 45}

    print(conj)
    print(conju)

    conj.add(157230989865140293952041936749356208970)
    print(conj)

    conju.remove(21)
    print(conju)

    conj.discard(142332689235466456275428936345890234589)
    print(conj)

    print(conj.union(conju))
    print(conju|conj)

    print(conju.intersection(conj))
    print(conj&conju)

    print(conju.difference(conj))

    print(conj.symmetric_difference(conju))

    conj1 = {12,453,3564,234,523,564,7564,8,76}
    conj2 = {12,43,654,234,354,756,234,8,76,32,453}
    print(3564 in conj1)
    print(conj2.issubset(conju))
    print(conj.issuperset(conj1))
    print(conju.isdisjoint(conj))
"""
Módulos Collection
"""
if JORGE == 123:
    #Counters
    from collections import Counter

    lista = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,8,8,8,8,8,8,8,8,6,76,6,76,76,676]
    res = Counter(lista)
    print(type(res))
    print(res)

    print(Counter('Paralelepípedo'))

    texto = """A mensagem desta palestra é que buracos negros não são tão negros quanto se pensa.
    Eles não são as prisões eternas que um dia se acreditou que fossem.
    As coisas podem sair de um buraco negro tanto pelo lado de fora e possivelmente para outro universo.
    Então se você sente que está em um buraco negro, não desista – existe um caminho de saída"""
    palavras = texto.split()
    print(texto)
    print(palavras)
    ras = Counter(palavras)
    print(ras)

    print(ras.most_common(2))

    #Default Dict
    from collections import defaultdict

    dicí = defaultdict(lambda: 12390890435)
    dicí['Cosmos'] = 'C.Sagan'
    print(dicí)
    print(dicí['Valor'])
    print(dicí)

    #Ordered Dict
    from collections import OrderedDict

    diciti = OrderedDict({89:1, 94:2, 47835:32, False:8,'aa':6,'9':9})
    for jorge, ricardo in diciti.items():
        print(f'ricardo ={jorge}:jorge ={ricardo}')

    dici1 = {'a':1, 'v':2}
    dici2 = {'v':2,'a':1}
    print(dici1 == dici2)

    dici1 = OrderedDict({'a': 1, 'v': 2})
    dici2 = OrderedDict({'v': 2, 'a': 1})
    print(dici1 == dici2)

    #Named Tupla
    from collections import namedtuple

    CatNot = namedtuple('CatNot','Idade Raça Nome')

    CatNot = namedtuple('CatNot','Idade, Raça, Nome')

    CatNot = namedtuple('CatNot',['Idade','Raça','Nome'])

    ray = CatNot(Idade=32,Raça='AuAu',Nome='Raymond')
    print(ray)
    print(ray[0])
    print(ray[1])
    print(ray[2])

    print(ray.Idade)
    print(ray.Raça)
    print(ray.Nome)

    #Deque
    from collections import deque

    deq = deque('Shazam')
    print(deq)

    deq.append('chorão')
    print(deq)

    deq.appendleft('ninguém perguntou como foi meu dia')
    print(deq)

    print(deq.pop())
    print(deq)

    print(deq.popleft())
    print(deq)

