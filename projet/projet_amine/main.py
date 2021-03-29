from Player import PLAYER
from insults import INSULT
characters=["Dame","gentleman","poor","gangster","king","master ocean"]
def Display_insult_list(list):
    for index in range(0,len(list),1):
        print("                ", index+1, "-->", list[index])
    print("\n")
def character_select(arr):
    for i in range(0,len(arr),1):
        print(i+1,"-->",arr[i])
def Player_input():
    player1=input("Pseudo de joueur 1 :")
    while player1 =="":
        player1=input("Pseudo de joueur 1 :")
    character_select(characters)
    character1=int(input("choisir un caractere : "))
    while character1<1 or character1>len(characters):
        character1=int(input("choisir un caractere : "))
    character1_selected=characters[character1-1]
    characters.remove(characters[character1-1])
    player2=input("Pseudo de joueur 2 :")
    while player2.upper()==player1.upper():
        print("les pseudos doivent être differents")
        player2=input("Pseudo de joueur 2 :")
    character_select(characters)
    character2=int(input("choisir un caractere : "))
    while character2<1 or character2>len(characters):
        character2=int(input("choisir un caractere : "))
    character2_selected=characters[character2-1]
    return player1,player2,character1_selected,character2_selected
name_player1,name_player2,character1,character2=Player_input()
print(name_player1,"-->",character1)
print(name_player2,"-->",character2)
PLAYER1=PLAYER(name_player1,character1)
PLAYER2=PLAYER(name_player2,character2)
insult=INSULT()
def Combat(PLAYER1,PLAYER2):
    list=[]
    while PLAYER1.pv>0 and PLAYER2.pv>0:
        if list==[]:
            list=insult.generate_insults_list()
        if list !=[]:
            Display_insult_list(list)
            print("le choix de ",PLAYER1.name, ":")
            choix1=int(input())
            while choix1<1 or choix1>len(list):
                print("le choix de ",PLAYER1.name, ":")
                choix1=int(input())   
            list.remove(list[choix1-1])         
Combat(PLAYER1,PLAYER2)