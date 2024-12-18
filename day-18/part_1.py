import collections


def parse_input(first_n=None):
    coords = []
    
    with open("input.txt") as f:
        for line in f.read().splitlines():
            if not line:
                continue
            
            if first_n is not None and len(coords) >= first_n:
                break
            
            split = line.split(",")
            coords.append((int(split[0]), int(split[1])))
    
    return coords


def search(corrupted: set, search_point: tuple):
    queue = collections.deque()
    queue.append(((0, 0), 0))  # coords, score, traversed
    
    visited = set()
    min_score = float("inf")
    
    while queue:
        coords, score = queue.popleft()
        
        if coords in visited:
            continue
        
        visited.add(coords)
        
        if score > min_score:
            continue
        
        if coords == search_point:
            min_score = score
            continue
        
        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_coords = (coords[0] + direction[0], coords[1] + direction[1])
            
            if new_coords in visited or new_coords in corrupted:
                continue
            
            if new_coords[0] < 0 or new_coords[0] > search_point[0] or new_coords[1] < 0 or new_coords[1] > search_point[1]:
                continue
            
            queue.append((new_coords, score + 1))
    
    return min_score


def main():
    corrupted = set(parse_input(1024))
    print(search(corrupted, (70, 70)))


if __name__ == "__main__":
    main()
