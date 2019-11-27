
n = input("N = ")
if n < 0 or n > 10000:
    print("N inválido")
else:
    pecas = ((n+1)*(n+2))/2
    print("Numero de pecas = " + str(pecas))