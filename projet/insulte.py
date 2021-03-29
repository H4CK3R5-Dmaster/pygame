class insulte :
    def __init__(self,name,damage,sujet,verbe,complement,point):
        self.name = name
        self.damage = damage
        self.sujet = sujet
        self.verbe = verbe
        self.complement = complement
        self.point = point

    def __str__(self):
        return self.name 

