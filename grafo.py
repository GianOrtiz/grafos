from typing import List, Callable, Dict, Tuple

class Grafo:

    def __init__(self, vertices: List[Tuple[str, str]], arestas: List[Tuple[str, str]], map_peso: Callable[[str, str], int]):
        self.__num_arestas = len(arestas)
        self.__vertices: Dict[str, Dict[str, int]] = {}
        for vertice in vertices:
            v, rotulo = vertice
            self.__vertices[vertice] = {
                'rotulo': routlo,
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
            for i in range(len(lines)):
                line = lines[i]
                if line.startswith("*vertices"):
                    num_vertices = int(line.split()[1])
                    for j in range(num_vertices):
                        line = lines[i+j+1]
                        index, rotulo = line.split()
                        self.__vertices[index] = {
                            'rotulo': rotulo,
                        }
                    i += num_vertices
                else:
                    u, v, peso = line.split()
                    self.__vertices[u][v] = peso
                    self.__vertices[v][u] = peso
