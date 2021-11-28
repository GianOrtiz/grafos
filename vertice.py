class Vertice:

    def __init__(self, index, rotulo, arestas):
        self._index = index
        self._rotulo = rotulo
        self._arestas = {}
        for aresta in arestas:
            self._arestas[aresta.v] = aresta
    
    @property
    def index(self):
        return self._index
    
    @property
    def rotulo(self):
        return self._rotulo
    
    @property
    def arestas(self):
        return self._arestas
