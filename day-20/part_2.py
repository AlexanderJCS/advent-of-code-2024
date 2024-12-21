from collections import Counter

import part_1


def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def shortcut(pos, radius, orig_path):
    shortcuts = []
    original_score = orig_path[pos]
    
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            offset_pos = (pos[0] + x, pos[1] + y)
            distance = manhattan_dist(pos, offset_pos)
            
            if distance > radius:
                continue
            
            if offset_pos not in orig_path:
                continue
            
            score_at = orig_path[offset_pos]
            
            if score_at > original_score + distance:
                shortcuts.append(score_at - (original_score + distance))
            
    return shortcuts


def main():
    walls, start, end, bounds = part_1.parse_input()
    orig_path = part_1.path(start, end, walls)
    
    savings = []
    
    for coord in orig_path:
        savings.extend(shortcut(coord, 20, orig_path))
    
    savings_greater_eq_100 = [item for item in savings if item >= 100]
    print(len(savings_greater_eq_100))


if __name__ == "__main__":
    main()
