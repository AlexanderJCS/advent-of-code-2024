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


def shortcut(pos, radius, current_score, orig_path, bounds, traversed=None):
    if traversed is None:
        traversed = set()
    
    if radius < 0:
        return []
    
    shortcuts = []
    
    traversed.add(pos)
    for offset in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        offset_pos = (pos[0] + offset[0], pos[1] + offset[1])
        
        if offset_pos[0] < 0 or offset_pos[0] >= bounds[0] or offset_pos[1] < 0 or offset_pos[1] >= bounds[1]:
            continue
        
        if offset_pos not in orig_path and offset_pos not in traversed:
            traversed = set(traversed)
            shortcuts.extend(shortcut(offset_pos, radius - 1, current_score + 1, orig_path, bounds))
        else:
            shortcuts.append(orig_path[offset_pos] - (current_score + 1))
    
    return shortcuts


def main():
    walls, start, end, bounds = parse_input()
    orig_path = path(start, end, walls)
    
    all_shortcuts = {}
    
    for coord in orig_path:
        shortcuts = shortcut(coord, 2, orig_path[coord], orig_path, bounds)
        
        if shortcuts:
            all_shortcuts[max(shortcuts)] = all_shortcuts.get(max(shortcuts), 0) + 1
    
    print(all_shortcuts)


if __name__ == "__main__":
    main()
