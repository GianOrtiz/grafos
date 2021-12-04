import sys
import os

from grafo import Grafo

def main():
    # Receive arguments from command line.
    args = sys.argv

    # Check if the lenght of args is correct.
    if len(args) < 3:
        print('Missing file and graph index!')
        exit(1)
    elif len(args) > 3:
        print('Receive more than file and graph index arguments!')
        exit(1)

    index, filename, index = args
    grafo = Grafo([], [])
    grafo.ler(filename)
    s = grafo.get_vertice(index)
    b, D, A = grafo.bellman_ford(s)
    if b:
        for key in A.keys():
            if key != s.index:
                caminho = key
                current_key = A[key]
                peso_caminho = D[key]
                while current_key != None and current_key != s.index:
                    caminho = '{0},{1}'.format(current_key, caminho)
                    peso_caminho += D[current_key]
                    current_key = A[current_key]
                caminho = '{0},{1}'.format(s.index, caminho)
            else:
                caminho = s.index
                peso_caminho = 0

            print('{0}: {1}; d={2}'.format(key, caminho, peso_caminho))

if __name__ == '__main__':
    main()
