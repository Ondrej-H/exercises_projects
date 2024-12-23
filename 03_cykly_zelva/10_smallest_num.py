def find_smallest_num(count_of_nums=5):
    """
    Find the lowest number from user input.
    @param count_of_nums: the number of numbers
    """
    nums = []
    for i in range(count_of_nums):
        nums.append(int(input(f"{i + 1}. number: ")))

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest


print(f"The smallest number is: {find_smallest_num()}")
