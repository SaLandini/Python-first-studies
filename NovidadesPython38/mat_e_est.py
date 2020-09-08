import math

nuns_v1 = [2,3,5,7]
nuns_v2 = (2,3,5,7)
nuns_v3 = {2,3,5,7}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(19))
print(math.sqrt(19))

#Pontos 3d
p3d1 = (12, 56, 76)
p3d2 = (1, 4, 8)

#Pontos 2d
p2d1 = [12, 34]
p2d2 = {12,43}

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

print(math.hypot(*p3d1))
print(math.hypot(*p2d1))


## Estatisca
import statistics

valores_reais = [1.342,3.567,6.6789,4.645]
valores_int = [1,5,7,8]

print(statistics.fmean(valores_int))
print(statistics.fmean(valores_reais))

print(statistics.geometric_mean(valores_int))
print(statistics.geometric_mean(valores_reais))

seq1 = 'Geek Universty'
seq2 = [1,4,5,7,8,9,6,5,3,2,3,5,7,9,0]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))