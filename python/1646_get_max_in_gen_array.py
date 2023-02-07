def get_max_generated(n: int):
    """
    :param n:
    :return: return the maximum of the array generated with n
    """
    if n == 0:
        return 0

    nums = [0, 1]

    for i in range(2, n + 1):
        if i % 2 == 0:
            nums.append(nums[i // 2])
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1])
    print(nums)
    return max(nums)


get_max_generated(7)
