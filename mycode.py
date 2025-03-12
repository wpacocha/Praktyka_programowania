import re
def Add(numbers):
    if not numbers:
        return 0
    if numbers.endswith('\n') or numbers.endswith(','):
        raise ValueError
    numbers_list = re.split(r'[, \n]',numbers)
    return sum(map(int, numbers_list))