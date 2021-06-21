import networkx as nx
import numpy as np
import random

PATH = './data/'

def save_graph(graph, type, index):
    file = PATH + type + str(index) + '.gexf'
    nx.write_gexf(graph, file)


def gen_ba_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        edges = random.randint(1, 5)
        G = nx.barabasi_albert_graph(nodes, edges)
        save_graph(G, 'ba', i)


def gen_scale_free_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.scale_free_graph(nodes)
        save_graph(G, 'sf', i)


def gen_powerlaw_cluster_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(10000, 100000)
        edges = random.randint(1, 5)
        probability = 0.4
        G = nx.powerlaw_cluster_graph(nodes, edges, probability)
        save_graph(G, 'pc', i)


def gen_grid_graph(quantity):
    for i in range(0, quantity):
        n = random.randint(10, 100)
        G = nx.grid_graph(dim=[n, n])
        save_graph(G, 'gr', i)


def gen_regular_graph(quantity):
    for i in range(0, quantity):
        degree = 1
        nodes = 1
        while ((degree * nodes) % 2 != 0):
            degree = random.randint(1, 10)
            nodes = random.randint(10, 100)
        G = nx.random_regular_graph(degree, nodes)
        save_graph(G, 'rg', i)


def gen_complete_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(100, 1000)
        G = nx.complete_graph(nodes)
        save_graph(G, 'co', i)


def gen_path_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.path_graph(nodes)
        save_graph(G, 'pt', i)


def gen_cycle_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.cycle_graph(nodes)
        save_graph(G, 'cy', i)


def gen_ladder_graph(quantity):
    for i in range(0, quantity):
        length = random.randint(1000, 10000)
        G = nx.cycle_graph(length)
        save_graph(G, 'ld', i)


def gen_lognormal_graph(quantity):
    for i in range(0, quantity):
        size = random.randint(1000, 10000)
        while True:
            s = np.random.lognormal(size=size)
            array =[]
            for j in s:
                array.append(int(round(j)))
            if nx.is_valid_degree_sequence_erdos_gallai(array):
                break
    
        G=nx.configuration_model(array)
        save_graph(G, 'ln', i)

def main():
    gen_ba_graph(2)
    gen_scale_free_graph(2)
    gen_powerlaw_cluster_graph(2)
    gen_grid_graph(2)
    gen_regular_graph(2)
    gen_complete_graph(2)
    gen_path_graph(2)
    gen_cycle_graph(2)
    gen_ladder_graph(2)
    gen_lognormal_graph(2)


if __name__ == "__main__":
    main()

