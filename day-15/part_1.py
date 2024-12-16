
INSTRUCTIONS_MAP = {
    "<": (-1, 0),
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1)
}


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    robot_map = []
    instructions = ""
    
    for line in data:
        if not line:
            continue
        
        if "#" in line:
            robot_map.append(line)
        
        else:
            instructions += line

    return robot_map, instructions


def convert_to_coords(robot_map):
    robot_pos = None
    crates = set()
    walls = set()
    
    for y, row in enumerate(robot_map):
        for x, ch in enumerate(row):
            if ch == "@":
                robot_pos = (x, y)
            elif ch == "#":
                walls.add((x, y))
            elif ch == "O":
                crates.add((x, y))
    
    return robot_pos, crates, walls


def run_instruction(
        robot_pos: tuple[int, int],
        crates: set[tuple[int, int]],
        walls: set[tuple[int, int]],
        instruction: tuple[int, int]
) -> tuple:
    """
    Runs the instruction.
    :return: new robot pos, crates
    """
    
    new_robot_pos = (robot_pos[0] + instruction[0], robot_pos[1] + instruction[1])
    
    if new_robot_pos in walls:
        return robot_pos, crates
    
    if new_robot_pos in crates:
        # move the crate in the direction until you hit a wall (impossible, revert to original position) or until there
        # is a free space
        offset = 1
        valid_space = False
        while True:
            new_crate_pos = (new_robot_pos[0] + instruction[0] * offset, new_robot_pos[1] + instruction[1] * offset)
            
            if new_crate_pos in crates:
                offset += 1
                continue
            
            if new_crate_pos in walls:
                break
            
            valid_space = True
            break
        
        if not valid_space:
            return robot_pos, crates
        
        crates = set(crates)
        crates.remove(new_robot_pos)
        crates.add(new_crate_pos)
    
    return new_robot_pos, crates


def score(crates):
    return sum(
        crate[1] * 100 + crate[0]
        for crate in crates
    )


def print_board(robot_pos, crates, walls, size):
    for y in range(size[1]):
        for x in range(size[0]):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in crates:
                print("O", end="")
            elif (x, y) == robot_pos:
                print("@", end="")
            else:
                print(".", end="")
        
        print()


def main():
    robot_map, instructions = parse_input()
    robot_pos, crates, walls = convert_to_coords(robot_map)

    for instruction in instructions:
        robot_pos, crates = run_instruction(robot_pos, crates, walls, INSTRUCTIONS_MAP[instruction])
        # print(f"\n{instruction}")
        # print_board(robot_pos, crates, walls, (len(robot_map[0]), len(robot_map)))
    
    print(score(crates))
    

if __name__ == "__main__":
    main()
