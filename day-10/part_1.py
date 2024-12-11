

def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    return [list(map(int, line)) for line in data]


def find_trailheads(data):
    trailheads = []

    for y, row in enumerate(data):
        trailheads.extend((x, y) for x, val in enumerate(row) if val == 0)
    
    return trailheads


def valid(data, pos, current):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data) and data[pos[1]][pos[0]] == current + 1


def get_test_positions(pos):
    return [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1)
    ]


def trailhead_score(data, trailhead):
    already_traversed = set()
    
    num_nines = 0
    stack = [trailhead]
    
    while stack:
        current_pos = stack.pop()
        
        if current_pos in already_traversed:
            continue
        
        already_traversed.add(current_pos)
        
        current = data[current_pos[1]][current_pos[0]]
        
        if current == 9:
            num_nines += 1
            continue
        
        for position in get_test_positions(current_pos):
            if valid(data, position, current):
                stack.append(position)

    return num_nines


def main():
    data = parse_input()
    trailheads = find_trailheads(data)

    total = 0
    for trailhead in trailheads:
        score = trailhead_score(data, trailhead)
        total += score

    print(total)


if __name__ == "__main__":
    main()
