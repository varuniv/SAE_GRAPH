import requetes


liste_options=["1 - Ensemble des collaborations entre 2 acteurs",
               "2 - Liste des acteurs se trouvant à une distance k d'un acteur",
               "3 - Distance entre 2 acteurs",
               "4 - Centralité d'un acteur",
               "5 - Acteur le plus central du graphe",
               "6 - Distance maximum entre 2 acteurs",
               "7 - Deux acteurs sont proches ou non pour une distance donné",
               "8 - Dessiner le graphe",
               "9 - List des acteur",
               "10 - Quitter l'application"
               ]

titre="Veuillez choisir une des options se trouvant ci-dessous"

# Affichages de l'application

def choix_option():
    valide=False
    while(not valide):
        choix = input("Entrez le numéro d'une des options entre 1 et 10: ")
        if(choix==""):
            print("Vous n'avez pas rentré de numéro")
            print("")
        try:
            opt = int(choix)
        except:
            print("Vous devez rentrer un numéro qui est compris entre 1 et 9")
            continue
        if(opt>len(liste_options) or choix<"1"):
            print("Vous avez entré un numéro non compris dans la liste des options")
        else:
            valide=True
    return int(choix)

def menu_application(titre, liste_options):
    print("+" + len(titre)*"-" + "+")
    print("|" + titre + "|")
    print("+" + len(titre)*"-" + "+")
    for i in range(len(liste_options)):
        print(liste_options[i])

def continuer_utilisation():
    while True:
        choix = input("Voulez-vous continuer à utiliser l'application? Veuillez répondre par Oui ou par Non: ")
        c = ["Oui","OUI","oui","Non","non","NON"]
        if(choix not in c):
            print("Veuillez répondre par Oui ou par Non")
            continue
        match choix:
            case "Oui":
                return True
            case "OUI":
                return True
            case "oui":
                return True
            case "Non":
                return False
            case "non":
                return False
            case "NON":
                return False
            




        

# Fonctions appelant les fonctions dans requetes.py concernées par l'option

G=requetes.json_vers_nx("data_court.txt")

def option_collaborateurs_2_acteurs():
    acteur1=input("Veuillez rentrer un premier acteur")
    acteur2=input("Veuillez rentrer un deuxième acteur")
    return requetes.collaborateurs_communs(G, acteur1, acteur2)

def option_acteurs_a_distance_k():
    acteur=input("Veuillez rentrer un acteur")
    k_valide=False
    while(not k_valide):
        k=input("Veuillez rentrer la distance maximal de recherche")
        try:
            int(k)
        except:
            print("Vous devez rentrer un nombre")
            continue
        k_valide=True
    return requetes.collaborateurs_proches(G, acteur, k)

def option_distance_entre_2_acteurs():
    acteur1=input("Veuillez rentrer un premier acteur")
    acteur2=input("Veuillez rentrer un deuxième acteur")
    return requetes.distance(G, acteur1, acteur2)

def option_centralite_acteur():
    acteur=input("Veuillez rentrer un acteur")
    return requetes.centralite(G, acteur)

def option_acteur_central():
    return requetes.centre_hollywood(G)

def option_distance_max_entre_2_acteurs():
    return requetes.eloignement_max(G)

def option_est_proche():
    acteur1=input("Veuillez rentrer un premier acteur")
    acteur2=input("Veuillez rentrer un deuxième acteur")
    distance=1 # Distance par défaut
    utiliser_distance=input("Voulez-vous préciser une distance. Répondez par Oui si vous souhaitez en préciser une, sinon l'application utilisera la distance par défaut égal à 1")
    if(utiliser_distance=="Oui"):
        distance_valide=False
        while not distance_valide:
            distance=input("Veuillez préciser une distance")
            try:
                int(distance)
            except:
                print("Vous devez rentrer un nombre")
                continue
            distance_valide=True
    return requetes(G, acteur1, acteur2, distance)

def option_dessiner_graphe():
    return requetes.dessiner_graphe(G)

def option_list_acteur():
    print(str(G.nodes).replace('[', '').replace(']', '').replace("'", ''))

# Programme principal

def application():
    utilisation=True
    while utilisation:
        menu_application(titre, liste_options)
        match choix_option():
            case 1:
                option_collaborateurs_2_acteurs()  
            case 2:
                option_acteurs_a_distance_k()
            case 3:
                option_distance_entre_2_acteurs()
            case 4:
                option_centralite_acteur()
            case 5:
                option_acteur_central()
            case 6:
                option_distance_max_entre_2_acteurs()
            case 7:
                option_est_proche()
            case 8:
                option_dessiner_graphe()
            case 9:
                option_list_acteur()
            case 10:
                break
        if(not continuer_utilisation()):
            utilisation=False
        print("")



application()
