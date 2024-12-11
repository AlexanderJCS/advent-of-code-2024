import part_1


def main():
    stones = part_1.parse_input()
    print(len(part_1.blink_n(stones, 75, True)))


if __name__ == "__main__":
    main()
