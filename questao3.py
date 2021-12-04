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
    tem_ciclo, ciclo = grafo.ciclo_euleriano()
    if not tem_ciclo:
        print('0')
    else:
        print('1')
        print(','.join(ciclo))

if __name__ == '__main__':
    main()