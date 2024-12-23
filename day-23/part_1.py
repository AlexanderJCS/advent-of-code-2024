import itertools

import networkx as nx


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    conns = {}
    
    for line in data:
        split = line.split("-")
        conns[split[0]] = conns.get(split[0], set()) | {split[1]}
        conns[split[1]] = conns.get(split[1], set()) | {split[0]}
    
    return conns


def main():
    connections = parse_input()
    
    combos = [
        (a, b, c)
        for a, b, c in itertools.combinations(connections.keys(), 3)
        if (a in connections[b] and b in connections[c] and a in connections[c]
            and (a[0] == "t" or b[0] == "t" or c[0] == "t"))
    ]

    print(len(combos))


if __name__ == "__main__":
    main()
