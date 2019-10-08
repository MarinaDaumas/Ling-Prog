class Aluno:
    
    def __init__(self, dre, nome, curso, cpf, senha):
        self.dre = dre
        self.nome = nome
        self.curso = curso
        self.cpf = cpf 
        self.senha = senha
        
    def get_nome(self):
        print (self.nome)
    
    def get_cpf(self):
        return self.cpf
    
    def get_senha(self):
        return self.senha
        
aluno1 =  Aluno("111", "Carolina", "Controle", "112", "123")
#aluno1.get_nome()

teste_cpf = ""

teste_cpf = input("USER: ")
teste_senha = input("SENHA: ")

if (teste_cpf == aluno1.get_cpf() and teste_senha == aluno1.get_senha()): 
    print ("login com sucesso")
else:
    print ("sai daqui")

