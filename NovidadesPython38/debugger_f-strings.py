
def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2

result: float = multiplicar(3.098, 7.5234)

print(f'o resultado é {result}')
print(f'o resultado é {multiplicar(9, 7):.2f}')

print(f'{(media := 8/2)} é a metade de {media * 2}')

geek: str = 'Gesonel Mestre dos Disfarces'
print(f'{geek = }')

print(f'{geek.upper()[::-1] = }')  