import part_1


def main():
    walls, start, end, bounds = part_1.parse_input()
    orig_path = part_1.path(start, end, walls)
    
    over_eq_100 = 0
    
    for coord in orig_path:
        shortcuts = part_1.shortcut(coord, 20, orig_path[coord], orig_path, bounds)
        
        for saving in shortcuts:
            if saving >= 100:
                over_eq_100 += 1
    
    print(over_eq_100)


if __name__ == "__main__":
    main()
