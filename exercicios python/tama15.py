from tama import Tamagushi


class TamagushiPlus(Tamagushi):

    def alterarFome(self, x=None):

        if x == None:
            x = int(input("\nQuanto de comida voce quer dar?\n"))

        self.fome -= x

    def alterarDiversao(self, x=None):

        if x == None:
            x = int(input("\nQuanto tempo voce quer brincar?\n"))
            for i in range(x):
                self.alterarFome(0.2)

        self.diversao += x


if __name__ == "__main__":

    nome = input("Escolha um nome para o seu bichinho: ")
    tam = TamagushiPlus(nome)
    tam.start()