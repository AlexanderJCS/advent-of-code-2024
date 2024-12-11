import part_1


def valid(data, pos, current):
    return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data) and data[pos[1]][pos[0]] == current + 1


def trailhead_score(data, trailhead):
    num_nines = 0
    stack = [trailhead]
    
    while stack:
        current_pos = stack.pop()
        current = data[current_pos[1]][current_pos[0]]
        
        if current == 9:
            num_nines += 1
            continue
        
        for position in part_1.get_test_positions(current_pos):
            if valid(data, position, current):
                stack.append(position)
    
    return num_nines


def main():
    data = part_1.parse_input()
    trailheads = part_1.find_trailheads(data)
    
    total = 0
    for trailhead in trailheads:
        score = trailhead_score(data, trailhead)
        total += score
    
    print(total)


if __name__ == "__main__":
    main()
