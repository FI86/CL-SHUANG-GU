# Exercice 14
# Mini Système BDD à partir d'un fichier qu'on nommera utilisateurs.txt et qui
# se situera dans le même dossier que ce script.

# Dans un premier temps :
# Créer un dictionnaire qui permettra d'enregistrer en clé le nom 
# et en valeur l'age et la taille de l'utilisateur.
# Créer une fonction inscription pour saisir les données utilisateurs, 
# les inscrire dans le dictionnaire et poser la question si on veut continuer
# à saisir un utilisateur.
# Créer une fonction consultationTotale qui permet de voir les données
# des utilisateurs enregistrés dans le dictionnaire.
# Créer une fonction consultation qui permettra de consulter les données d'un utilisateur.
# Créer un menu pour choisir entre quitter, inscription ou consultation.

# Dans un deuxième temps :
# Créer une fonction enregistrer qui enregistrera les infos utilisateurs
# dans le fichier nommé utilisateurs.txt
# On utilisera le caractère séparateur @ pour séparer la clé des valeurs du dictionnaire,
# et le caractère # pour séparer les données constituant ces valeurs.
# Exemple Juliette@18#1.68
# Créer une fonction lecture qui permettra de lire le fichier utilisateurs.txt
# et d'inscrire les données lues dans le dictionnaire.
# Modifier le menu pour ajouter les fonctions enregistrement et lecture.

# Exemple de menu :
# (L) Lecture
# (I) Inscription 
# (C) Consultation par nom
# (T) Consultation totale
# (E) Enregistrement
# (Q) Quitter

import os
import re

FICHIER = "/utilisateurs.txt"
CHEMIN = os.path.dirname(__file__)
dico = {}

def inscription():
    while True:
        nom = input("Saisir le nom de l'utilisateur : ")
        # Verification si un nom n'a pas de chiffre dans la saisie.
        if any(c.isdigit() for c in nom):
            print("le nom ne doit pas avoir de chiffre.")
            continue

        while True:
            try:
                age = int(input("Saisissez l'age de l'utilisateur : "))
                if age > 0:
                    break
                else:
                    print("Saisissez un age positif.")
            except ValueError:
                print("Saisissez un nombre entier pour l'age.")

        while True:
            try:
                taille = float(input("Saisissez la taille de l'utilisateur : "))
                if taille > 0:
                    break
                else:
                    print("Saisissez une taille positive")                
            except ValueError:
                print("Saisissez un nombre pour la taille.")

        dico[nom] = (age, taille)
        reponse = input("Ecrire 'non' pour arreter de saisir un utilisateur.")
        if reponse.upper() == "NON": break

def consultation():
    nom = input("Quel nom d'utilisateur ? ")
    
    if nom in dico:
        print(f"Nom : {nom:20} - Age : {dico[nom][0]:<03d} - Taille : {dico[nom][1]:2.2f}")
    else:
        print("L'utilisateur n'existe pas.")

def consultationTotale():
    for nom in dico:
        print(f"Nom : {nom:20} - Age : {dico[nom][0]:<03d} - Taille : {dico[nom][1]:2.2f}")

def ligne():
        print("_" * 50)

def enregistrement():
    try:
        with open(CHEMIN + FICHIER, "wt") as f:
            for nom in dico:
                f.write(f"{nom}@{dico[nom][0]}#{dico[nom][1]}\n")

        print("Ecriture du dictonnaire dans le fichier effectuée.")
    except Exception:
        print("Erreur d'enregistrement.")

def lecture():
    try:
        with open(CHEMIN + FICHIER, "rt") as f:
            for ligneInfos in f.readlines():
                # Solution 1
                # utilisateur = ligneInfos.split("@")
                # nom = utilisateur[0]
                # tampon = utilisateur[1].split("#")
                # age = int(tampon[0])
                # taille = float(tampon[1])
                # dico[nom] = (age, taille)
                # Solution 2 avec regex 
                # pour controler l'age compris entre 0 et 150
                # remplacer (\d+) par (?:[0-9]|[1-9][0-9]|1[0-4][0-9]|150)
                regexp = re.compile(r'^(.+)@(\d+)#([012]\.\d+)$')
                m = re.match(regexp, ligneInfos)
                if m:
                    nom = m[1]
                    age = int(m[2])
                    taille = float(m[3])
                    dico[nom] = (age, taille)
                else:
                    print("Ligne invalide rencontrée :", ligneInfos.rstrip('\n'))
    # Si le fichier n'est pas trouvé à la lecture on le crée.
    except Exception:
        f = open(CHEMIN + FICHIER, "wt") 
        f.close()
        print("Le fichier n'existait pas, il est maintenant crée.")
    else:
        print("Lecture fichier effectuée.")

def quitter():
    print("Fin de programme.")
    input("Appuyer sur la touche <Entrée> pour quitter !")
    raise SystemExit

def clear():
    if os.name == "nt": os.system('cls') 
    else: os.system('clear') 

def main():
    clear()
    # Solution 1 premiere et deuxieme partie
    # menu = """
    # (L) Lecture
    # (I) Inscription
    # (C) Consultation
    # (T) Consutation Totale
    # (E) Enregistrement
    # (Q) Quitter
    # """
    #
    # reponse = ""    
    # while reponse != "Q":
    #     print(menu)
    #     reponse = input("Votre choix : ").upper()
    #     ligne()
    #   # Solution avec match case :
        # match reponse:
            # case "L": lecture()
            # case "I": inscription()
            # case "C": consultation()
            # case "T": consultationTotale()
            # case "E": enregistrement()
            # case "Q": quitter()
            # case _: print("Choisissez l'une des option du menu.")
    # 
    #     ligne()
    #
      # Solution avec if elif else :        
        # if reponse == "L": lecture()
        # elif reponse == "I": inscription()
        # elif reponse == "C": consultation()
        # elif reponse == "T": consultationTotale()
        # elif reponse == "E": enregistrement()
        # elif reponse == "Q": quitter()
        # else: print("Choisissez l'une des options du menu.")
        
        # ligne()

    # Solution 2
    dicoMenu = {
        "L" : ("Lecture", lecture),
        "I" : ("Inscription", inscription),
        "C" : ("Consultation par nom", consultation),
        "T" : ("Consultation totale", consultationTotale),
        "E" : ("Enregistrement", enregistrement),
        "Q" : ("Quitter", quitter)}  

    while True:
        for cle in dicoMenu: # sorted(dicoMenu): # ==> tri le menu sur la clé
            print(f"{cle} : {dicoMenu[cle][0]}")
        
        reponse = input("Votre choix : ").upper()
        ligne()

        if reponse not in dicoMenu.keys(): 
            print("Veuillez saisir un choix du menu.")
        else : 
            eval("dicoMenu.get(reponse, "")[1]()")
            
        ligne()
    
if __name__ == "__main__":
    main()
