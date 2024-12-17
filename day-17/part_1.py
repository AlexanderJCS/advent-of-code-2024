

def parse_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    registers = [int(line.split()[2]) for line in data if line.startswith("Register")]
    program = list(map(int, data[-1].split()[1].split(",")))
    
    return registers, program


def eval_operand(operand: int, registers: list[int]) -> int:
    if 0 <= operand <= 3:
        return operand
    if 4 <= operand <= 6:
        return registers[operand - 4]
    if operand == 7:
        return None


def exec_instruction(instruction: int, combo_operand: int, literal_operand: int, registers: list[int], pointer: int):
    output = -1
    
    if instruction == 0:
        registers[0] //= 2 ** combo_operand
    elif instruction == 1:
        registers[1] ^= literal_operand
    elif instruction == 2:
        registers[1] = combo_operand % 8
    elif instruction == 3:
        if registers[0] != 0:
            return literal_operand, output
    elif instruction == 4:
        registers[1] ^= registers[2]
    elif instruction == 5:
        output = combo_operand % 8
    elif instruction == 6:
        registers[1] = registers[0] // (2 ** combo_operand)
    elif instruction == 7:
        registers[2] = registers[0] // (2 ** combo_operand)
    
    return pointer + 2, output


def get_program_output(registers, program):
    pointer = 0
    output = []
    while pointer < len(program):
        literal_operand = program[pointer + 1]
        
        combo_operand = eval_operand(literal_operand, registers)
        pointer, output_add = exec_instruction(program[pointer], combo_operand, literal_operand, registers, pointer)
        
        if output_add != -1:
            output.append(output_add)
    
    return output


def main():
    registers, program = parse_input()

    print(",".join(map(str, get_program_output(registers, program))))
    

if __name__ == "__main__":
    main()
    