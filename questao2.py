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
    levels = grafo.busca_em_largura(index)
    for level in levels.keys():
        vertexes = ','.join(levels[level])
        print('{0}: {1}'.format(level, vertexes))

if __name__ == '__main__':
    main()
