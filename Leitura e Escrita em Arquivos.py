
"""
 Leitura de Arquivo

Para fazer a leitura do arquivo usamos a função open()
A gente passa o caminho ou o nome do arquivo que vamos abrir. É retornado um _io.TextIOWrapper
a função open serve apenas para fazer a leitura de um arquivo

Usamos o read() para realmente ler o arquivo

Depois de trabalhar com o arquivo, devemos fechar o arquivo, usando o close()
"""

arquivo = open('text.txt')
print(arquivo)
print(type(arquivo))

ret = arquivo.read()
print(ret)
print(type(ret))

"""
    Seek e Cursors
    
seek() é utilizada para mover o cursor pelo arquivo
"""

arquivo.seek(0)
print(ret)

arquivo.seek(22)
print(ret)

arquivo.seek(0)

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

arquivo.seek(0)

linhas = arquivo.readlines()
print(linhas)
print(len(linhas))

arquivo.seek(0)
ret = arquivo.read(43)
print(ret)

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)

"""
    Bloco with

É utilizado para criar um contexto de trabalho onde os recursos são fechados após o bloco with

É a forma pythonica de manipular arquivos
"""

with open('text.txt') as arq:
    print(arq.readlines())
    print(arq.closed)

print(arq.closed)

"""
    Escrevendo em arquivos  
"""

with open('new.txt','w') as arquivo:
    arquivo.write('Olha só que top.\n' *999)
    arquivo.write('Tá brabo.\n' *999)
    arquivo.write('Eita.bixoo' *999)
"""
print('a')
with open('Algo.txt', 'w') as arquivo:
    while True:
        algo = input("Manda a braba ")
        if algo != 'Não':
            arquivo.write(algo)
            arquivo.write('\n')
        else:
            break
"""
"""
    Modos de Arquivos

r -> Abre para leitura
w -> Abre para escrita e se já existe, sobrescreve 
x -> Abre para escrita somente se o arquivo não existir
a -> Abre para escrita adcionando o conteudo no final do arquivo
+ -> Abre para o modo de atualização, leitura e escrita
"""

"""
    StringIO

Utilizado para ler e criar arquivos em memória
"""
from io import StringIO
mensagem = 'É uma string normal'

arquivo = StringIO(mensagem)
print(arquivo.read())

arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())

