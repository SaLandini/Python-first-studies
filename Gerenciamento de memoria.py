"""
    GIL - Python Global Interpreter Lock
"""
import time
from threading import Thread

contador = 2000000000

def cont_regre(n):
    while n > 0:
        n -= 1
t1 = Thread(target=cont_regre, args=(contador//2,))
t2 = Thread(target=cont_regre, args=(contador//2,))
t3 = Thread(target=cont_regre, args=(contador//2,))
t4 = Thread(target=cont_regre, args=(contador//2,))
t5 = Thread(target=cont_regre, args=(contador//2,))
t6 = Thread(target=cont_regre, args=(contador//2,))

inicio = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
fim = time.time()
print(f'tempo em segundos foi {fim - inicio}')

