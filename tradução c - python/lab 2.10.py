print("Escolha 3 numeros")

n1 = int(input("N1 = "))
n2 = int(input("N2 = "))
n3 = int(input("N3 = "))

lista = [n1, n2, n3]
lista.sort()
print(lista)

if n1 == n2 and n2 == n1:
    print("Todos iguais")

else:
    print("Maior = {}\nMenor = {}".format(lista[2], lista[0])) 