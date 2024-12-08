import part_1


def is_possible(solution: int, formula: list[int], current: int | None = None):
    if not formula:
        return solution == current
    
    return (is_possible(solution, formula[1:], current * formula[0] if current is not None else formula[0])
            or is_possible(solution, formula[1:], current + formula[0] if current is not None else formula[0])
            or is_possible(solution, formula[1:], int(f"{current}{formula[0]}") if current is not None else formula[0]))


def main():
    data = part_1.get_input()

    count = sum(
        solution if is_possible(solution, formula) else 0
        for solution, formula in data
    )
    
    print(count)


if __name__ == "__main__":
    main()
