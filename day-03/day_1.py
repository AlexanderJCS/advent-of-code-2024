import re


def main():
    with open("input.txt") as f:
        data = f.read()
    
    mul_regex = re.compile(r"mul\(\d*,\d*\)")
    findings = mul_regex.findall(data)
    
    mul_sum = 0
    for finding in findings:
        numbers = list(map(int, finding[4:-1].split(",")))
        mul_sum += int(numbers[0]) * int(numbers[1])
    
    print(mul_sum)
    

if __name__ == "__main__":
    main()
