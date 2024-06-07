from tkinter.tix import TEXT
import networkx as nx
import matplotlib.pyplot as plt
import json
    
def split_name(txt):
    """traite le texte donné 

    Args:
        txt (str): texte issue de file 

    Returns:
        str: le texte traité
    """    
    txt = txt.replace('[', '').replace(']', '').replace("'", '')
    i = len(txt)
    if "(" in txt:
        i = min(i, txt.index("("))
    if "<" in txt:
        i = min(i, txt.index("<"))
    if "|" in txt:
        i = min(i, txt.index("|"))
    txt = txt[:i]
    return txt



def json_vers_nx(chemin):
        """transforme les données des acteurs et leurs collaborations en graphe avec les acateurs en forme de noeud et 
        les collaborations comme une arrete avec un autre acteur    

        Args:
            chemin (str): chemin vers le fichier

        Returns:
            Graph: graphe des acteurs
        """          
        G = nx.Graph()
        f = open(chemin, 'r')
        for ligne in f:
            dict_ligne = json.loads(ligne)
            acteurs=dict_ligne['cast']
            tmp = set()
            for acteur in acteurs:
                    acteur1 = split_name(acteur)
                    if not G.has_node(acteur1):
                        G.add_node(acteur1)
                        tmp.add(acteur1) 
                    for act in tmp:
                        if act != acteur1:
                            G.add_edge(acteur1,act)
        return G


def collaborateurs_communs(G, u, v):
    """Fonction renvoyant l'ensemble des collaborations de 2 acteurs précisés en paramètre

    Args:
        u (str): le premier acteur
        v (str): le deuxième acteur

    Returns:
        set: l'ensemble des collaborations
    """
    collab = set() 
    if u  in G.nodes() and v in G.nodes():
        c1 = G.adj[u] 
        c2 = G.adj[v]
        for act in c1:
            for act2 in c2:
                if act == act2:
                    collab.add(act) 
    return collab
        



def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.

    Parametres:
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collabo = set()
    collabo.add(u)
    print(collabo) 
    for i in range(k):
        collaborateurs_directs = set()
        for c in collabo:
            for voisin in G.adj[c]:
                if voisin not in collabo:
                    collaborateurs_directs.add(voisin)
        collabo = collabo.union(collaborateurs_directs)
    return collabo

def est_proche(G,u,v,k=1):
    """renvoie True si v est proche de u pour une distance donné, sinon False. La distance par défaut est 1.

    Args:
        G (graph): graphe des acteurs
        u (str): acteur
        v (str): acteur
        k (int, optional): la distance. Par défaut égal à 1

    Returns:
        bool: True si v est proche de u sur la distance donné, sinon False
    """   
    return v in collaborateurs_proches(G,u,k)

def distance_naive(G,u,v):
    """Fonction donnant la distance entre 2 acteurs, renvoie None si la distance entre les 2 acteurs est introuvable

    Args:
        G : graphe 
        u (str): un premier acteur
        v (str): un deuxième acteur
    
    Returns:
        int: distance entre les 2 acteurs.  None si la distance est introuvable
    """   
    d = 1
    m = G.number_of_nodes()
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    if v not in G.nodes:
        print(v,"est un illustre inconnu")
        return None
    while d <= m :
        if est_proche(G,u,v):
            return d
        else:
            d += 1
    return None


def distance(G,u,v):
    """Fonction donnant la distance entre 2 acteurs, renvoie None si la distance entre les 2 acteurs est introuvable

    Args:
        G : graphe
        u (str): un premier acteur
        v (str): un deuxième acteur
        
    Returns:
        int: distance entre les 2 acteurs.  None si la distance est introuvable
    """       
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    if v not in G.nodes:
        print(v,"est un illustre inconnu")
        return None
    collabo = set()
    collabo.add(u)
    for i in range(G.number_of_nodes()):
        collaborateurs_directs = set()
        for c in collabo:
            for voisin in G.adj[c]:
                if voisin not in collabo:
                    collaborateurs_directs.add(voisin)
        collabo = collabo.union(collaborateurs_directs)
        if v in collabo:
            return i
    if i == G.number_of_nodes():
        if est_proche(G,u,v):
            return i
        else:
            return None
    else :
        return None

def centralite(G,u): 
    """renvoie la centralité d'un acteur

    Args:
        G (graph): graphe des acteurs
        u (str): nom d'acteur

    Returns:
        int: centralité de l'acteur
    """    
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    distance = nx.shortest_path_length(G,source=u)
    return max(distance.values())

def centre_hollywood(G):
    """renvoie la centralité du graphe

    Args:
        G (graph): graphe

    Returns:
        str: l'acteur au centre du graphe
    """    
    listG = list(G.nodes)
    min = None
    acteur = None 
    for i in range(G.number_of_nodes()):
        tmp = centralite(G,listG[i])
        if min == None or min > tmp:
            min = tmp
            acteur = listG[i]
    return acteur     

def eloignement_max(G:nx.Graph):
    """renvoie l'éloignement maximum du graphe donné

    Args:
        G (graph): graphe

    Returns:
        int: l'éloignement maximum
    """    
    listG = list(G.nodes)
    max = None
    acteur = None 
    for i in range(G.number_of_nodes()):
        tmp = centralite(G,listG[i])
        if max == None or max < tmp:
            max = tmp
            acteur = listG[i]
    return max 