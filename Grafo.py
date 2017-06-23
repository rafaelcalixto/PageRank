import networkx
import matplotlib.pyplot as plt

class Grafo():
    def __init__(self):
        self.grafo = networkx.Graph()
        self.cores = ['yellow'
                      ,'blue'
                      ,'green'
                      ,'black'
                      ,'pink'
                      ,'gray'
                      ,'white'
                      ,'brown'
                      ,'red'
                      ,'orange']
        
    def criar_grafo(self, catalogo):
        for no in catalogo:
            cor = self.cores.pop()
            for aresta in no['links']:
                self.grafo.add_edge(no['url']
                                    , aresta
                                    , weight = no['ranking']
                                    , color = cor)

        networkx.draw(self.grafo)
        plt.show()
            
        
