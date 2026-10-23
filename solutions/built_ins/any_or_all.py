def any_or_all(nums):
    return all(x > 0 for x in nums) and any(str(x) == str(x)[::-1] for x in nums)
