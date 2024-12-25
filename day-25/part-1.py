

def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    lock_keys = [[]]
    for line in lines:
        if not line:
            lock_keys.append([])
            continue
        
        lock_keys[-1].append(line)
    
    # blank line at eof
    if not lock_keys[-1]:
        lock_keys.pop()
    
    locks = []
    keys = []
    
    for lock_key in lock_keys:
        is_lock = lock_key[0][0] == "#"
        
        if is_lock:
            locks.append([])
        else:
            keys.append([])
            
        for x in range(len(lock_key[0])):
            y = 0  # init y to 0 to prevent "referenced before assignment" warning in PyCharm
            y_range = range(len(lock_key)) if is_lock else range(len(lock_key) - 1, -1, -1)
            
            for y in y_range:
                if lock_key[y][x] == ".":
                    break
            
            if is_lock:
                locks[-1].append(y - 1)
            else:
                keys[-1].append(6 - y - 1)
    
    return locks, keys


def main():
    locks, keys = parse_input()
    
    pairs = 0
    for lock in locks:
        for key in keys:
            for lock_height, key_height in zip(lock, key):
                if lock_height + key_height >= 6:
                    break
            
            else:  # no break
                pairs += 1
    
    print(pairs)
    

if __name__ == "__main__":
    main()
