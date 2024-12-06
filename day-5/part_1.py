
def is_before(page: int, test: int, rules: list[tuple[int, int]]):
    return any(rule[0] == page and rule[1] == test for rule in rules)


def is_after(page: int, test: int, rules: list[tuple[int, int]]):
    return any(rule[0] == test and rule[1] == page for rule in rules)


def is_valid_book(pages: list[int], rules: list[tuple[int, int]]):
    for i, page in enumerate(pages):
        for j, test in enumerate(pages):
            if i == j:
                continue
            
            if i < j and not is_before(page, test, rules):
                return False
            
            if i > j and not is_after(page, test, rules):
                return False
    
    return True


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    split_point = data.index("")

    before_after = []
    for line in data[:split_point]:
        before, after = line.split("|")
        before_after.append((int(before), int(after)))

    books = [list(map(int, line.split(","))) for line in data[split_point + 1:]]
    
    middle_page_sum = 0
    for book in books:
        if is_valid_book(book, before_after):
            middle_page_sum += book[len(book) // 2]
    
    print(middle_page_sum)


if __name__ == "__main__":
    main()
