

def guard_location(input_data: list[str]) -> tuple[int, int]:
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            if letter == "^":
                return x, y
    
    return -1, -1


def wall_locations(input_data: list[str]) -> set[tuple[int, int]]:
    walls = set()
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            if letter == "#":
                walls.add((x, y))
    
    return walls


def rotate_90(x: int, y: int) -> tuple[int, int]:
    return -y, x


def get_places_visited(data: list[str]) -> set:
    prev_places = set()
    position = guard_location(data)
    heading = (0, -1)
    walls = wall_locations(data)
    bounds = (len(data[0]), len(data))
    
    while bounds[0] > position[0] >= 0 and bounds[1] > position[1] >= 0:
        prev_places.add(position)
        new_position = (position[0] + heading[0], position[1] + heading[1])
        while new_position in walls:
            heading = rotate_90(*heading)
            new_position = (position[0] + heading[0], position[1] + heading[1])
        
        position = new_position
    
    return prev_places


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    print(len(get_places_visited(data)))


if __name__ == "__main__":
    main()
