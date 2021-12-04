import math

from typing import List, Callable, Dict, Tuple
from aresta import Aresta
from vertice import Vertice

class Grafo:

    def __init__(self, vertices: List[Tuple[str, str]] = [], arestas: List[Tuple[str, str, int]] = [], map_peso: Callable[[str, str], int] = None):
        self._arestas = []
        for aresta in arestas:
            u, v, peso = aresta
            self._arestas.append(Aresta(u, v, peso))

        self._vertices = {}
        for vertice in vertices:
            index, rotulo = vertice
            arestas_do_vertice = []
            for aresta in arestas:
                if aresta[0] == index or aresta[1] == index:
                    arestas_do_vertice.append(aresta)
            
            self._vertices[index] = Vertice(index, rotulo, arestas_do_vertice)

    @property
    def vertices(self) -> List[Vertice]:
        vertices = []
        for v in self._vertices.values():
            vertices.append(v)
        return vertices
    
    def get_vertice(self, index: str) -> Vertice:
        return self._vertices.get(index)
    
    def qtdVertices(self) -> int:
        return len(self._vertices)

    def qtdArestas(self) -> int:
        return len(self._arestas)

    def grau(self, v: str) -> int:
        return len(self._vertices[v].arestas)

    def rotulo(self, v: str) -> str:
        return self._vertices[v].rotulo

    def vizinhos(self, v: str) -> List[str]:
        return self._vertices[v].arestas.keys()
    
    def haAresta(self, u: str, v: str) -> bool:
        return self._vertices[u].arestas.get(v) is not None
    
    def peso(self, u: str, v: str) -> int:
        return self._vertices[u].arestas[v].peso
    
    def ler(self, arquivo: str):
        self._vertices: Dict[str, Dict[str, int]] = {}
        with open(arquivo) as f:
            lines = f.readlines()
            reading_edges = False
            i = 0
            arestas = []
            vertices_indexes = []
            vertices_rotulos = []
            while i != len(lines):
                line = lines[i]
                if line.startswith("*vertices"):
                    num_vertices = int(line.split()[1])
                    for j in range(num_vertices):
                        line = lines[i+j+1]
                        index, rotulo = line.split()
                        vertices_indexes.append(index)
                        vertices_rotulos.append(index)
                    # Pula todos os vértices e o header de arestas.
                    i += num_vertices + 1
                else:
                    u, v, peso = line.split()
                    arestas.append(Aresta(u, v, int(peso)))
                i += 1

        self._arestas = arestas
        self._vertices = {}
        for i in range(len(vertices_indexes)):
            index = vertices_indexes[i]
            rotulo = vertices_rotulos[i]
            arestas_do_vertice = []
            for aresta in arestas:
                if aresta.u == index or aresta.v == index:
                    arestas_do_vertice.append(aresta)

            self._vertices[index] = Vertice(index, rotulo, arestas_do_vertice)    

    def busca_em_largura(self, index: str):
        # Marca vértices como não visitados.
        vertices = {}
        for key in self._vertices.keys():
            vertices[key] = False
        
        level = 0
        levels = {
            level: [index],
        }
        level += 1
        vertice_atual = self._vertices[index]
        vertices[index] = True
        vertices_a_visitar = vertice_atual.arestas.keys()
        while len(vertices_a_visitar) > 0:
            novos_vertices_a_visitar = []
            for key in vertices_a_visitar:
                if not vertices[key]:
                    vertices[key] = True
                    if levels.get(level) is None:
                        levels[level] = [key]
                    else:
                        levels[level].append(key)
                    for child in self._vertices[key].arestas.keys():
                        if vertices.get(child) is not None and vertices.get(child) is False:
                            novos_vertices_a_visitar.append(child)
            vertices_a_visitar = novos_vertices_a_visitar
            level += 1
        return levels

    def bellman_ford(self, v: Vertice):
        D = {}
        A = {}
        for u in self._vertices.keys():
            D[u] = math.inf
            A[u] = None
        D[v.index] = 0

        for i in range(1, len(self._vertices)):
            for aresta in self._arestas:
                if D[aresta.v] > D[aresta.u] + aresta.peso:
                    D[aresta.v] = D[aresta.u] + aresta.peso
                    A[aresta.v] = aresta.u
                if D[aresta.u] > D[aresta.v] + aresta.peso:
                    D[aresta.u] = D[aresta.v] + aresta.peso
                    A[aresta.u] = aresta.v

        for aresta in self._arestas:
            if D[aresta.v] > D[aresta.u] + aresta.peso:
                return (False, None, None)
            if D[aresta.u] > D[aresta.v] + aresta.peso:
                return (False, None, None)
        
        return (True, D, A)
