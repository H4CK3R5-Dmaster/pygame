from random import randint
from liste_insultes import Liste_insultes


class INSULT:
    def __init__(self):
        self.Sujet = [Liste_insultes("tu", 2), Liste_insultes("ton père", 7), Liste_insultes("ta mère", 9), Liste_insultes(
            "ton mari", 4), Liste_insultes("ta femme", 4), Liste_insultes("ta soeur", 5), Liste_insultes("ton frère", 5)]
        self.Verbe = [Liste_insultes("es(t)", 2), Liste_insultes("a(s)", 2), Liste_insultes("n'es(t) pas", 2), Liste_insultes("n'a(s) pas", 2), Liste_insultes(
            "n'es(t) pas", 2), Liste_insultes("a(s) triché", 2), Liste_insultes("n'a(s) pas regardé", 2), Liste_insultes("rassemble(s) à", 2)]
        self.Verbe_adj = [Liste_insultes("es(t) lent comme", 2), Liste_insultes(
            "es(t) stupide comme", 2), Liste_insultes("es(t) con comme", 2), Liste_insultes("est aveugle comme", 2), Liste_insultes("est aveugle comme", 2)]
        self.Adj = [Liste_insultes("stupide", 10), Liste_insultes("un(e) con", 8), Liste_insultes(
            "intelligent(e)", 4), Liste_insultes("petit comme", 5), Liste_insultes("grand", 7), Liste_insultes("un(e) idiot", 7)]
        self.COD = [Liste_insultes("star wars", 4), Liste_insultes("le train", 5), Liste_insultes("Prison Break", 5), Liste_insultes("La casa del papel", 5), Liste_insultes(
            "la maison", 4), Liste_insultes("la merde", 5), Liste_insultes("une pyramide", 5), Liste_insultes("en cp pour réussir", 5), Liste_insultes("de vie", 5)]

    def generate_random_list(self):
        Random_List = []
        if len(self.Sujet)>3:
            sujet = randint(1, 2)
            suj_val = randint(0, len(self.Sujet)-1)
            for j in range(0, sujet, 1):
                Random_List.append(self.Sujet[suj_val].name)
                self.Sujet.remove(self.Sujet[suj_val])
                suj_val = randint(0, len(self.Sujet)-1)
            # while self.Sujet[suj_val].name in Random_List:
            #     suj_val=randint(0,len(self.Sujet)-1)
        if len(self.Verbe)>3:
            verbe = randint(1, 2)
            ver_val = randint(0, len(self.Verbe)-1)
            for vb in range(0, verbe, 1):
                Random_List.append(self.Verbe[ver_val].name)
                self.Verbe.remove(self.Verbe[ver_val])
                ver_val = randint(0, len(self.Verbe)-1)
            # while self.Verbe[ver_val].name in Random_List:
            #     ver_val=randint(1,len(self.Verbe)-1)
        if len(self.Verbe_adj)>3:
            verbe_adj = randint(1, 2)
            ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            for vb_adj in range(0, verbe_adj, 1):
                Random_List.append(self.Verbe_adj[ver_adj_val].name)
                self.Verbe_adj.remove((self.Verbe_adj[ver_adj_val]))
                ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            # while self.Verbe[ver_adj_val].name in Random_List:
            #     ver_adj_val=randint(1,len(self.Verbe_adj)-1)
        if len(self.Adj)>3:
            adjective = randint(1, 2)
            adj_val = randint(0, len(self.Adj)-1)
            for adj in range(0, adjective, 1):
                Random_List.append(self.Adj[adj_val].name)
                self.Adj.remove(self.Adj[adj_val])
                adj_val = randint(0, len(self.Adj)-1)
                # while self.Adj[adj_val].name in Random_List:
                #     adj_val=randint(1,len(self.Adj)-1)
        if len(self.COD)>3:
            cod_rep = randint(1, 2)
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
