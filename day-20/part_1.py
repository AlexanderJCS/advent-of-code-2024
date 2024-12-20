from collections import Counter
import math
from functools import cache


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()

    start = (-1, -1)
    end = (-1, -1)
    walls = set()
    
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "S":
                start = (x, y)
            elif ch == "E":
                end = (x, y)
            elif ch == "#":
                walls.add((x, y))
    
    bounds = (len(data[0]), len(data))
    
    return frozenset(walls), start, end, bounds


def path(start, end, walls):
    traversed = {}
    score = 0

    pos = start

    while pos != end:
        traversed[pos] = score
        
        for direction in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            
            if new_pos in traversed or new_pos in walls:
                continue
            
            score += 1
            pos = new_pos
            break
    
    traversed[pos] = score
    return traversed


def manhattan(radius: int):
    return [
        (x, y)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        if abs(x) + abs(y) <= radius + 1
    ]


def shortcut(pos, radius, current_score, orig_path, traversed=None):
    # todo: this function needs to be recursive
    
    if traversed is None:
        traversed = set()
    
    shortcuts = []
    
    traversed.add(pos)
    for offset in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        offset_pos = (pos[0] + offset[0], pos[1] + offset[1])
        
        if offset_pos not in orig_path:
            traversed = set(traversed)
            shortcuts.extend(shortcut(pos, ))
    
    return shortcuts


def main():
    walls, start, end, bounds = parse_input()
    orig_path = path(start, end, walls)
    
    print(shortcut((1, 3), 2, orig_path[(1, 3)], orig_path))
    
    # upper_bound = search_iterative(start, end, walls, bounds, cheats=0)[0]
    # quicker = search_iterative(start, end, walls, bounds, score_cap=upper_bound)
    # savings = [upper_bound - time for time in quicker]
    # savings_count = dict(Counter(savings))
    #
    # big_savings = sum(count for saving, count in savings_count.items() if saving >= 100)
    # print(big_savings)


if __name__ == "__main__":
    main()
