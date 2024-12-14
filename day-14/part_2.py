import part_1


def positions_set(robots):
    return {tuple(robot[0]) for robot in robots}


def is_interesting(robots):
    positions = positions_set(robots)
    
    # check for 7 in a row
    for position in positions:
        for x in range(1, 7):
            if (position[0] + x, position[1]) not in positions:
                break
        
        else:  # no break
            return True
    
    return False


def main():
    dimensions = (101, 103)
    robots = part_1.parse_input()
    
    for i in range(20000):
        simulated = part_1.simulate(robots, i, dimensions)
        if is_interesting(simulated):
            print(f"\n{i}:")
            part_1.print_robots(simulated, dimensions)


if __name__ == "__main__":
    main()
