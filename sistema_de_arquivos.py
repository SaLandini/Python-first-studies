"""
    Para fazer uso de arquivos do sistema, precisamos importar
    e fazer uso do módulo os.

"""
import os

print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())


os.chdir('backup')
print(os.getcwd())

print(os.listdir())