import itertools
import time
from collections import defaultdict, deque

import part_1


def sell_prices(seed):
    bananas = []
    
    for _ in range(2000):
        bananas.append(seed % 10)
        seed = part_1.rand(seed)
    
    return bananas


def main():
    seeds = part_1.parse_input()
    sell_prices_list = [sell_prices(seed) for seed in seeds]
    
    sequence_price = defaultdict(int)
    
    for prices in sell_prices_list:
        seen = set()
        
        for a, b, c, d, e in zip(prices, prices[1:], prices[2:], prices[3:], prices[4:]):
            sequence = (b - a, c - b, d - c, e - d)
            
            if sequence in seen:
                continue
            
            seen.add(sequence)
            sequence_price[sequence] += e
    
    seq_price_sorted = sorted(sequence_price.items(), key=lambda n: n[1], reverse=True)
    print(seq_price_sorted[0][0])
    print(seq_price_sorted[0][1])


if __name__ == "__main__":
    main()
