def insert_seperator(list_name: list, length_multiplier: int):
    if length_multiplier == 0:
        return
    else:
        list_name.insert(-3 * length_multiplier, '.')
        insert_seperator(list_name, length_multiplier - 1)


class Solution:
    def thousandSeparator(self, n: int) -> str:
        string_n = str(n)
        temp_list = [*string_n]   # convert int to string and unpack in temp list
        length = len(temp_list)
        if length >= 4:     # only insert full stop if number has thousands place
            list_multiplier = (length - 1) // 3
            insert_seperator(temp_list, list_multiplier)
            separated_n = ''.join((str(char) for char in temp_list))    # list back to string
            return separated_n
        else:
            return string_n