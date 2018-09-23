annee = int(0)  # Annee en entier
mois = int(0)  # Mois en entier
jour = int(0)  # Jour en entier


def anneeMoisJour():  # Fonction pour obtenir le jour de la date entrée par un utilisateur
    # Recuperation des variables annee/mois/jour entree par l'utilisateur
    annee = int(input("Merci d'entrer l'année : "))
    mois = int(input("Merci d'entrer le mois (en chiffres) : "))
    jour = int(input("Merci d'entrer le jour : "))

    while (annee < int(1947)) or (annee == int(1582) and mois < int(11)) or (mois > 12) or (jour > 31):
        print("")
        print("La date est invalide")
        annee = int(input("Merci d'entrer l'année : "))
        mois = int(input("Merci d'entrer le mois (en chiffres) : "))
        jour = int(input("Merci d'entrer le jour : "))

    # On récupèrer les deux derniers chiffres de l'année dans la variable anneeDeux, en typant en string / action / typant entier
    anneeDeux = str(annee)
    anneeDeux = anneeDeux[2:4]
    anneeDeux = int(anneeDeux)

    # On effectue la deuxieme partie a la variable somme, en typant en string / action / typant entier
    somme = anneeDeux / int(4)
    somme = str(somme)
    somme = somme[0:2]
    somme = int(somme)
    somme = anneeDeux + somme

    # On garde la variable, puis on effectue la partie 3
    somme = somme + jour

    # On analyse à quoi correspond le mois pour ajouter ajouter à somme une valeur
    if mois == 1:  # Janvier
        somme = somme + 1
    elif mois == 2:  # Février
        somme = somme + 3
    elif mois == 3:  # Mars
        somme = somme + 3
    elif mois == 4:  # Avril
        somme = somme + 6
    elif mois == 5:  # Mai
        somme = somme + 1
    elif mois == 6:  # Juin
        somme = somme + 4
    elif mois == 7:  # Juillet
        somme = somme + 6
    elif mois == 8:  # Aout
        somme = somme + 2
    elif mois == 9:  # Septembre
        somme = somme + 5
    elif mois == 10:  # Octobre
        somme = somme + 0
    elif mois == 11:  # Novembre
        somme = somme + 3
    elif mois == 12:  # Decembre
        somme = somme + 5

    # Si c'est une annee Bissextile ET Janvier OU Février, on retire 1 à la somme
    if (annee % 400 == 0) and (mois == 1 or mois == 2):
        somme = somme - 1

    # On effectue la sixieme partie a la variable somme, en typant en string / action / typant entier

    anneeSiecle = str(annee)
    anneeSiecle = anneeSiecle[0:2]
    anneeSiecle = int(anneeSiecle)

    # La valeur d'anneeSiecle permet d'ajouter la valeur correspondante à la variable somme

    if anneeSiecle == 16:  # Années1600
        somme = somme + 6
    elif anneeSiecle == 17:  # Années1700
        somme = somme + 4
    elif anneeSiecle == 18:  # Années1800
        somme = somme + 2
    elif anneeSiecle == 19:  # Années1900
        somme = somme + 0
    elif anneeSiecle == 20:  # Années2000
        somme = somme + 6
    elif anneeSiecle == 21:  # Années2100
        somme = somme + 4

    # On divise la somme par 7
    valeurJour = somme % 7

    # La nouvelle valeur obtenue permet de déterminer le jour de la semaine de la date entrée par l'utilisateur
    if valeurJour == 0:  # 0 = Dimanche
        leJour = "dimanche"
    if valeurJour == 1:  # 1 = Lundi
        leJour = "lundi"
    if valeurJour == 2:  # 2 = Mardi
        leJour = "mardi"
    if valeurJour == 3:  # 3 = Mercredi
        leJour = "mercredi"
    if valeurJour == 4:  # 4 = Jeudi
        leJour = "jeudi"
    if valeurJour == 5:  # 5 = Vendredi
        leJour = "vendredi"
    if valeurJour == 6:  # 6 = Samedi
        leJour = "samedi"

    print("Votre date du ", jour, "/", mois, "/", annee, " était un ", leJour)


anneeMoisJour()
