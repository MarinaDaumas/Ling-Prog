
class Carro:
    
    def __init__(self, consumo):
        self.consumo = consumo 
        self.combustivel = 0

    def andar(self, dist):

        self.combustivel = self.combustivel - self.consumo*dist
        if self.combustivel <= 0:
            self.combustivel = 0
            print("O carro morreu no meio do caminho, seu irresponsavel")

    def obterGasolina(self):
        '''
        Retorna a quantidade de gasolina no tanque.
        '''
        print(self.combustivel)

    def adcionarGasolina(self, gas):
        self.combustivel = self.combustivel + gas


if __name__ == "__main__":

    fusca = Carro(4)
    fusca.adcionarGasolina(40)
    fusca.andar(13)
    fusca.obterGasolina()