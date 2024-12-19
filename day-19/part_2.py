from functools import cache
import part_1


@cache
def num_combinations(pattern: str, available: tuple[str], current: str = ""):
    if not pattern.startswith(current):
        return False
    
    if current == pattern:
        return True
    
    return sum(
        num_combinations(pattern, available, current + add)
        for add in available
    )


def main():
    available, desired = part_1.parse_input()
    available = tuple(available)
    
    sum_combinations = 0
    for towel in desired:
        combinations = num_combinations(towel, available)
        sum_combinations += combinations
        print(towel, combinations)
    
    print(sum_combinations)


if __name__ == "__main__":
    main()
