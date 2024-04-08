import networkx as nx
class Donnees:

    def __init__(self):
        self.file = open('data.json', 'r')
        self.collab = {} #clé nom d'acteur, valeur leur collaboration effectué 
        self.G = nx.Graph()

    def draw_graph(self):
        nx.draw(self.G)
    
    def chercher_collab(self,acteur):
        f = self.file
        
        for ligne in f: #chercher l'acteur et ajouter les collab dans le dic
            print(ligne)
            ligne
            
        
        
        f.close()
test = Donnees()
test.chercher_collab('sasa')