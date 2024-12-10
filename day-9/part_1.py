

def construct_list(input_data):
    output = []

    for i, ch in enumerate(input_data):
        append = None if i % 2 == 1 else i // 2
        output.extend(append for _ in range(int(ch)))
    
    return output


def amphipodulate(input_list):
    input_list_stack = list(input_list)
    output = []

    for i, val in enumerate(input_list):
        if i >= len(input_list_stack):
            break
        
        if val is not None:
            output.append(val)
            continue

        popped = input_list_stack.pop()
        while popped is None:
            popped = input_list_stack.pop()

        output.append(popped)
    
    return output


def checksum(amphi_list) -> int:
    return sum(i * val if val is not None else 0 for i, val in enumerate(amphi_list))


def main():
    with open("input.txt") as f:
        data = f.read()
    
    data_list = construct_list(data)
    amphipodulated = amphipodulate(data_list)
    
    print(checksum(amphipodulated))


if __name__ == "__main__":
    main()
