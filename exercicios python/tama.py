
class Tamagushi():

    def __init__(self, nome):

        self.nome = nome
        self.diversao = 7
        self.fome = 3
        self.saude = 7
        self.idade = 0
        self.humor = "Feliz"

    def alterarNome(self, nome):
        self.nome = nome

    def alterarFome(self, x=-3):
        self.fome += x

    def alterarSaude(self, x=3):
        self.saude += x

    def alterarDiversao(self, x=3):
        self.diversao += x

    def alterarIdade(self):
        '''
        Aumenta em 1 a idade do Tamagushi 
        '''
        self.idade += 1

    def retornarNome(self):
        print("Nome: {}".format(self.nome)) 

    def retornarFome(self):

        if self.fome > 10:
            self.fome = 10

        if self.fome < 0:
            self.fome = 0

        print("Fome: {}".format(self.fome)) 

    def retornarSaude(self):

        if self.saude > 10:
            self.saude = 10

        if self.saude < 0:
            self.saude = 0

        print("Saude:{}".format(self.saude))


    def retornarDiversao(self):

        if self.diversao > 10:
            self.diversao = 10

        if self.diversao < 0:
            self.diversao = 0

        print("Diversao: {}".format(self.diversao))

    def retornarIdade(self):
        print("Idade: {} tama-anos".format(self.idade))

    def calcHumor(self):

        if self.fome > 8 or self.saude < 2:
            h = "Morrendo"

        elif self.fome > 5 or self.saude < 5:
            h = "Triste"

        elif self.diversao <= 5:
            h = "Entediado"

        elif self.fome > 3 or self.saude < 7:
            h = "Mais ou menos"

        elif self.fome <= 3 and self.saude >= 7:
             h = "Feliz"

        self.humor =  h

    def agir(self, acao):
        if "comida" in acao:
            self.alterarFome()
            self.retornarFome()

        if "vitamina" in acao:
            self.alterarSaude()
            self.retornarSaude()
            
        if "brincar" in acao:
            self.alterarDiversao()
            self.retornarDiversao()

        if "dormir" in acao:
            print("\n{}: ZZZzzzzz...".format(self.nome))
            
        elif "mudar" in acao:
            nome = input("\nEscolha um novo nome para o seu bichinho: " )
            self.alterarNome(nome)
        
    def atualizar(self):

        self.alterarFome(0.5)
        self.alterarSaude(-0.2)
        self.alterarDiversao(-0.5)
        self.alterarIdade()

    def start(self):
        '''
        Método principal
        '''
        print("\nVoce agora é responsavel por {}. Voce deve dar comida, brincar, dar vitamina quando sua saúde estiver baixa e botar pra dormir antes de ir embora\n".format(self.nome))
        print(self.nome)

        while True:
            self.calcHumor()
            print("\nHumor: {}".format(self.humor))

            acao = input("O que deseja fazer com {}?\n".format(self.nome))
            
            self.agir(acao)
            self.atualizar()

            if 'dormir' in acao:
                break


if __name__ == "__main__":

    nome = input("Escolha um nome para o seu bichinho: ")
    tam = Tamagushi(nome)

    tam.start()