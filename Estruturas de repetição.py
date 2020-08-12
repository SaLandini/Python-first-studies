
#For String

name = "Gesonel Mestre dos Disfarces"

for letter in name:
    print(letter)
for _, letter in enumerate(name):
    print(name)
for valor in enumerate(name):
    print(valor)
for valor in enumerate(name):
    print(valor[0])
for valor in enumerate(name):
    print(valor[1])

#For List

list = [1.923, 2.30403, 2 - 3, 0.999999999999999]

for number in list:
    print(number)

# For  Range

number = range(0, 15)

for number in range(0, 15):
    print(number, end=' ')

times = int(input('how many time you want to see that code?'))
add = 0
for n in range(1, times+1):
    num = int(input(f'quer somar {n}/{times} valor: '))
    add = add + num
print(f'a soma é {add}')

#	U+1F320
#	U0001F320

emoji = 'U0001F320'
for _ in range(1):
    for num in range(1, 12):
        print('\U0001F320'* num)

for num in range(999, 9999):
    print(num)

for num in range(98, 2935, 98):
    print(num)

for num in range(23674393, -23674393, -999):
    print(num)

number = 9990

while number < 10000:
    print(number)
    number = number + 1

argument = ' '

while argument != 'Abaixo a Opressão':
   argument = input('Me dê um argumento valido')

for number in range (9, 99999999999999999999999999999999999999):
    if number == 999999:
        break
    else:
        print(number)

print("o codigo foi forçado a parar")

while True:
    comando = input('digite"sair"para parar o codigo')
    if comando == 'sair':
        break

print("o codigo foi forçado a parar")