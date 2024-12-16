import math
import collections

import part_1


def optimal_path_tiles(walls, start, end, min_score):
    tiles = set()
    
    queue = collections.deque()
    queue.append((start, (1, 0), set(), 0))

    min_at_pos = {}
    
    while queue:
        pos, heading, traversed, score = queue.popleft()
        
        traversed = set(traversed)
        traversed.add(pos)
        
        if pos == end:
            tiles.update(traversed)
            continue
        
        if score > min_score:  # no need to continue searching
            traversed.remove(pos)
            continue
        
        state = (pos, tuple(traversed))
        if min_at_pos.get(state, math.inf) < score:
            continue
        
        min_at_pos[state] = score
        
        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if direction == (-heading[0], -heading[1]):
                continue
            
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            
            if new_pos in walls or new_pos in traversed:
                continue
            
            queue.append(
                (new_pos, direction, traversed, score + 1 + (direction != heading) * 1000)
            )
    
    return tiles


def print_best_path(walls, best_path, bounds):
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if (x, y) in best_path:
                print("O", end="")
            elif (x, y) in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()


def main():
    walls, start, end, bounds = part_1.parse_input()
    min_score = part_1.min_score(walls, start, end)
    
    best_paths = optimal_path_tiles(walls, start, end, min_score)
    
    print_best_path(walls, best_paths, bounds)
    print(len(best_paths))


if __name__ == "__main__":
    main()
