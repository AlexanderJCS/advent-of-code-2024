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


@cache
def search(
        pos: tuple,
        end: tuple,
        walls: frozenset,
        bounds: tuple,
        cheats=1,  # subtract 1 by num allowed cheats
        enabled_cheats=False,
        traversed: list | None = None,
        score: int = 0,
        score_cap: int = math.inf
) -> list[int]:
    if traversed is None:
        traversed = frozenset()
    
    # horribly inefficient but it works
    traversed = set(traversed)
    traversed.add(pos)
    
    if score > score_cap or pos[0] < 0 or pos[0] >= bounds[0] or pos[1] < 0 or pos[1] >= bounds[1]:
        return []
    
    if pos == end:
        return [score]
    
    if enabled_cheats:
        cheats -= 1
    
    savings = []
    for offset in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        offset_pos = (pos[0] + offset[0], pos[1] + offset[1])
        
        if offset_pos in traversed:
            continue
        
        is_cheat = offset_pos in walls
        if is_cheat and cheats <= 0:
            continue
        
        traversed = frozenset(traversed)
        savings.extend(search(offset_pos, end, walls, bounds, cheats, enabled_cheats or is_cheat, traversed, score + 1, score_cap))
    
    return savings


def search_iterative(
        start: tuple,
        end: tuple,
        walls: frozenset,
        bounds: tuple,
        cheats=1,  # subtract 1 by num allowed cheats
        score_cap: int = math.inf
) -> list[int]:
    stack = [(start, 0, cheats, False, set())]
    results = []
    
    while stack:
        pos, score, cheats, cheating_enabled, traversed = stack.pop()
        traversed.add(pos)
        
        if score > score_cap or pos[0] < 0 or pos[0] >= bounds[0] or pos[1] < 0 or pos[1] >= bounds[1]:
            continue
        
        if pos == end:
            results.append(score)
            continue
        
        if cheating_enabled:
            cheats -= 1
        
        for offset in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            offset_pos = (pos[0] + offset[0], pos[1] + offset[1])
            
            if offset_pos in traversed:
                continue
            
            is_cheat = offset_pos in walls
            if is_cheat and cheats <= 0:
                continue
            
            traversed = set(traversed)
            stack.append(
                (offset_pos, score + 1, cheats, cheating_enabled or is_cheat, traversed)
            )
    
    return results


def main():
    walls, start, end, bounds = parse_input()
    upper_bound = search_iterative(start, end, walls, bounds, cheats=0)[0]
    quicker = search_iterative(start, end, walls, bounds, score_cap=upper_bound)
    savings = [upper_bound - time for time in quicker]
    savings_count = dict(Counter(savings))
    
    big_savings = sum(count for saving, count in savings_count.items() if saving >= 100)
    print(big_savings)


if __name__ == "__main__":
    main()
