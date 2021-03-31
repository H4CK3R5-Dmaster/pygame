from Player import PLAYER
from insults import INSULT
characters = ["Dame", "gentleman", "poor", "gangster", "king", "master ocean"]

#this function displays the available insults
def Display_insult_list(list):
    for index in range(0, len(list), 1):
        print("                ", index+1, "-->", list[index])
    print("\n")

#this function displays the available characters
def character_select(arr):
    for i in range(0, len(arr), 1):
        print(i+1, "-->", arr[i])


#this function takes the length of an array to check if the value inserted is numeric
#as well as this value is inside the array
def saisie_char_num(length,msg):
    verif=False
    while verif == False:
        c=input(msg)
        while c.isnumeric()==False:
            c=input(msg)
        character=int(c)
        if character>=1 and character<=length:
            verif=True
    return character

    
#this function takes care of the player input such as the playername and character
def Player_input():
    #1stplayername(wont work if empty)
    player1 = input("Pseudo de joueur 1 :")
    while player1 == "":
        player1 = input("Pseudo de joueur 1 :")
    #after player name inserted the player has to choose a character 
    #by choosing the number related to that character
    character_select(characters)
    character1=saisie_char_num(len(characters),"choisir un caractère : ")
    #character1_selected is the 1st player's final value which will be returned by the function
    character1_selected = characters[character1-1]
    #we remove the character chosen by player1(the players cant have the same character)
    characters.remove(characters[character1-1])
    #2nd player's name (wont work if empty or same name as 1st player)
    player2 = input("Pseudo de joueur 2 :")
    while player2.upper() == player1.upper() or player2=="":
        if player2 !="":
            print("les pseudos doivent être differents")
        player2 = input("Pseudo de joueur 2 :")
    character_select(characters)
    character2=saisie_char_num(len(characters),"choisir un caractère : ")
    character2_selected = characters[character2-1]
    return player1, player2, character1_selected, character2_selected


name_player1, name_player2, character1, character2 = Player_input()
#we display each player and character
print(name_player1, "-->", character1)
print(name_player2, "-->", character2)
PLAYER1 = PLAYER(name_player1, character1)
PLAYER2 = PLAYER(name_player2, character2)
insult = INSULT()


def display_array_in_string(arr):
    str = ""
    for i in range(0, len(arr), 1):
        str = str+arr[i]+" "
    return str


def display_messages(player1name,player1msg,player2name,player2msg):
    print("message de ", player1name, " = ",player1msg)
    print("message de ", player2name, " = ",player2msg)

def Combat(PLAYER1, PLAYER2):
    list = []
    success = 0
    tabP1 = []
    tabP2 = []
    while PLAYER1.pv > 0 and PLAYER2.pv > 0 or (list == [] and success != 0):
        display_messages(PLAYER1.name,display_array_in_string(tabP1),PLAYER2.name,display_array_in_string(tabP2))
        success = 1
        if list == []:
            list = insult.generate_insults_list()
        if list != []:
            Display_insult_list(list)
            # print("le choix de ", PLAYER1.name, ":")
            str1="Le choix de "+PLAYER1.name+" : "
            str2="Le choix de "+PLAYER2.name+" : "
            choix1 = saisie_char_num(len(list),str1)
            tabP1.append(list[choix1-1])
            display_messages(PLAYER1.name,display_array_in_string(tabP1),PLAYER2.name,display_array_in_string(tabP2))
            if len(tabP1)>=3:
                print(PLAYER1.name, " do you want to attack?\n\n1-->yes\n\n2-->no : ")
                choixattack1=int(input())
                while choixattack1!=1 and choixattack1!=2:
                    print(PLAYER1.name, " do you want to attack?\n\n1-->yes\n\n2-->no : ")

            list.remove(list[choix1-1])
            
            if list == []:
                list = insult.generate_insults_list()
            Display_insult_list(list)
            
            choix2=saisie_char_num(len(list),str2)
            tabP2.append(list[choix2-1])
            list.remove(list[choix2-1])


Combat(PLAYER1, PLAYER2)
