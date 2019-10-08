from tama15 import TamagushiPlus

class TamagushiPPLus(TamagushiPlus):

    def ver(self):
                  
        self.retornarNome()
        self.retornarIdade()
        self.retornarFome()
        self.retornarSaude()
        self.retornarDiversao()
    
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
        
        elif "ver" in acao:
            self.ver()
            
        elif "mudar" in acao:
            nome = input("\nEscolha um novo nome para o seu bichinho: " )
            self.alterarNome(nome)



if __name__ == "__main__":

    nome = input("Escolha um nome para o seu bichinho: ")
    tam = TamagushiPPLus(nome)

    tam.start()