import itertools
import time

import part_1


def score(banana_delta_values, sequence: list[int]):
    total = 0
    
    for banana_delta in banana_delta_values:
        matches_sequence = 0
        found = False
        
        for delta, value in banana_delta:
            if delta == sequence[matches_sequence]:
                matches_sequence += 1
                
                if matches_sequence == len(sequence):
                    found = True
                    break
                
            else:
                matches_sequence = 0
        
        if found:
            total += value
    
    return total


def delta_value_pair(li):
    return [((b - a), b) for a, b in zip(li, li[1:])]


def bananas_list(seed):
    bananas = []
    
    for _ in range(2000):
        bananas.append(seed % 10)
        seed = part_1.rand(seed)
    
    return bananas


def main():
    seeds = part_1.parse_input()
    bananas = [bananas_list(seed) for seed in seeds]
    banana_delta_values = [delta_value_pair(banana_list) for banana_list in bananas]

    max_sequence = []
    max_score = -1
    
    for i, sequence in enumerate(itertools.product(range(-9, 10), repeat=4)):
        if i % 1000 == 0:
            print(time.time(), f"{i / 19 ** 4 * 100}%")
        
        seq_score = score(banana_delta_values, sequence)
        
        if seq_score > max_score:
            max_score = seq_score
            max_sequence = sequence
        
    print(max_score, max_sequence)


if __name__ == "__main__":
    main()
