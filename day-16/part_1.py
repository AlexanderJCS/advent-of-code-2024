import math
import collections
import time


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    walls = set()
    start = (-1, -1)
    end = (-1, -1)
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "#":
                walls.add((x, y))
            elif ch == "S":
                start = (x, y)
            elif ch == "E":
                end = (x, y)
    
    return walls, start, end


def min_score(walls, start, end):
    queue = collections.deque()
    queue.append((start, (1, 0), set(), 0))
    
    min_score = math.inf
    
    iterations = 0
    start_time = time.time()
    
    min_at_pos = {}
    
    while queue:
        iterations += 1
        if iterations % 50000 == 0:
            print(f"{iterations=}, {len(queue)=}, time elapsed: {time.time() - start_time:.2f}, min score: {min_score}")
        
        pos, heading, traversed, score = queue.popleft()
        
        traversed.add(pos)
        
        if pos == end:
            min_score = min(score, min_score)
            traversed.remove(pos)
            continue
        
        if score > min_score:  # no need to continue searching
            traversed.remove(pos)
            continue
        
        if min_at_pos.get(pos, math.inf) < score:
            traversed.remove(pos)
            continue
        else:
            min_at_pos[pos] = score
        
        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if direction == (-heading[0], -heading[1]):
                continue
            
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            
            if new_pos in walls or new_pos in traversed:
                continue
            
            queue.append(
                (new_pos, direction, traversed, score + 1 + (direction != heading) * 1000)
            )
            
        traversed.remove(pos)
        
    return min_score


def main():
    walls, start, end = parse_input()
    
    print(min_score(walls, start, end))


if __name__ == "__main__":
    main()
