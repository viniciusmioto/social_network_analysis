import networkx as nx
import statistics as sts
import numpy as np

path = './graphs/'
file_labels = open('graph.Labels')
lines = file_labels.readlines()

base_features = open('graphs_db_new_features.csv', "w")
base_features.write("graph_type," +
                    "clustering_coef," +
                    "first_quartile," +
                    "second_quartile," +
                    "third_quartile,"
                    "max_triangles," +
                    "max_degree," +
                    "qtd_max_degree," +
                    "min_degree," +
                    "qtd_min_degree," +
                    "avg_degree," +
                    "density," +
                    "is_power_law" +
                    "\n")


for line in lines:
    file = str(line)[2:-1]

    graph_type = file[0:4]

    print(file)

    graph = nx.read_gexf(path+file)

    second_quartile = sts.median(dict(nx.degree(graph)).values())

    third_quartile = np.percentile(
        list(dict(nx.degree(graph)).values()), [75])[0]

    max_triangles = max(nx.triangles(graph).values())

    max_degree = max(dict(nx.degree(graph)).values())

    min_degree = min(dict(nx.degree(graph)).values())

    avg_degree = sts.mean(dict(nx.degree(graph)).values())

    qtd_max_degree = list(dict(nx.degree(graph)).values()).count(max_degree)

    qtd_min_degree = list(dict(nx.degree(graph)).values()).count(min_degree)

    density = nx.density(graph)

    base_features.write(str(graph_type) + ",")

    base_features.write(str(nx.average_clustering(graph)) + ",")

    base_features.write(str(np.percentile(
        list(dict(nx.degree(graph)).values()), [25])[0]) + ",")

    base_features.write(str(second_quartile) + ",")

    base_features.write(str(third_quartile) + ",")

    base_features.write(str(max_triangles) + ",")

    base_features.write(str(max_degree) + ",")

    base_features.write(str(qtd_max_degree) + ", ")

    base_features.write(str(min_degree) + ", ")

    base_features.write(str(qtd_min_degree) + ",")

    base_features.write(str(avg_degree) + ",")

    base_features.write(str(density) + ",")
    
    base_features.write(str(line[0:1]) + "\n")

    del graph
