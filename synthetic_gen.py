import networkx as nx
import numpy as np
import random

PATH = './data/'

def write_label(type, index, is_power_law):
    with open('graphs.Labels', 'a+') as f:
        line = type + str(index) + '.gexf' + ' ' + str(is_power_law) + '\n'
        f.write(line)

def save_graph(graph, type, index):
    file = PATH + type + str(index) + '.gexf'
    nx.write_gexf(graph, file)


def gen_ba_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        edges = random.randint(1, 5)
        G = nx.barabasi_albert_graph(nodes, edges)
        save_graph(G, 'ba', i)
        write_label('ba', i, 1)

def gen_scale_free_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.scale_free_graph(nodes)
        save_graph(G, 'sf', i)
        write_label('sf', i, 1)


def gen_powerlaw_cluster_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(10000, 100000)
        edges = random.randint(1, 5)
        probability = 0.4
        G = nx.powerlaw_cluster_graph(nodes, edges, probability)
        save_graph(G, 'pc', i)
        write_label('pc', i, 1)


def gen_grid_graph(quantity):
    for i in range(0, quantity):
        n = random.randint(10, 100)
        G = nx.grid_graph(dim=[n, n])
        save_graph(G, 'gr', i)
        write_label('gr', i, -1)

def gen_regular_graph(quantity):
    for i in range(0, quantity):
        degree = 1
        nodes = 1
        while ((degree * nodes) % 2 != 0):
            degree = random.randint(1, 10)
            nodes = random.randint(10, 100)
        G = nx.random_regular_graph(degree, nodes)
        save_graph(G, 'rg', i)
        write_label('rg', i, -1)


def gen_complete_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(100, 1000)
        G = nx.complete_graph(nodes)
        save_graph(G, 'co', i)
        write_label('co', i, -1)


def gen_path_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.path_graph(nodes)
        save_graph(G, 'pt', i)
        write_label('pt', i, -1)


def gen_cycle_graph(quantity):
    for i in range(0, quantity):
        nodes = random.randint(1000, 10000)
        G = nx.cycle_graph(nodes)
        save_graph(G, 'cy', i)
        write_label('cy', i, -1)


def gen_ladder_graph(quantity):
    for i in range(0, quantity):
        length = random.randint(1000, 10000)
        G = nx.ladder_graph(length)
        save_graph(G, 'ld', i)
        write_label('ld', i, -1)


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
        write_label('ln', i, -1)


def main():
    gen_ba_graph(2) # 599
    gen_scale_free_graph(2) # 200
    gen_powerlaw_cluster_graph(2) # 300
    gen_grid_graph(2) # 200
    gen_regular_graph(2) # 200
    gen_complete_graph(2) # 200
    gen_path_graph(2) # 150
    gen_cycle_graph(2) # 100
    gen_ladder_graph(2) # 250
    gen_lognormal_graph(2) # 300


if __name__ == "__main__":
    main()

