
def is_x_mas(data, x, y):
    if data[y][x] != "A":
        return False
    
    return (data[y - 1][x - 1] in ["M", "S"]
            and data[y + 1][x + 1] in ["M", "S"]
            and data[y - 1][x + 1] in ["M", "S"]
            and data[y + 1][x - 1] in ["M", "S"]
            and data[y - 1][x - 1] != data[y + 1][x + 1]
            and data[y - 1][x + 1] != data[y + 1][x - 1])


def x_mas(data):
    count = 0
    for y, line in list(enumerate(data))[1:-1]:
        for x, letter in list(enumerate(line))[1:-1]:
            if letter != "A":
                continue
            
            if is_x_mas(data, x, y):
                count += 1
    
    return count


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    print(x_mas(data))


if __name__ == "__main__":
    main()
