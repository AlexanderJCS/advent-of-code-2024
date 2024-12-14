

def solve(a: tuple, b: tuple, prize: tuple) -> tuple:
    # solving the system of equations:
    #  a_x * A + b_x * B = prize_x
    #  a_y * A + b_y * B = prize_y
    
    # wolfram gave me the solutions A and B to the system
    
    a_presses = (prize[0] * b[1] - b[0] * prize[1]) / (a[0] * b[1] - b[0] * a[1])
    b_presses = (prize[0] * a[1] - a[0] * prize[1]) / (b[0] * a[1] - a[0] * b[1])
    
    return a_presses, b_presses


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    # format: [[a, b, s], [a, b, s], ...]
    output = [[]]
    
    for line in data:
        split = line.split(" ")
        
        if line.startswith("Button"):
            output[-1].append([
                int(split[2][2:-1]),
                int(split[3][2:])
            ])
        
        elif line.startswith("Prize:"):
            output[-1].append([
                int(split[1][2:-1]),
                int(split[2][2:])
            ])
        
        else:
            output.append([])
    
    return output


def total_cost(data, max_presses=100):
    cost_sum = 0
    for a, b, prize in data:
        a_presses, b_presses = solve(a, b, prize)
        
        if (
                a_presses > max_presses
                or b_presses > max_presses
                or abs(a_presses - int(a_presses)) > 0.000001
                or abs(b_presses - int(b_presses)) > 0.000001
        ):
            continue
        
        cost_sum += a_presses * 3 + b_presses

    return int(cost_sum)


def main():
    data = parse_input()
    print(total_cost(data))


if __name__ == "__main__":
    main()
