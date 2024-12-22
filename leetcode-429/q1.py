def is_distinct(nums):
    existent = {}
    for num in nums:
        if existent.get(num):
            return False
        else:
            existent[num] = True
    return True


def minimum_operations(nums):
    operations = 0
    while not is_distinct(nums):
        operations += 1
        nums = nums[3:]
    return operations


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
    assert minimum_operations(nums=nums) == 2
    nums = nums = [4, 5, 6, 4, 4]
    assert minimum_operations(nums=nums) == 2
    nums = [6, 7, 8, 9]
    assert minimum_operations(nums=nums) == 0
