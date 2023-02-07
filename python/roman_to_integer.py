def roman_to_int(s: str) -> int:
    numeral_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    numbers = []

    for index, numeral in enumerate(s[:-1]):
        if numeral == 'I' and (s[index + 1] == 'V' or s[index + 1] == 'X'):
            numbers.append(-numeral_values[numeral])
        elif numeral == 'X' and (s[index + 1] == 'L' or s[index + 1] == 'C'):
            numbers.append(-numeral_values[numeral])
        elif numeral == 'C' and (s[index + 1] == 'D' or s[index + 1] == 'M'):
            numbers.append(-numeral_values[numeral])
        else:
            numbers.append(numeral_values[numeral])
    numbers.append(numeral_values[s[-1]])

    return sum(numbers)


print(roman_to_int('XCII'))
