import networkx as nx
import statistics as sts

path = './graphs/'
file_labels = open(path + 'target.Labels')
lines = file_labels.readlines()

base_features = open('graphs_db.csv',"w")
base_features.write("max_degree, " +
					"qtd_max_degree, " +
			 		"min_degree, " +
					"qtd_min_degree, " +
					"avg_degree, " +
					"density, " +
					"is_power_law\n")

for line in lines:
    file = str(line)[2:-1]

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
    base_features.write(str(density) + ", ")
    base_features.write(str(line[0]) + "\n")
	
    del graph
