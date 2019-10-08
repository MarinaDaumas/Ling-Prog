def soma(n1, n2):
    return (n1 + n2)

def sub(n1, n2):
    return (n1 - n2) 
        
def mult(n1, n2):
    return (n1 * n2)

def div(n1, n2):
    return (n1 / n2)



def calculadora():   
    print("Escolha 2 numeros e uma operacao")

    while True: 
    
        n1 = float(input("Primeiro numero: "))
        n2 = float(input("Segundo numero: "))
        operacao = raw_input("Operacao: ")

        if operacao == "marina":
            print("SAAAAAAAAAAAAAAAAAAAA")

        if operacao == "+":
            result = (soma(n1, n2))
        elif operacao == "-":
            result = (sub(n1, n2))
        elif operacao == "*":
            result = (mult(n1, n2))
        elif operacao == "/":
            result = (div(n1, n2))
        else:
            print("Operacao invalida")

        print(result)

        while True:
            cont = raw_input("Deseja contiuar? (S ou N)")
            if cont ==  "S" or cont == "N":
                break
            else:
                print("Resposta invalida")

        if cont ==  "N":
            break      

if __name__ == "__main__":
    calculadora()