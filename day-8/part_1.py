

def parse():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    bounds = (len(data[0]), len(data))
    
    antennas = {}
    
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == ".":
                continue
            
            if not antennas.get(col):
                antennas[col] = set()
            
            antennas.get(col).add((x, y))
    
    return antennas, bounds


def get_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def get_line_equation(p1, p2):
    m = get_slope(p1, p2)
    b = p1[1] - m * p1[0]
    
    return m, b


def sample_linear_equation(m, b, x):
    return m * x + b


def get_antinode(p1, p2):
    m, b = get_line_equation(p1, p2)
    
    x_offset = abs(p1[0] - p2[0])
    
    lesser_x = min(p1[0], p2[0])
    greater_x = max(p1[0], p2[0])
    
    antinode_p1 = [lesser_x - x_offset, sample_linear_equation(m, b, lesser_x - x_offset)]
    antinode_p2 = [greater_x + x_offset, sample_linear_equation(m, b, greater_x + x_offset)]
    
    antinode_p1 = tuple(map(round, antinode_p1))
    antinode_p2 = tuple(map(round, antinode_p2))
    
    return antinode_p1, antinode_p2


def in_bounds(p, bounds):
    return 0 <= p[0] < bounds[0] and 0 <= p[1] < bounds[1]


def antenna_at(p, antennas):
    return next((antenna for antenna, points in antennas.items() if p in points), None)


def main():
    antennas, bounds = parse()
    
    antinodes = set()
    
    for antenna, points in antennas.items():
        points_list = list(points)
        
        for i, p1 in enumerate(points_list):
            for p2 in points_list[i + 1:]:
                antinode_p1, antinode_p2 = get_antinode(p1, p2)
                
                if in_bounds(antinode_p1, bounds):
                    antinodes.add(antinode_p1)
                
                if in_bounds(antinode_p2, bounds):
                    antinodes.add(antinode_p2)
    
    print(antinodes)
    print(len(antinodes))


if __name__ == "__main__":
    main()
