import re


def main():
    with open("input.txt") as f:
        data = f.read()
    
    mul_regex = re.compile(r"mul\(\d*,\d*\)")
    do_regex = re.compile(r"do\(\)")
    dont_regex = re.compile(r"don't\(\)")
    
    mul_sum = 0
    do = True
    index = 0
    
    while index < len(data):
        if do:
            mul_match = mul_regex.search(data, index)
            dont_match = dont_regex.search(data, index)
            
            if mul_match is None:
                break
            
            if dont_match is not None and dont_match.start() < mul_match.start():
                do = False
                index = dont_match.end()
                continue
            
            mul_string = mul_match.string[mul_match.start():mul_match.end()]
            numbers = list(map(int, mul_string[4:-1].split(",")))
            mul_sum += int(numbers[0]) * int(numbers[1])
            index = mul_match.end()
            
        if not do:
            do_match = do_regex.search(data, index)
            
            if do_match is None:
                break
            
            do = True
            index = do_match.end()
    
    print(mul_sum)


if __name__ == "__main__":
    main()
