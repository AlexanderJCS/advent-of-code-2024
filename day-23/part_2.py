import networkx as nx


def parse_input() -> nx.Graph:
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    graph = nx.Graph()
    for line in data:
        split = line.split("-")
        graph.add_edge(*split)
    
    return graph


def main():
    graph = parse_input()
    
    cliques = list(nx.find_cliques(graph))
    
    largest_clique_len = 0
    largest_clique = None
    
    for clique in cliques:
        if len(clique) > largest_clique_len:
            largest_clique_len = len(clique)
            largest_clique = clique
    
    print(",".join(sorted(largest_clique)))


if __name__ == "__main__":
    main()
    