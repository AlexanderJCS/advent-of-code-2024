from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    env = {}
    definitions = {}

    for line in lines:
        if ":" in line:
            split = line.split(": ")
            env[split[0]] = bool(int(split[1]))

        if "->" in line:
            split = line.split()
            definitions[split[4]] = split[:3]
    
    return env, definitions
    

def operation(a, b, operator):
    if operator == "OR":
        return a or b
    if operator == "AND":
        return a and b
    if operator == "XOR":
        return a ^ b
    
    raise ValueError(f"Operator {operator} not found")


def main():
    env, definitions = parse_input()
    
    while True:
        did_something = False
        for var, definition in definitions.items():
            if var in env:
                continue
            
            if definition[0] not in env or definition[2] not in env:
                continue
            
            did_something = True
            env[var] = operation(env[definition[0]], env[definition[2]], definition[1])
        
        if not did_something:
            break
        
    result = 0
    for var, val in env.items():
        if var[0] != "z" or not val:
            continue
        
        shift = int(var[1:])
        result |= 1 << shift
    
    print(result)


if __name__ == "__main__":
    main()
