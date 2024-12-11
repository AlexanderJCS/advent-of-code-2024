import part_1
import collections


def stone_map(stones: list[int]):
    return dict(collections.Counter(stones))


def blink(stone_dict: dict[int, int]) -> dict[int, int]:
    new_stones = {}
    
    for stone_value, count in stone_dict.items():
        if stone_value == 0:
            new_stones[1] = new_stones.get(1, 0) + count
        elif len((stone_str := str(stone_value))) % 2 == 0:
            left = int(stone_str[:len(stone_str) // 2])
            right = int(stone_str[len(stone_str) // 2:])
            new_stones[left] = new_stones.get(left, 0) + count
            new_stones[right] = new_stones.get(right, 0) + count
        else:
            new_stones[stone_value * 2024] = new_stones.get(stone_value * 2024, 0) + count
    
    return new_stones


def main():
    stones = stone_map(part_1.parse_input())
    
    print(stones)
    
    for _ in range(75):
        stones = blink(stones)
    
    print(stones)
    
    print(sum(stones.values()))


if __name__ == "__main__":
    main()
