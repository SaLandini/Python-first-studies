
valor = '67.9'
print(float(valor))

def cumprimenta_v1(nome):
    return f'Fala {nome}'

print(cumprimenta_v1('jorge'))
print(cumprimenta_v1(nome='jorfe'))

def cumprimenta_v2(nome, /):
    return f'Fala {nome}'

print(cumprimenta_v2('jorge'))
#print(cumprimenta_v2(nome='jorfe'))

def cumprimenta_v3(nome, /, mensagem="Ola"):
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Ricardo', mensagem='Tchau'))

def cumprimenta_v4(nome, mensagem="Ola", /):
    return f'{mensagem} {nome}'

print(cumprimenta_v4('jorge', 'ola'))

def cumprimenta_v5(*, nome):
    return f'Ola {nome}'

print(cumprimenta_v5(nome='jorge'))
