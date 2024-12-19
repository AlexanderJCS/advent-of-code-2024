from functools import cache


def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    available = data[0].split(", ")
    desired = [line for line in data[1:] if line]
    
    return available, desired


@cache
def is_possible(pattern: str, available: tuple[str], current: str = ""):
    if not pattern.startswith(current):
        return False
    
    if current == pattern:
        return True
    
    return any(
        is_possible(pattern, available, current + add)
        for add in available
    )


def main():
    available, desired = parse_input()
    available = tuple(available)
    
    sum_possible = 0
    for towel in desired:
        possible = is_possible(towel, available)
        sum_possible += possible
        print(towel, possible)
    
    print(sum_possible)


if __name__ == "__main__":
    main()
    