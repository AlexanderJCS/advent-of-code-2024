import random
import part_1


def gen_random_test_case() -> tuple[int, list[int]]:
    solution = random.randint(0, 10)
    formula = [solution]
    for i in range(random.randint(5, 15)):
        formula.append(random.randint(1, 1000))
        
        if random.randint(0, 1):
            solution *= formula[-1]
        else:
            solution += formula[-1]
    
    return solution, formula


def test_possibility_false_negative():
    # sourcery skip: no-loop-in-tests
    for _ in range(100):
        solution, formula = gen_random_test_case()
        assert part_1.is_possible(solution, formula), f"{solution}, {formula}"


def test_input_parsing():
    # sourcery skip: no-loop-in-tests
    for _ in range(100):
        solution, formula = gen_random_test_case()
        input_str = f"{solution}: {' '.join(map(str, formula))}"
        
        data = part_1.get_input(input_str)
        
        assert (solution, formula) in data, f"{solution}, {formula}"


def test():
    test_input_parsing()
    test_possibility_false_negative()
    
    print("All tests passed")


if __name__ == "__main__":
    test()
