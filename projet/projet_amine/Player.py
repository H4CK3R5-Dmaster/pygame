from insults import INSULT
from liste_insultes import Liste_insultes
from random import randint
class PLAYER:
    def __init__(self,name,caractere):        
        self.pv=200
        self.name=name
        self.character=caractere
        if self.character=="Dame":
            self.type = "ground"

    # def choose_insult(self,)


