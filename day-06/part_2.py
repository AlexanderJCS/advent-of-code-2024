import part_1


def is_infinite_loop(data: list[str], walls: set) -> bool:
    prev_places_headings: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    position = part_1.guard_location(data)
    heading = (0, -1)
    bounds = (len(data[0]), len(data))
    
    while bounds[0] > position[0] >= 0 and bounds[1] > position[1] >= 0:
        if (position, heading) in prev_places_headings:
            return True
        
        prev_places_headings.add((position, heading))
        new_position = (position[0] + heading[0], position[1] + heading[1])
        while new_position in walls:
            heading = part_1.rotate_90(*heading)
            new_position = (position[0] + heading[0], position[1] + heading[1])
        
        position = new_position
    
    return False


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    places_visited = part_1.get_places_visited(data)
    
    walls = part_1.wall_locations(data)
    
    infinite_loops = 0
    for place in places_visited:
        walls.add(place)
        
        if is_infinite_loop(data, walls):
            infinite_loops += 1
        
        walls.remove(place)
    
    print(infinite_loops)


if __name__ == "__main__":
    main()
