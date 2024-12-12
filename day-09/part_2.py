import part_1


def move_back(input_data, number) -> list[int]:
    input_copy = list(input_data)

    back = []
    start_idx = -1
    end_idx = -1
    for i, val in enumerate(input_copy):
        if val == number:
            back.append(number)
            
            end_idx = i
            if start_idx == -1:
                start_idx = i
        
        elif back:
            break
    
    # now search for a free space
    free_spaces = 0
    free_space_start_idx = -1
    for i, val in enumerate(input_data):
        if val is None:
            free_spaces += 1
            
            if free_spaces == 1:
                free_space_start_idx = i
            
            if free_spaces >= len(back):
                break
        else:
            free_spaces = 0
    
    if free_space_start_idx == -1 or free_spaces < len(back) or start_idx < free_space_start_idx:
        return input_data
    
    for i in range(len(back)):
        input_copy[free_space_start_idx + i] = back[0]

    for i in range(start_idx, end_idx + 1):
        input_copy[i] = None
    
    return input_copy


def print_list(li):
    for val in li:
        print(val if val is not None else ".", end="")
    
    print()


def amphipodulate_parktitions(input_data) -> list[int | None]:
    current = list(input_data)
    
    for i in range(max(item for item in input_data if item is not None), -1, -1):
        print(i)
        # print_list(current)
        current = move_back(current, i)
    
    # print_list(current)
    return current


def main():
    with open("input.txt") as f:
        data = f.read()
    
    data_list = part_1.construct_list(data)
    amphi = amphipodulate_parktitions(data_list)
    print(part_1.checksum(amphi))


if __name__ == "__main__":
    main()
