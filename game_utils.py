import os
import time

def clear():
    os.system('cls')

def end():
    print("GAME OVER")

def start():
    clear()
    print("Bienvenue dans JEU")
    time.sleep(3)
    clear()
    print("CE JEU NE DISPOSE PAS DE SYSTEME DE SAUVEGARDE")
    time.sleep(3)
    clear()
    ftl_NAME()

def ft_NAME():
    choice = 0
    clear()
    pseudo = input("Entrez votre nom : ")
    clear()
    print(pseudo+"? Etes vous sur ?")
    choice = ft_choice()
    if choice == 1:
        #DEBUT DE JEU
        return
    elif choice == 0:
        _NAME()

def ft_choice():
    while True:
        try:
            choice = int(input("1.Oui | 2.Non : "))
            if choice == 1:
                return 1
            elif choice == 2:
                return 0
            else:
                print("Erreur\n")
        except ValueError:
            print("Erreur : entrée invalide\n")
