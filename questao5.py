from grafo import Grafo

def main():
    vertices = [
        ('1', 'rotulo1'),
        ('2', 'rotulo2'),
        ('3', 'rotulo3'),
        ('4', 'rotulo4'),
        ('5', 'rotulo5'),
    ]
    arestas = [
        ('1', '2', 2),
        ('2', '3', 4),
        ('3', '4', 7),
        ('4', '5', 1),
        ('5', '1', 9),
    ]
    grafo = Grafo(vertices=vertices, arestas=arestas)
    D = grafo.floyd_warshal()
    for i in range(len(D)):
        distanceStr = ''
        for j in D[i]:
            distanceStr += str(j) + ' '
        print('{0}: {1}'.format(str(i+1), distanceStr))
    
if __name__ == '__main__':
    main()