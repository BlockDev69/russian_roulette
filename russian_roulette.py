import os
import random
import time
from colorama import Fore, Style, init
from art import*
from termcolor import colored

print(colored(text2art('DEAD OR LIFE').center(6), 'red'))

# Initialisation de colorama pour les couleurs dans le terminal
init(autoreset=True)

def afficher_titre():
    print(Fore.YELLOW + "==============================================")
    print(Fore.YELLOW + "       ROULETTE RUSSE - ÉDITION TERMINAL       ")
    print(Fore.YELLOW + "==============================================")
    print(Style.RESET_ALL)

def afficher_vies(vies):
    print(Fore.CYAN + f"\nVies restantes : {vies}")
    print(Fore.CYAN + "❤️ " * vies + "💔 " * (6 - vies))
    print(Style.RESET_ALL)

def afficher_message_perte(fichier_a_supprimer):
    print(Fore.RED + "==============================================")
    print(Fore.RED + "       BOOM ! Vous avez perdu une vie.        ")
    print(Fore.RED + f"  Le fichier {fichier_a_supprimer} a été supprimé.  ")
    print(Fore.RED + "==============================================")
    print(Style.RESET_ALL)

def afficher_message_survie():
    print(Fore.GREEN + "==============================================")
    print(Fore.GREEN + "       Ouf ! Vous avez survécu cette fois.     ")
    print(Fore.GREEN + "==============================================")
    print(Style.RESET_ALL)

def afficher_message_fin():
    print(Fore.RED + "==============================================")
    print(Fore.RED + "  Vous avez perdu toutes vos vies. Game Over ! ")
    print(Fore.RED + "==============================================")
    print(Style.RESET_ALL)

def supprimer_fichier_aleatoire(dossier):
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    if fichiers:
        fichier_a_supprimer = random.choice(fichiers)
        os.remove(os.path.join(dossier, fichier_a_supprimer))
        return fichier_a_supprimer
    return None

def supprimer_dossier(dossier):
    for fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, fichier)
        try:
            if os.path.isfile(chemin_fichier) or os.path.islink(chemin_fichier):
                os.unlink(chemin_fichier)
            elif os.path.isdir(chemin_fichier):
                shutil.rmtree(chemin_fichier)
        except Exception as e:
            print(Fore.RED + f"Erreur lors de la suppression de {chemin_fichier}. Raison : {e}")
    os.rmdir(dossier)
    print(Fore.RED + f"Le dossier {dossier} a été supprimé.")

def roulette_russe(dossier):
    vies = 6
    afficher_titre()
    print(Fore.MAGENTA + "Bienvenue dans le jeu de la roulette russe !")
    print(Fore.MAGENTA + "Choisissez un nombre entre 1 et 6. Si vous tombez sur le mauvais nombre, un fichier sera supprimé.")
    print(Fore.MAGENTA + "Si vous perdez 6 fois, tout le dossier sera supprimé !")
    print(Style.RESET_ALL)

    while vies > 0:
        afficher_vies(vies)
        try:
            nombre_joueur = int(input(Fore.BLUE + "Choisissez un nombre entre 1 et 6 : " + Style.RESET_ALL))
            if nombre_joueur < 1 or nombre_joueur > 6:
                print(Fore.RED + "Veuillez choisir un nombre entre 1 et 6.")
                continue
        except ValueError:
            print(Fore.RED + "Veuillez entrer un nombre valide.")
            continue

        nombre_programme = random.randint(1, 6)
        print(Fore.YELLOW + f"Le programme a choisi le nombre : {nombre_programme}")
        time.sleep(1)  # Petite pause pour le suspense

        if nombre_joueur == nombre_programme:
            fichier_a_supprimer = supprimer_fichier_aleatoire(dossier)
            if fichier_a_supprimer:
                afficher_message_perte(fichier_a_supprimer)
            else:
                print(Fore.RED + "Aucun fichier à supprimer dans le dossier.")
            vies -= 1
        else:
            afficher_message_survie()

        if vies == 0:
            afficher_message_fin()
            supprimer_dossier(dossier)
            break

if __name__ == "__main__":
    dossier = input(Fore.BLUE + "Entrez le chemin du dossier : " + Style.RESET_ALL)
    if os.path.isdir(dossier):
        roulette_russe(dossier)
    else:
        print(Fore.RED + "Le chemin spécifié n'est pas un dossier valide.")