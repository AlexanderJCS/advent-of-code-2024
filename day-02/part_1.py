

def is_safe(report: list[int]) -> bool:
    direction = report[0] - report[1]
    if direction == 0:
        return False
    direction = -1 if direction < 0 else 1
    
    for current_report, next_report in zip(report, report[1:]):
        delta = current_report - next_report  # slightly diff definition of delta but that's fine
        
        if delta * direction <= 0:  # also covers case of delta == 0
            return False
        
        if abs(delta) > 3:
            return False
        
    return True


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        
    safe_reports = 0
    for line in data:
        report = list(map(int, line.split(" ")))
        if is_safe(report):
            safe_reports += 1
    
    print(safe_reports)


if __name__ == "__main__":
    main()
    