from Player import PLAYER
from insults import INSULT
characters = ["Dame", "gentleman", "poor", "gangster", "king", "master ocean"]

# cette fonction affiche les insultes disponibles


def Display_insult_list(list):
    for index in range(0, len(list), 1):
        print("                ", index+1, "-->", list[index])
    print("\n")

# cette fonction affiche les caractères disponibles


def character_select(arr):
    for i in range(0, len(arr), 1):
        print(i+1, "-->", arr[i])


# cette fonction prend une valeur et verifie si le caractère saisie est numerique ou pas
# après elle la compare avec cette valeur maximale (cette fonction est utilisée dans les choix avec les nums)
def saisie_char_num(length, msg):
    verif = False
    while verif == False:
        c = input(msg)
        while c.isnumeric() == False:
            c = input(msg)
        character = int(c)
        if character >= 1 and character <= length:
            verif = True
    return character


# cette fonction permet de gérer les informations de chaque joueur(pseudo et caractère préféré)
def Player_input():
    # le 1er joueur(ca ne marchera pas si sa valeur est vide)
    player1 = input("Pseudo de joueur 1 :")
    while player1 == "":
        player1 = input("Pseudo de joueur 1 :")
    # après avoir saisi le pseudo le joueur peut choisir son caractère
    # par saisir le nombre correspondant avec ce caractère
    character_select(characters)
    character1 = saisie_char_num(len(characters), "choisir un caractère : ")
    # character1_selected c'est la valeur final qui sera retournée par la fonction
    character1_selected = characters[character1-1]
    # on enlève le caractère selectionné de la liste(les deux joueurs ne peuvent pas avoir le meme caractère)
    characters.remove(characters[character1-1])
    # le pseudo du 2éme joueur(ca ne marchera pas si vide ou egal au celui du 1er joueur)
    player2 = input("Pseudo de joueur 2 :")
    while player2.upper() == player1.upper() or player2 == "":
        if player2 != "":
            print("les pseudos doivent être differents")
        player2 = input("Pseudo de joueur 2 :")
    character_select(characters)
    character2 = saisie_char_num(len(characters), "choisir un caractère : ")
    character2_selected = characters[character2-1]
    return player1, player2, character1_selected, character2_selected


name_player1, name_player2, character1, character2 = Player_input()
# on affiche le caractère de chaque joueur
print(name_player1, "-->", character1)
print(name_player2, "-->", character2)
PLAYER1 = PLAYER(name_player1, character1)
PLAYER2 = PLAYER(name_player2, character2)
insult = INSULT()
insult1 = INSULT()
insult2 = INSULT()


def display_array_in_string(arr):
    str = ""
    for i in range(0, len(arr), 1):
        str = str+arr[i]+" "
    return str


def display_messages(player1name, player1msg, player2name, player2msg):
    print("message de ", player1name, " = ", player1msg)
    print("message de ", player2name, " = ", player2msg)

# cette fonction permet de calculer le totalle des points depend des insultes


def sum_insults(arr, insult):
    sum = 0
    for i in range(0, len(arr), 1):
        for insult_index in insult.Sujet:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Verbe:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Verbe_adj:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Adj:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.COD:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
    return sum
# cette fonction permet de gérer le combat


def Combat(PLAYER1, insult1, PLAYER2, insult2):
    list = []
    tabP1 = []
    tabP2 = []
    while PLAYER1.pv > 0 and PLAYER2.pv > 0:
        display_messages(PLAYER1.name, display_array_in_string(
            tabP1), PLAYER2.name, display_array_in_string(tabP2))
        print(PLAYER1.name, " = ", PLAYER1.pv)
        print(PLAYER2.name, " = ", PLAYER2.pv)
        if list == []:
            list = insult.generate_insults_list()
        if list != []:
            Display_insult_list(list)
            choix1 = saisie_char_num(
                len(list), "Le choix de "+PLAYER1.name+" : ")
            tabP1.append(list[choix1-1])
            display_messages(PLAYER1.name, display_array_in_string(
                tabP1), PLAYER2.name, display_array_in_string(tabP2))
            if len(tabP1) >= 3:
                choixattack1 = saisie_char_num(
                    2, PLAYER1.name+" Tu veux attaquer?:\n\n1-->oui\n\n2-->non  ")
                if choixattack1 == 1:
                    s1 = sum_insults(tabP1, insult1)
                    PLAYER2.pv -= s1
                    tabP1 = []
            print(PLAYER1.name, " = ", PLAYER1.pv)
            print(PLAYER2.name, " = ", PLAYER2.pv)
            list.remove(list[choix1-1])

            if list == []:
                list = insult.generate_insults_list()
            Display_insult_list(list)

            choix2 = saisie_char_num(
                len(list), "Le choix de "+PLAYER2.name+" : ")
            tabP2.append(list[choix2-1])
            if len(tabP2) >= 3:
                choixattack2 = saisie_char_num(
                    2, PLAYER2.name+" Tu veux attaquer?:\n\n1-->oui\n\n2-->non  ")
                if choixattack2 == 1:
                    s2 = sum_insults(tabP2, insult2)
                    PLAYER1.pv -= s2
                    tabP2 = []
            list.remove(list[choix2-1])


Combat(PLAYER1, insult1, PLAYER2, insult2)
