import time

import part_1


def main():
    print("warning: unless you want to be computing this for the next ~90 years, don't run this on the input data")
    
    registers, program = part_1.parse_input()
    
    output = []
    iteration = -1
    start_time = time.time()
    while output != program:
        iteration += 1
        registers[0] = iteration
        output = part_1.get_program_output(registers, program)
        
        if iteration % 100000 == 0:
            print(iteration, time.time() - start_time)
    
    print(iteration)


if __name__ == "__main__":
    main()
