
class Funcionario():

    def __init__(self, nome, salario):

        self.nome = str(nome)
        self.salario = float(salario)

    def aumentarSalario(self, perc):
        self.salario += self.salario*perc/100 

    def getNome(self):
        return(self.nome)

    def getSalario(self):
        return(self.salario)


m = Funcionario("Pedro Pedra", 10000.00)

m.aumentarSalario(20)

print(m.getSalario())