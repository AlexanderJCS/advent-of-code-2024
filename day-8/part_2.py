import part_1


def get_antinodes(p1, p2, bounds):
    m, b = part_1.get_line_equation(p1, p2)
    
    x_offset = abs(p1[0] - p2[0])
    
    lesser_x = min(p1[0], p2[0])
    greater_x = max(p1[0], p2[0])
    
    # extend in the +x direction
    x = greater_x
    antinodes = []
    while True:
        y_position = round(part_1.sample_linear_equation(m, b, x))
        
        if not part_1.in_bounds((x, y_position), bounds):
            break
        
        antinodes.append((round(x), y_position))
        x += x_offset
    
    x = lesser_x
    while True:
        y_position = round(part_1.sample_linear_equation(m, b, x))
        
        if not part_1.in_bounds((x, y_position), bounds):
            break
        
        antinodes.append((round(x), y_position))
        x -= x_offset
    
    return antinodes


def main():
    antennas, bounds = part_1.parse()
    
    antinodes = set()
    
    for antenna, points in antennas.items():
        points_list = list(points)
        
        for i, p1 in enumerate(points_list):
            for p2 in points_list[i + 1:]:
                new_antinodes = get_antinodes(p1, p2, bounds)
                antinodes.update(new_antinodes)
    
    print(len(antinodes))


if __name__ == "__main__":
    main()
