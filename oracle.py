#import requetes


liste_options=["1 - Ensemble des collaborations entre 2 acteurs",
               "2 - Liste des acteurs se trouvant à une distance k d'un acteur",
               "3 - Distance entre 2 acteurs",
               "4 - Centralité d'un acteur",
               "5 - Acteur le plus central du graphe",
               "6 - Distance maximum entre 2 acteurs",
               "7 - Quitter l'application"
               ]
titre="Veuillez choisir une des options se trouvant ci-dessous"

# Affichages de l'application

def choix_option():
    valide=False
    while(not valide):
        choix = input("Entrez le numéro d'une des options entre 1 et 7: ")
        if(choix==""):
            print("Vous n'avez pas rentré de numéro")
            print("")
        try:
            opt = int(choix)
        except:
            print("Vous devez rentrer un numéro qui est compris entre 1 et 7")
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
        if(choix!="Oui" and choix!="Non"):
            print("Veuillez répondre par Oui ou par Non")
            continue
        match choix:
            case "Oui":
                return True
            case "Non":
                return False

        

# Fonctions appelant les fonctions dans requetes.py concernées par l'option

def option_collaborateurs_2_acteurs():# paramètres si besoin
    return None
def option_acteurs_a_distance_k():# paramètres si besoin
    return None
def option_distance_entre_2_acteurs():# paramètres si besoin
    return None
def option_centralite_acteur():# paramètres si besoin
    return None
def option_acteur_central():# paramètres si besoin
    return None
def option_distance_max_entre_2_acteurs():# paramètres si besoin
    return None



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
                break
        if(not continuer_utilisation()):
            utilisation=False
        print("")

application()
