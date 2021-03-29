from insulte import insulte

class game:
    def __init__(self,role):
        self.role = role
        if role == "warrior":
            self.pv = 100
            self.force = 20
            self.defense = 15
            self.type = "ground"
        elif role == "gentleman":
            self.pv = 100
            self.force = 15
            self.defense = 10
            self.type = "wind"
        elif role == "king":
            self.pv = 100
            self.force = 25
            self.defense = 18
            self.type = "fire"
        elif role == "master ocean":
            self.pv = 100
            self.force = 30
            self.defense = 24
            self.type = "water"
        