import networkx as nx
import statistics as sts

path = './graphs/'

base_features = open('graphs_db.csv',"w")
base_features.write("max_degree, " +
					"qtd_max_degree, " +
			 		"min_degree, " +
					"qtd_min_degree, " +
					"avg_degree, " +
					"density\n")

for i in range(1, 5):
    file = str(i) + '.gexf'

    graph = nx.read_gexf(path+file)
    max_degree = max(dict(nx.degree(graph)).values())
    min_degree = min(dict(nx.degree(graph)).values())
    avg_degree = sts.mean(dict(nx.degree(graph)).values())
    qtd_max_degree = list(dict(nx.degree(graph)).values()).count(max_degree)
    qtd_min_degree = list(dict(nx.degree(graph)).values()).count(min_degree)
    density = nx.density(graph)

    base_features.write(str(max_degree) + ", ")
    base_features.write(str(qtd_max_degree) + ", ")
    base_features.write(str(min_degree) + ", ")
    base_features.write(str(qtd_min_degree) + ", ")
    base_features.write(str(avg_degree) + ", ")
    base_features.write(str(density) + "\n")

    del graph

