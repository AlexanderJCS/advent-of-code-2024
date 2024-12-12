import itertools
import part_1


def get_num_sides(region: set, bounds: tuple):
    corners = 0

    # marching-cubes inspired technique where you analyze the permutations of a marching 2x2 grid
    # number of corners = number of edges
    for y, x in itertools.product(range(-1, bounds[1]), range(-1, bounds[0])):
        top_left = (x, y) in region
        bottom_left = (x, y + 1) in region
        top_right = (x + 1, y) in region
        bottom_right = (x + 1, y + 1) in region

        # odd-number
        grid_spaces = sum([top_left, bottom_left, top_right, bottom_right])
        corners += grid_spaces % 2
        
        # even, but diagonal
        if grid_spaces == 2 and ((top_left and bottom_right) or (top_right and bottom_left)):
            corners += 2
    
    return corners


def get_bulk_price(regions: set, bounds: tuple):
    return sum(
        part_1.get_region_area(region) * get_num_sides(region, bounds)
        for region in regions
    )


def main():
    data = part_1.parse_input()
    regions = part_1.get_all_regions(data)
    
    print(get_bulk_price(regions, (len(data[0]), len(data))))
    

if __name__ == "__main__":
    main()
