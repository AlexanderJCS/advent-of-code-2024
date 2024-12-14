import copy
import math


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()

    # format: [[position, velocity]
    robots = []

    for line in data:
        if not line:
            continue
        
        split = line.split()

        pos = split[0].split(",")
        vel = split[1].split(",")

        robot = [[int(pos[0][2:]), int(pos[1])], [int(vel[0][2:]), int(vel[1])]]
        robots.append(robot)

    return robots


def simulate(robots: list, t: int, dimensions: tuple):
    robots = copy.deepcopy(robots)
    
    for robot in robots:
        robot[0][0] += robot[1][0] * t
        robot[0][1] += robot[1][1] * t
        
        robot[0][0] %= dimensions[0]
        robot[0][1] %= dimensions[1]
    
    return robots


def robots_per_quadrant(robots: list, dimensions: tuple):
    top_left = 0
    bottom_left = 0
    top_right = 0
    bottom_right = 0
    
    for robot_pos, _ in robots:
        ratio_x = robot_pos[0] / (dimensions[0] - 1)
        ratio_y = robot_pos[1] / (dimensions[1] - 1)
        
        if abs(ratio_x - 0.5) < 0.0001 or abs(ratio_y - 0.5) < 0.0001:
            continue
        
        if ratio_x < 0.5 and ratio_y < 0.5:
            top_left += 1
        elif ratio_x < 0.5 and ratio_y > 0.5:
            bottom_left += 1
        elif ratio_x > 0.5 and ratio_y < 0.5:
            top_right += 1
        elif ratio_x > 0.5 and ratio_y > 0.5:
            bottom_right += 1
    
    return top_left, bottom_left, top_right, bottom_right


def print_robots(robots, dimensions):
    image = [["." for _ in range(dimensions[0])] for _ in range(dimensions[1])]
    
    for robot_pos, _ in robots:
        current = image[robot_pos[1]][robot_pos[0]]
        
        if current == ".":
            image[robot_pos[1]][robot_pos[0]] = "1"
        elif current.isdigit():
            image[robot_pos[1]][robot_pos[0]] = str(int(current) + 1) if int(current) < 9 else "+"
    
    for line in image:
        print("".join(line))


def main():
    dimensions = (101, 103)
    
    robots = parse_input()
    
    simulated = simulate(robots, 100, dimensions)
    
    print_robots(simulated, dimensions)
    
    quadrants = robots_per_quadrant(simulated, dimensions)
    print(math.prod(quadrants))
    

if __name__ == "__main__":
    main()
