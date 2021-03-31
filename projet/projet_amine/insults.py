from random import randint
from liste_insultes import Liste_insultes


class INSULT:
    def __init__(self):
        self.Sujet = [Liste_insultes("tu", 6), Liste_insultes("ton père", 14), Liste_insultes("ta mère", 20), Liste_insultes(
            "ton mari", 8), Liste_insultes("ta femme", 8), Liste_insultes("ta soeur", 10), Liste_insultes("ton frère", 10), Liste_insultes("ton chien", 6), Liste_insultes("ton chat", 6), Liste_insultes("ton hamster", 6)]
        self.Verbe = [Liste_insultes("es(t)", 3), Liste_insultes("a(s)", 3), Liste_insultes("n'es(t) pas", 3), Liste_insultes("n'a(s) pas", 3), Liste_insultes(
            "n'es(t) pas", 3), Liste_insultes("a(s) triché", 3), Liste_insultes("n'a(s) pas regardé", 4), Liste_insultes("rassemble(s) à", 4), Liste_insultes("ne connais pas", 4), Liste_insultes("rassemble(s) à", 0), Liste_insultes("rassemble(s) à", 0)]
        self.Verbe_adj = [Liste_insultes("es(t) lent comme", 5), Liste_insultes(
            "es(t) stupide comme", 5), Liste_insultes("es(t) con comme", 4), Liste_insultes("est bete comme", 6), Liste_insultes("est aveugle comme", 5), Liste_insultes("est aveugle comme", 0), Liste_insultes("est aveugle comme", 0)]
        self.Adj = [Liste_insultes("stupide", 10), Liste_insultes("un(e) con", 8), Liste_insultes(
            "intelligent(e)", 4), Liste_insultes("petit comme", 5), Liste_insultes("grand", 7), Liste_insultes("un(e) idiot", 7), Liste_insultes("un(e) idiot", 0), Liste_insultes("un(e) idiot", 0)]
        self.COD = [Liste_insultes("star wars", 6), Liste_insultes("le train", 5), Liste_insultes("l'intelligence", 5), Liste_insultes("l'honneur", 7), Liste_insultes("Prison Break", 6), Liste_insultes("La casa del papel", 6), Liste_insultes(
            "la maison", 4), Liste_insultes("la merde", 5), Liste_insultes("une pyramide", 7), Liste_insultes("en cp pour réussir", 7), Liste_insultes("de vie", 5), Liste_insultes("la vache", 6)]

    def generate_random_list(self):
        Random_List = []
        if len(self.Sujet)>1:
            sujet = randint(4, 6)
            suj_val = randint(0, len(self.Sujet)-1)
            for j in range(0, sujet, 1):
                Random_List.append(self.Sujet[suj_val].name)
                self.Sujet.remove(self.Sujet[suj_val])
                suj_val = randint(0, len(self.Sujet)-1)
            # while self.Sujet[suj_val].name in Random_List:
            #     suj_val=randint(0,len(self.Sujet)-1)
        if len(self.Verbe)>2:
            verbe = randint(3, 4)
            ver_val = randint(0, len(self.Verbe)-1)
            for vb in range(0, verbe, 1):
                Random_List.append(self.Verbe[ver_val].name)
                self.Verbe.remove(self.Verbe[ver_val])
                ver_val = randint(0, len(self.Verbe)-1)
            # while self.Verbe[ver_val].name in Random_List:
            #     ver_val=randint(1,len(self.Verbe)-1)
        if len(self.Verbe_adj)>2:
            verbe_adj = randint(2, 3)
            ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            for vb_adj in range(0, verbe_adj, 1):
                Random_List.append(self.Verbe_adj[ver_adj_val].name)
                self.Verbe_adj.remove((self.Verbe_adj[ver_adj_val]))
                ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            # while self.Verbe[ver_adj_val].name in Random_List:
            #     ver_adj_val=randint(1,len(self.Verbe_adj)-1)
        if len(self.Adj)>2:
            adjective = randint(2, 3)
            adj_val = randint(0, len(self.Adj)-1)
            for adj in range(0, adjective, 1):
                Random_List.append(self.Adj[adj_val].name)
                self.Adj.remove(self.Adj[adj_val])
                adj_val = randint(0, len(self.Adj)-1)
                # while self.Adj[adj_val].name in Random_List:
                #     adj_val=randint(1,len(self.Adj)-1)
        if len(self.COD)>2:
            cod_rep = randint(2, 3)
            cod_val = randint(0, len(self.COD)-1)
            for cod_i in range(0, cod_rep, 1):
                Random_List.append(self.COD[cod_val].name)
                self.COD.remove(self.COD[cod_val])
                cod_val = randint(0, len(self.COD)-1)
                # while self.COD[cod_val].name in Random_List:
                #     cod_val=randint(1,len(self.COD)-1)
        return Random_List

    def generate_insults_list(self):
        print("\n")
        List = self.generate_random_list()
        if List != []:
            n=len(List)
            displayed_list=[]
            for index in range(0, n, 1):
                List_random_element=randint(0,len(List)-1)
                displayed_list.append(List[List_random_element])
                List.remove(List[List_random_element])
        return displayed_list
