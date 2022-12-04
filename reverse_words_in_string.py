
def reverse_words(s: str) -> str:
    solution = ""
    for word in s.split(" ")[::-1]:
        if word.isalnum():
            solution += word + " "
    return solution.rstrip(" ")


print(reverse_words("a     good   example"))
