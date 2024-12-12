OFFSETS = ((0, -1), (0, 1), (1, 0), (-1, 0))


def parse_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def get_region(data: list[str], location: tuple[int, int]) -> set[tuple[int, int]]:
    region_char = data[location[1]][location[0]]
    
    locations = set()
    stack = [location]
    
    while stack:
        loc = stack.pop()
        locations.add(loc)
        
        for offset in OFFSETS:
            offset_loc = (loc[0] + offset[0], loc[1] + offset[1])
            
            if offset_loc[0] < 0 or offset_loc[0] >= len(data[0]) or offset_loc[1] < 0 or offset_loc[1] >= len(data):
                continue
            
            if offset_loc in locations:
                continue
            
            if data[offset_loc[1]][offset_loc[0]] != region_char:
                continue
            
            stack.append(offset_loc)
    
    return locations


def get_all_regions(data):
    regions = []
    scanned_areas = set()
    
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if (x, y) in scanned_areas:
                continue
            
            region = get_region(data, (x, y))
            scanned_areas = scanned_areas.union(region)
            regions.append(region)
    
    return regions


def get_region_area(region: set):
    return len(region)


def get_region_perimeter(region: set):
    perimeter = 0

    for point in region:
        for offset in OFFSETS:
            offset_point = (point[0] + offset[0], point[1] + offset[1])
            
            if offset_point not in region:
                perimeter += 1
    
    return perimeter


def get_price(regions: list[set]):
    return sum(
        get_region_area(region) * get_region_perimeter(region)
        for region in regions
    )


def main():
    data = parse_input()
    all_regions = get_all_regions(data)
    
    print(get_price(all_regions))


if __name__ == "__main__":
    main()
