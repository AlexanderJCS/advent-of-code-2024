

def search_word(data, word, x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    count = 0
    for direction in directions:
        for i in range(len(word)):
            new_x = x + i * direction[0]
            new_y = y + i * direction[1]
            
            if new_x < 0 or new_x >= len(data[0]) or new_y < 0 or new_y >= len(data):
                break
            
            if data[new_y][new_x] != word[i]:
                break
        
        else:  # nobreak
            count += 1
    
    return count


def word_search_occurences(data, word):
    count = 0
    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            if letter != word[0]:
                continue
            
            if increment := search_word(data, word, x, y):
                count += increment
    
    return count


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    print(word_search_occurences(data, "XMAS"))


if __name__ == "__main__":
    main()
