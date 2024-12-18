import part_1


def main():
    corrupted = part_1.parse_input()
    
    inf = float("inf")
    
    for i in range(len(corrupted) + 1):
        if part_1.search(set(corrupted[:i]), (70, 70)) == inf:
            break
    
    else:
        print("No solution found")
        return

    print(",".join(list(map(str, corrupted[i - 1]))))


if __name__ == "__main__":
    main()
