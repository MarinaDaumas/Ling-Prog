from random import randint

N = int(input("tamanho sequencia = "))

if N < 3 or N > 500:
    print("tamanho invalido")

else:
    seq = []

    temp = int(input())
    if temp != 1:
        print("numero invalido")
    seq.append(temp)

    for i in range(N-2):
        temp = int(input())
        if temp != 1 and temp != 2:
            print("numero invalido")
            break
        seq.append(temp)
    
    temp = int(input())
    if temp != 1:
        print("numero invalido")
    seq.append(temp)

    #continuar depois
        if seq[i] == seq[i+1]:
            del(seq[i+1]) 
            i -= 1

    Niguais = len(seq)
    print("Quantidade max de numeros" + str(Niguais))