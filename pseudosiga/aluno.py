class Aluno (name, DRE):

    def __init__(self, name):

    def novo_cadastro(self, name, DRE, password):
        
        login = self.name + "-" + password
        with open("login_list.txt", "+w") as file:
            login.write(file)

    def login(self, name, password):

        login = self.name + "-" + password
        with open("login_list.txt", "r") as file:
            napas = (line for line in file)
            if login in napas:
                return True