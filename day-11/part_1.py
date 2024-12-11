import time


def parse_input():
    with open("input.txt") as f:
        data = f.read()
    
    return list(map(int, data.split(" ")))


def blink(stones: list[int]) -> list[int]:
    for i, stone in reversed(list(enumerate(stones))):
        if stone == 0:
            stones[i] = 1
        elif len((stone_str := str(stone))) % 2 == 0:
            left = stone_str[:len(stone_str) // 2]
            right = stone_str[len(stone_str) // 2:]
            stones[i] = int(right)
            stones.insert(i, int(left))
        else:
            stones[i] *= 2024
        
    return stones


def blink_n(stones: list[int], n: int, verbose=False) -> list[int]:
    stones = list(stones)
    
    for i in range(n):
        if verbose:
            print(len(stones))
        
        blink(stones)
    
    return stones


def main():
    stones = parse_input()
    print(len(blink_n(stones, 25)))


if __name__ == "__main__":
    main()
