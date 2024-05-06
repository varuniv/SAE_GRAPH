#import networkx as nx
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
        #self.G = nx.Graph()

    def draw_graph(self):
        pass
        #nx.draw(self.G)
    
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

    def collab(self, acteur1, acteur2):
        if not ((acteur1,acteur2) in self.collaborateurs or (acteur2,acteur1) in self.collaborateurs):
            acteurs={acteur1, acteur2}
            self.collaborateurs[(acteur1,acteur2)] = set()
            for cast_list in self.casts.values():
                for cast in cast_list:
                    if(acteur1 in cast and acteur2 in cast):
                        self.collaborateurs[(acteur1, acteur2)].update(cast)
            self.collaborateurs[(acteur1, acteur2)]-=acteurs
        return self.collaborateurs

    
test = Donnees()
test.ajout_donnees()
test.collab("[[Marion Dougherty]]", "[[Lynn Stalmaster]]")