from typing import List, Callable, Dict, Tuple

class Grafo:

    def __init__(self, vertices: List[Tuple[str, str]] = None, arestas: List[Tuple[str, str]] = None, map_peso: Callable[[str, str], int] = None):
        if vertices is None or arestas is None or map_peso is None:
            self.__num_arestas = 0
            self.__vertices = {}
            self.__map_peso = None
        else:
            self.__num_arestas = len(arestas)
            self.__vertices: Dict[str, Dict[str, int]] = {}
            for vertice in vertices:
                v, rotulo = vertice
                self.__vertices[vertice] = {
                    'rotulo': rotulo,
                }
            for aresta in arestas:
                u, v = aresta
                self.__vertices[u][v] = map_peso(u, v)
                self.__vertices[v][u] = map_peso(u, v)
            self.__map_peso = map_peso
    
    def qtdVertices(self) -> int:
        return len(self.__vertices)

    def qtdArestas(self) -> int:
        return self.__num_arestas

    def grau(self, v: str) -> int:
        return len(self.__vertices[v])

    def rotulo(self, v: str) -> str:
        return self.__vertices[v]['rotulo']

    def vizinhos(self, v: str) -> List[str]:
        return self.__vertices[v].keys()
    
    def haAresta(self, u: str, v: str) -> bool:
        return self.__vertices[u].get(v) is not None
    
    def peso(self, u: str, v: str) -> int:
        return self.__vertices[u][v]
    
    def ler(self, arquivo: str):
        self.__vertices: Dict[str, Dict[str, int]] = {}
        with open(arquivo) as f:
            lines = f.readlines()
            reading_edges = False
            i = 0
            while i != len(lines):
                line = lines[i]
                if line.startswith("*vertices"):
                    num_vertices = int(line.split()[1])
                    for j in range(num_vertices):
                        line = lines[i+j+1]
                        index, rotulo = line.split()
                        self.__vertices[index] = {
                            'rotulo': rotulo,
                        }
                    # Pula todos os vértices e o header de arestas.
                    i += num_vertices + 1
                else:
                    u, v, peso = line.split()
                    self.__vertices[u][v] = int(peso)
                    self.__vertices[v][u] = int(peso)
                i += 1

    def busca_em_largura(self, index: str):
        # Marca vértices como não visitados.
        vertices = {}
        for key in self.__vertices.keys():
            vertices[key] = False
        
        level = 0
        levels = {
            level: [index],
        }
        level += 1
        vertice_atual = self.__vertices[index]
        vertices[index] = True
        vertices_a_visitar = vertice_atual.keys()
        while len(vertices_a_visitar) > 1:
            novos_vertices_a_visitar = []
            for key in vertices_a_visitar:
                if key != 'rotulo':
                    if not vertices[key]:
                        vertices[key] = True
                        if levels.get(level) is None:
                            levels[level] = [key]
                        else:
                            levels[level].append(key)
                        for child in self.__vertices[key].keys():
                            if vertices.get(child) is not None and vertices.get(child) is False:
                                novos_vertices_a_visitar.append(child)
            vertices_a_visitar = novos_vertices_a_visitar
            level += 1
        return levels