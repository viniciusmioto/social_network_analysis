# Social Network Analysis

## Supervised Learning Algorithms
* K-Nearest Neighbors
* Support Vector Machines
* Random Forest
* Gradient Boosting

## Unsupervised Learning Algorithms
* K-Means
* DBSCAN

## Types of graphs

### Real World

* amzn: [Amazon Networks](https://snap.stanford.edu/data/amazon-meta.html)
* caid: [CAIDA AS Relationships Datasets](https://snap.stanford.edu/data/as-caida.html)
* citt: [Citation Networks](https://snap.stanford.edu/data/cit-HepTh.html)
* clab: [Collaboration Networks](https://snap.stanford.edu/data/ca-AstroPh.html)
* emal: [EU Email Communication Network](https://snap.stanford.edu/data/email-EuAll.html)
* euss: [EuroSis web-mapping](https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781783987405/9/ch09lvl1sec97/exploring-the-web-and-internet-domain-eurosis-web-mapping-study)
* gloc: [Brightkite ocations by checking-in](https://snap.stanford.edu/data/loc-Brightkite.html)
* gnut: [Gnutella peer-to-peer network](http://snap.stanford.edu/data/p2p-Gnutella08.html)
* smcd: [Social Media](https://snap.stanford.edu/data/ego-Facebook.html)
* webn: [Web Networks](https://snap.stanford.edu/data/web-BerkStan.html)
* bion: [Biological](http://graphdatasets.com/bio.php)
* enzy: [Enzymes](https://github.com/MLDroid/graph2vec_tf)
* brai: [Brain networks](http://graphdatasets.com/bn.php)
* eclg: [Ecology](http://graphdatasets.com/eco.php)
* road: [Road Maps](http://graphdatasets.com/road.php)
* infr: [Infrastructure](http://graphdatasets.com/inf.php)
* ecnm: [Economics](http://graphdatasets.com/econ.php)

### Synthetic
* ba: [Barabási-Albert](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html)
* co: [Complete](https://networkx.org/documentation/stable/reference/generated/networkx.generators.classic.complete_graph.html#networkx.generators.classic.complete_graph)
* cy: [Cycle](https://networkx.org/documentation/stable/reference/generated/networkx.generators.classic.cycle_graph.html#networkx.generators.classic.cycle_graph)
* gr: [Grid](https://networkx.org/documentation/stable/reference/generated/networkx.generators.lattice.grid_graph.html#networkx.generators.lattice.grid_graph)
* ld: [Ladder](https://networkx.org/documentation/stable/reference/generated/networkx.generators.classic.circular_ladder_graph.html#networkx.generators.classic.circular_ladder_graph)
* ln: [Log-normal](https://en.wikipedia.org/wiki/Log-normal_distribution)
* pc: [PowerLaw Cluster](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.powerlaw_cluster_graph.html#networkx.generators.random_graphs.powerlaw_cluster_graph)
* pt: [Path](https://networkx.org/documentation/stable/reference/generated/networkx.generators.classic.path_graph.html#networkx.generators.classic.path_graph)
* rg: [Regular](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.random_regular_graph.html#networkx.generators.random_graphs.random_regular_graph)
* sf: [Scale Free](https://networkx.org/documentation/stable/reference/generated/networkx.generators.directed.scale_free_graph.html#networkx.generators.directed.scale_free_graph)

## Data Frame Creator

### Inputs
The input is any graph file in *.gexf* format, they must be saved in **graphs** folder

### Properties
The `graphs2csv.py` script will create a *csv* file with the following properties of your graphs:
* graph_type
* clustering_coef
* first_quartile
* second_quartile
* third_quartile
* max_triangles
* max_degree
* qtd_max_degree
* min_degree
* qtd_min_degree
* avg_degree
* density
* is_power_law

## Synthetic Graph Generator

Script to generate synthetic graphs for my undergraduate research project: Recognizing Power-Law Graphs by Machine Learning Algorithms.

### How to generate the graphs
* Chose one of the functions `gen_<type>_graph` and give the quantity of graphs in the parameter. Those functions will generate graphs from [NetworkX](https://networkx.org/)

### Data files
* The results will be saved in `graphs` directory with as a .gexf file

### Project Advisors
* [André Luis Vignatti](https://www.inf.ufpr.br/vignatti/)
* [Alane Marie de Lima](https://www.inf.ufpr.br/amlima/)
