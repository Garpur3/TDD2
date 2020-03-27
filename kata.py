import re

def Add(numbers):
    if len(numbers) > 0:
        list_of_numbers = re.split(",|\n", numbers)
        total = 0
        negatives = ""
        for number in list_of_numbers:
            if int(number) <= 1000:
                if int(number) < 0:
                    negatives += number + ","
                total += int(number)
        if len(negatives) > 0:
            raise ValueError(f"Negatives not allowed: {negatives[:-1]}")
        return total
    return 0