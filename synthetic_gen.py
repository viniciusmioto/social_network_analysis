import networkx as nx
import random

PATH = './data/'

def generate_ba_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(10, 20)
        edges = random.randint(1, 5)
        G = nx.barabasi_albert_graph(nodes, edges)
        file = PATH + str(i) + '.gexf'
        nx.write_gexf(G, file)


def main():
    generate_ba_graph(5)


if __name__ == "__main__":
    main()

