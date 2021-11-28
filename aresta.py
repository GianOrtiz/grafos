class Aresta:

    def __init__(self, u, v, peso):
        self._u = u
        self._v = v
        self._peso = peso
    
    @property
    def u(self):
        return self._u
    
    @property
    def v(self):
        return self._v
    
    @property
    def peso(self):
        return self._peso
