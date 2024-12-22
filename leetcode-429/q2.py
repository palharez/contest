def operations(nums, k):
    operator = k * -1
    asw = []
    for num in nums:
        if operator > k:
            asw.append(num)
        else:
            result = num + operator
            asw.append(result)
            operator += 1
    return asw


def max_distinct_elements(nums, k):
    parsed_nums = operations(nums, k)
    count = 0
    existent = {}
    for num in parsed_nums:
        if not existent.get(num):
            existent[num] = True
            count += 1
    return count


if __name__ == "__main__":
    assert max_distinct_elements(nums=[1, 2, 2, 3, 3, 4], k=2) == 6
    assert max_distinct_elements(nums=[4, 4, 4, 4], k=1) == 3
    assert max_distinct_elements(nums=[7, 7], k=3) == 2
