from functools import cache


def parse_input():
    with open("input.txt") as f:
        return list(map(int, (line for line in f.read().splitlines() if not line.isspace())))


@cache
def rand(n):
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    n %= 16777216
    
    return n


def secret_iterate(n, m):
    for _ in range(m):
        n = rand(n)
    
    return n

    
def main():
    starting = parse_input()
    
    print(sum(secret_iterate(num, 2000) for num in starting))


if __name__ == "__main__":
    main()
