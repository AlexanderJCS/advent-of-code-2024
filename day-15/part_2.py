import part_1


class Crate:
    def __init__(self, left: tuple, right: tuple):
        self.left = left
        self.right = right
        
        self.moved = False
    
    def what_if(self, offset: tuple):
        left = (self.left[0] + offset[0], self.left[1] + offset[1])
        right = (self.right[0] + offset[0], self.right[1] + offset[1])
        
        return left, right
    
    def move(self, offset: tuple):
        self.left, self.right = self.what_if(offset)
    
    def collides_crate(self, other):
        return self.left in (other.left, other.right) or self.right in (other.left, other.right)

    def collides_point(self, point: tuple):
        return point in (self.left, self.right)
    
    def score(self):
        return self.left[1] * 100 + self.left[0]
    
    def __str__(self):
        return f"Crate({self.left}, {self.right})"


class Crates:
    def __init__(self, crates_set: set):
        self.crates = [
            Crate((crate[0] * 2, crate[1]), (crate[0] * 2 + 1, crate[1]))
            for crate in crates_set
        ]
    
    def move_crate(self, move_crate: Crate, walls: set, robot_movement: tuple):
        move_crate.move(robot_movement)

        for crate in self.crates:
            if move_crate is crate:
                continue

            if crate.collides_crate(move_crate):
                self.move_crate(crate, walls, robot_movement)
    
    def can_move_crate(self, move_crate: Crate, walls: set, robot_movement: tuple):
        left, right = move_crate.what_if(robot_movement)
        
        if left in walls or right in walls:
            return False
        
        for crate in self.crates:
            if move_crate is crate:
                continue
            
            if (
                (crate.collides_point(left) or crate.collides_point(right))  # collision
                and not self.can_move_crate(crate, walls, robot_movement)  # collides, and crate can't move
            ):
                return False
        
        return True
    
    def resolve_conflicts(self, robot_pos: tuple, walls: set, robot_movement: tuple):
        move_crate = next(
            (crate for crate in self.crates if crate.collides_point(robot_pos)),
            None,
        )
        
        if move_crate is None:
            return True

        if not self.can_move_crate(move_crate, walls, robot_movement):
            return False

        self.move_crate(move_crate, walls, robot_movement)
        return True
    
    def score(self):
        return sum(crate.score() for crate in self.crates)
    
    def char_at(self, point):
        for crate in self.crates:
            if point == crate.left:
                return "["
            elif point == crate.right:
                return "]"
        
        return None
    

def run_instruction(robot_pos: tuple, crates: Crates, walls: set, instruction: tuple):
    new_robot_pos = (robot_pos[0] + instruction[0], robot_pos[1] + instruction[1])
    
    if new_robot_pos in walls:
        return robot_pos
    
    if crates.resolve_conflicts(new_robot_pos, walls, instruction):
        return new_robot_pos
    
    return robot_pos


def convert_walls(old_walls: set):
    new_walls = set()
    
    for wall in old_walls:
        new_walls.add((wall[0] * 2, wall[1]))
        new_walls.add((wall[0] * 2 + 1, wall[1]))
    
    return new_walls


def print_map(robot, walls, crates, dimensions):
    for y in range(dimensions[1]):
        for x in range(dimensions[0]):
            if (x, y) == robot:
                print("@", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif crate_char := crates.char_at((x, y)):
                print(crate_char, end="")
            else:
                print(".", end="")
        
        print()


def main():
    robot_map, instructions = part_1.parse_input()
    robot_pos, crates, walls = part_1.convert_to_coords(robot_map)
    walls = convert_walls(walls)
    crates = Crates(crates)
    robot_pos = (robot_pos[0] * 2, robot_pos[1])
    
    # print_map(robot_pos, walls, crates, (len(robot_map[0]) * 2, len(robot_map)))

    for i, instruction in enumerate(instructions):
        robot_pos = run_instruction(robot_pos, crates, walls, part_1.INSTRUCTIONS_MAP[instruction])
        
        # print(f"\n{i}, {instruction}")
        # print_map(robot_pos, walls, crates, (len(robot_map[0]) * 2, len(robot_map)))

    print(crates.score())


if __name__ == "__main__":
    main()
