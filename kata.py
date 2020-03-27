import re

def Add(numbers):
    if len(numbers) > 0:
        list_of_numbers = re.split(",|\n", numbers)
        total = 0
        for number in list_of_numbers:
            total += int(number)
        return total
    return 0