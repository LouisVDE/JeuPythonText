import os
import time
import re

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
    ft_NAME()

def ft_NAME():
    while True:
        clear()
        pseudo = input("Entrez votre nom : ")
        # Vérifier si le nom ne contient que des lettres et des espaces
        if not re.match("^[a-zA-Z ]+$", pseudo):
            print("Erreur : le nom ne doit contenir que des lettres et des espaces\n")
            continue
        clear()
        print(pseudo+"? Etes vous sur ?")
        choice = ft_choice()
        if choice == 1:
            #DEBUT DE JEU
            return pseudo
        elif choice == 2:
            # Demander à l'utilisateur de saisir un nouveau nom
            continue
        else:
            # Gérer les autres choix d'entrée
            print("Choix invalide. Veuillez réessayer.\n")
            continue

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
