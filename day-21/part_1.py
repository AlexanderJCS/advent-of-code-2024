
NUMPAD = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
    " ": (0, 3)
}

DPAD = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
    " ": (0, 0)
}


def parse_input():
    with open("input.txt") as f:
        # list comprehension to avoid newline at the end of a file (or any other blank line)
        return [line for line in f.read().splitlines() if not line.isspace()]


def shortest_path(p1, p2, avoid_point):
    displacement = (p2[0] - p1[0], p2[1] - p1[1])
    
    y_first = avoid_point[1] == p1[1]
    
    if not y_first:
        path = ("<" if displacement[0] < 0 else ">") * abs(displacement[0])
        path += ("^" if displacement[1] < 0 else "v") * abs(displacement[1])
    else:
        path = ("^" if displacement[1] < 0 else "v") * abs(displacement[1])
        path += ("<" if displacement[0] < 0 else ">") * abs(displacement[0])
    
    return path


def keypad(inputs: str, mapping: dict):
    pos = mapping["A"]
    avoid = mapping[" "]
    instructions = ""

    for ch in inputs:
        new_pos = mapping[ch]
        instructions += f"{shortest_path(pos, new_pos, avoid)}A"
        pos = new_pos

    return instructions


def decode(encoded: str):
    instructions = ""
    
    pos = (DPAD["A"])
    
    offsets = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    
    for i in range(3):
        pos = NUMPAD["A"] if i == 2 else pos
        avoid = NUMPAD[" "] if i == 2 else DPAD[" "]
        
        for instruction in encoded:
            if instruction in offsets:
                offset = offsets[instruction]
                pos = (pos[0] + offset[0], pos[1] + offset[1])
                
                if pos == avoid:
                    raise ValueError(f"At illegal pos: {pos}")
                
            else:
                dpad_or_npad = DPAD if i < 2 else NUMPAD
                
                inverse = {v: k for k, v in dpad_or_npad.items()}
                instructions += inverse[pos]
        
        encoded = instructions
        instructions = ""
    
    return encoded


def main():
    codes = parse_input()
    complexities = 0
    
    for code in codes:
        instructions = keypad(code, NUMPAD)
        
        for _ in range(2):
            instructions = keypad(instructions, DPAD)
        
        print(f"{len(instructions)} * {int(code[:-1])} | decoded: {decode(instructions)}")
        complexities += len(instructions) * int(code[:-1])
    
    print(complexities)


if __name__ == "__main__":
    main()
