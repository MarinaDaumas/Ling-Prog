from tama import Tamagushi
import random

if __name__ == "__main__":
    
    print("Agora voce tem uma fazenda inteira de bichinhos, mas as regras sao as mesmas." )
    nomes = ["Tulo", "Bobi", "Lulu", "Odete", "Georfina", "Alibaba", "Otis", "Emero", "Linda", "Delcio", "Olavo", "Winston", "Kel", "Mel", "Jules", "Nemer", "Gali", "Alex", "Orango", "Mog", "Nardis", "Pati", "Delso", "Ronaldo", "Rodney"]  
    bichos = []
    for i in range(10):
        nome = random.choice(nomes)
        x = Tamagushi(nome) 
        x.diversao = random.randrange(0, 10)
        x.fome = random.randrange(0, 10)
        bichos.append(x)
    
    while True:

        print("\n")
        for i in range(10):
            print(bichos[i].nome + ": " + bichos[i].humor)

        acao = input("\nEscolha o que fazer na sua fazenda\n(Brincar, dar comida, dar vitamina)\n")

        for i in range(10):
            bichos[i].agir(acao)
            bichos[i].atualizar()
            bichos[i].calcHumor()
        
        if "dormir" in acao:
            break

    