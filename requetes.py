from tkinter.tix import TEXT
import networkx as nx
import matplotlib.pyplot as plt
import json

class Donnees:

    def __init__(self):
        self.titres = {"titres":set()} 
        self.casts = {"casts":[]}
        self.directeurs = {'directeurs':set()}
        self.producteurs = {'producteurs':set()}
        self.companies = {'companies':set()}
        self.annees = {'annees':set()}

        # Attributs pour les requêtes
        self.collaborateurs = {} #clé tuple des acteurs, valeur leur collaborations effectué dans un ensemble 

        # Graphe
        self.G = nx.Graph()

    def draw_graph(self):
        nx.draw(self.G)
        plt.show()
        
    def split_name(self,txt):
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
    
    def ajout_donnees(self):
        f = open('data_100.txt', 'r')
        for ligne in f:
            dict_ligne=json.loads(ligne)
            self.titres['titres'].add(dict_ligne['title'])
            self.casts['casts'].append(list(dict_ligne['cast']))
            if('directors' in dict_ligne):
                self.directeurs['directeurs'].update(dict_ligne['directors'])
            if('producers' in dict_ligne):
                self.producteurs['producteurs'].update(dict_ligne['producers'])
            if('companies' in dict_ligne):
                self.companies['companies'].update(dict_ligne['companies'])
            if('year' in dict_ligne):
                self.annees['annees'].add(dict_ligne['year'])
        f.close()

    def json_vers_nx(self):
            f = open('data_100.txt', 'r')
            for ligne in f:
                dict_ligne = json.loads(ligne)
                acteurs=dict_ligne['cast']
                for acteur in acteurs:
                    acteur1 = self.split_name(acteur)
                    if not self.G.has_node(acteur1):
                        self.G.add_node(acteur1)
                    acteurs.remove(acteur)
                    for act in acteur:
                        self.G.add_edge(acteur1,self.split_name(act))
                
            


    def collaborateurs_communs(self, acteur1, acteur2):
        """Fonction renvoyant l'ensemble des collaborations de 2 acteurs précisés en paramètre

        Args:
            acteur1 (str): le premier acteur
            acteur2 (str): le deuxième acteur

        Returns:
            set: l'ensemble des collaborations
        """        
        if not ((acteur1,acteur2) in self.collaborateurs or (acteur2,acteur1) in self.collaborateurs):
            acteurs={acteur1, acteur2}
            self.collaborateurs[(acteur1,acteur2)] = set()
            for cast_list in self.casts.values():
                for cast in cast_list:
                    if(acteur1 in cast and acteur2 in cast):
                        self.collaborateurs[(acteur1, acteur2)].update(cast)
            self.collaborateurs[(acteur1, acteur2)]-=acteurs
        return self.collaborateurs
        

    def collaborateurs_proches(self,u,k):
        """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.

        Parametres:
            u: le sommet de départ
            k: la distance depuis u
        """
        if u not in self.G.nodes:
            print(u,"est un illustre inconnu")
            return None
        collabo = set()
        collabo.add(u)
        print(collabo) 
        for i in range(k):
            collaborateurs_directs = set()
            for c in collabo:
                for voisin in self.G.adj[c]:
                    if voisin not in collabo:
                        collaborateurs_directs.add(voisin)
            collabo = collabo.union(collaborateurs_directs)
        return collabo
    
    def distance(self,u,v):
        """Fonction donnant la distance entre 2 acteurs

        Args:
            u (str): un premier acteur
            v (str): un deuxième acteur
        """        
        if u not in self.G.nodes:
            print(u,"est un illustre inconnu")
            return None
        collabo = set()
        collabo.add(u)
        print(collabo) 
        for i in range(self.G.number_of_nodes()):
            collaborateurs_directs = set()
            for c in collabo:
                for voisin in self.G.adj[c]:
                    if voisin not in collabo:
                        collaborateurs_directs.add(voisin)
            collabo = collabo.union(collaborateurs_directs)
            if v in collabo:
                return i
        return i
    
test = Donnees()
test.ajout_donnees()
test.json_vers_nx()
#print(list(test.G.nodes()))
#print(test.split_name("[[Rosa Maria Sardà]]"))
#print(test.distance("Rosa Maria Sardà","Bruce Campbell"))



