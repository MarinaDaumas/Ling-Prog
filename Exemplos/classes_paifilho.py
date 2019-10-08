class Pai():
    def comer(self):
        print("nhac!\nnhac!\nnhac!\nnhac!")

    def dormir(self):
        print("RRRROONN spspssp")

class Filho(Pai):
    def jogar_videogame(self):
        print("Trrrr!\nPiuuuu!\nPiuuu!")
    
    def dormir(self):
        print("Zzzzzzzzzz")



Eric = Filho()

Eric.comer()
Eric.jogar_videogame()
Eric.dormir()