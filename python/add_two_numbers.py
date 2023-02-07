def add_two_numbers(l1: list, l2: list) -> list:
    s1 = ""  # initialize string for list 1
    s2 = ""  # initialize string for list 2
    solution = []   # initialize list for solution
    l1.reverse()  # reverse list 1
    l2.reverse()  # reverse list 2
    for num in l1:  # turn both reversed lists into strings
        s1 += str(num)
    for num in l2:
        s2 += str(num)
    s3 = str(int(s1) + int(s2))  # create a string of the sum
    for num in s3[::-1]:  # iterate through string backwards
        solution.append(int(num))
    return solution


print(add_two_numbers([0, 0, 2], [2, 0, 4]))
