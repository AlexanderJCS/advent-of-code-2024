import part_1


def main():
    data = part_1.parse_input()
    for item in data:
        item[2][0] += 10000000000000
        item[2][1] += 10000000000000
        
    print(data)
    
    print(part_1.total_cost(data, max_presses=float("inf")))


if __name__ == "__main__":
    main()
