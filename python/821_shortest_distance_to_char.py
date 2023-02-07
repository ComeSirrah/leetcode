def shortest_to_char(s: str, c: str) -> list[int]:
    indexed_chars = {i: char for i, char in enumerate(s)}
    # indexed_chars = dict()  # instantiate the dict
    # for i, char in enumerate(s):    # add a key-value pair to dict for index and char in s
    #     indexed_chars[i] = char
    # isolate index of each instance of c
    indices_of_c = [int(key) for key, value in indexed_chars.items() if value == c]
    # get a list of comparison between each char in s with each comparison being the absolute value of the number
    comparisons = [[abs(c_index - s_index) for c_index in indices_of_c] for s_index in range(len(s))]
    # return only the smallest absolute value of each list, because this is the shortest distance to each letter.
    solution = [sorted(comparison)[0] for comparison in comparisons]
    return solution


if __name__ == '__main__':
    s = "loveleetcode"
    c = "e"

    print(shortest_to_char(s, c))
