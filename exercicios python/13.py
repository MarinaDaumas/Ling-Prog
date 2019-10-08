
class Funcionario():

    def __init__(self, nome, salario):

        self.nome = str(nome)
        self.salario = float(salario)

    def getNome(self):
        return(self.nome)

    def getSalario(self):
        return(self.salario)



ana = Funcionario("Ana Maria", 15000.00)

print(ana.getNome())
print(ana.getSalario())