def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    left_list = []
    right_list = []
    
    for line in data:
        left_list.append(int(line.split("   ")[0]))
        right_list.append(int(line.split("   ")[1]))
    
    similarity_score = 0
    
    for left in left_list:
        similarity_score += left * right_list.count(left)
    
    print(similarity_score)


if __name__ == "__main__":
    main()
