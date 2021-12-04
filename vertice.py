class Vertice:

    def __init__(self, index, rotulo, arestas):
        self._index = index
        self._rotulo = rotulo
        self._arestas = {}
        for aresta in arestas:
            if aresta.v is not index:
                self._arestas[aresta.v] = aresta
            else:
                self._arestas[aresta.u] = aresta
    
    @property
    def index(self):
        return self._index
    
    @property
    def rotulo(self):
        return self._rotulo
    
    @property
    def arestas(self):
        return self._arestas
