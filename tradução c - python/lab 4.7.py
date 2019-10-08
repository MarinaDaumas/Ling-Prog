vet = [5, 6, 7, 86, 0, 74, 11, 9, 33, 1, 68]
vet.sort()

print(vet)

num = int(input("Valor procurado: "))


print("Posicao de {} = {}".format(num, (vet.index(num)+1)))