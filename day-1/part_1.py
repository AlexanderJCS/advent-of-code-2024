
def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    left_list = []
    right_list = []
    
    for line in data:
        left_list.append(int(line.split("   ")[0]))
        right_list.append(int(line.split("   ")[1]))
    
    left_list.sort()
    right_list.sort()
    
    distances = []
    for left, right in zip(left_list, right_list):
        distances.append(abs(right - left))
    
    print(sum(distances))


if __name__ == "__main__":
    main()
