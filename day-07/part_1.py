

def get_input(input_str=None) -> list[tuple[int, list[int]]]:
    if input_str is None:
        with open("input.txt") as f:
            data = f.read().splitlines()
    else:
        data = input_str.splitlines()  # input_str used for testing
    
    equations = []
    for line in data:
        solution = int(line.split(": ")[0])
        formula = list(map(int, line.split(": ")[1].split(" ")))
        equations.append((solution, formula))
    
    return equations


def is_possible(solution: int, formula: list[int], current: int | None = None):
    if not formula:
        return solution == current
    
    return (is_possible(solution, formula[1:], current * formula[0] if current is not None else formula[0])
            or is_possible(solution, formula[1:], current + formula[0] if current is not None else formula[0]))


def main():
    data = get_input()

    count = sum(
        solution if is_possible(solution, formula) else 0
        for solution, formula in data
    )
    
    print(count)


if __name__ == "__main__":
    main()
