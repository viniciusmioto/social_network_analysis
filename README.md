# Synthetic Graph Generator

Script to generate synthetic graphs for my undergraduate research project: Recognizing Power-Law Graphs by Machine Learning Algorithms.

## How to generate the graphs
* Chose one of the functions `gen_<type>_graph` and give the quantity of graphs in the parameter. Those functions will generate graphs from [NetworkX](https://networkx.org/)

## Data files
* The results will be saved in `data` directory with as a .gexf file

## Types of graphs

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

### Advisors
* [André Luis Vignatti](https://www.inf.ufpr.br/vignatti/)
* [Alane Marie de Lima](https://www.inf.ufpr.br/amlima/)
