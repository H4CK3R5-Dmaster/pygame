from random import randint
from liste_insultes import Liste_insultes
class INSULT:
    def __init__(self):
        self.Sujet=[Liste_insultes("tu",2),Liste_insultes("ton père",7),Liste_insultes("ta mère",9),Liste_insultes("ton mari",4),Liste_insultes("ta femme",4),Liste_insultes("ta soeur",5),Liste_insultes("ton frère",5)]
        self.Verbe=[Liste_insultes("est",2),Liste_insultes("es",2),Liste_insultes("a",2),Liste_insultes("n'est pas",2),Liste_insultes("n'a pas",2),Liste_insultes("n'as pas",2),Liste_insultes("n'es pas",2)]
        self.Adj=[Liste_insultes("stupide",10),Liste_insultes("con",8),Liste_insultes("intelligent(e)",4),Liste_insultes("petit",5),Liste_insultes("grand",7),Liste_insultes("idiot",7)]
        self.COD=[Liste_insultes("star wars",4),Liste_insultes("le train",5),Liste_insultes("la maison",4),Liste_insultes("la merde",5)]
    def generate_random_list(self):
        Random_List=[]
        sujet=randint(1,3)
        suj_val=randint(0,len(self.Sujet)-1)
        verbe=randint(1,3)
        ver_val=randint(1,len(self.Verbe)-1)
        adjective=randint(1,2)
        adj_val=randint(1,len(self.Adj)-1)
        cod_rep=randint(1,2)
        cod_val=randint(1,len(self.COD)-1)
        for j in range(0,sujet,1):
            Random_List.append(self.Sujet[suj_val].name)
            suj_val=randint(0,len(self.Sujet)-1)
            while self.Sujet[suj_val].name in Random_List:
                suj_val=randint(0,len(self.Sujet)-1)
        for vb in range(0,verbe,1):
            Random_List.append(self.Verbe[ver_val].name)
            ver_val=randint(1,len(self.Verbe)-1)
            while self.Verbe[ver_val].name in Random_List:
                ver_val=randint(1,len(self.Verbe)-1)
        for adj in range(0,adjective,1):
            Random_List.append(self.Adj[adj_val].name)
            adj_val=randint(1,len(self.Adj)-1)
            while self.Adj[adj_val].name in Random_List:
                adj_val=randint(1,len(self.Adj)-1)
        for cod_i in range(0,cod_rep,1):
            Random_List.append(self.COD[cod_val].name)
            cod_val=randint(1,len(self.COD)-1)
            while self.COD[cod_val].name in Random_List:
                cod_val=randint(1,len(self.COD)-1)
        return Random_List
    def display_insults_list(self):
        print("\n")
        List=self.generate_random_list()
        for index in range(0,len(List),1):
            print("                ",index+1,"-->",List[index])
        print("\n")