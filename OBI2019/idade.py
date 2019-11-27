# -*- coding: utf-8 -*-

temp = True
while temp:
    M = int(input("Idade Monica: "))
    A = int(input("Idade primeiro filho: "))
    B = int(input("Idade segundo filho: "))

    if 40 > M or M > 110 or A == B or 1 > A or A >= M or  1 > B or B >= M:
        temp = True
        print("Idades invalidas")
    else:
        temp = False

F = M - (A+B)
filhos = [A, B, F]
V = max(filhos)
print("Idade filho mais velho = " + str(V))