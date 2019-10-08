
class ContaBancaria():

    def __init__(self, saldo):
        self.saldo = saldo

    def printSaldo(self):
        print(self.saldo)

class ContaDeInvestimento(ContaBancaria):

    def __init__(self, saldo, taxa):
        self.saldo = saldo
        self.taxa = taxa

    def adicioneJuros(self):
        self.saldo = self.saldo*(1+self.taxa)
   


if __name__ == "__main__":

    poupanca = ContaDeInvestimento(1000.00, 0.1)

    for i in range(5):
        poupanca.adicioneJuros()

    poupanca.printSaldo()
