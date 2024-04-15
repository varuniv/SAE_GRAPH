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
        self.collaborateurs = {} #clé nom d'acteur, valeur leur collaboration effectué 

        # Graphe
        #self.G = nx.Graph()

    def draw_graph(self):
        pass
        #nx.draw(self.G)
    
    def ajout_donnees(self):
        f = open('data_court.txt', 'r')
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
        print(self.casts)

    
test = Donnees()
test.ajout_donnees()
