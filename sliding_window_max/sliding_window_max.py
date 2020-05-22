'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    new_arr = []
    for i in range(len(nums) - (k - 1)):
        print('\033[96m\nstart\033[97m')
        max_num = None
        for j in range(i, k + i):
            if max_num is None:
                max_num = nums[j]
            elif nums[j] > max_num:
                max_num = nums[j]

        new_arr.append(max_num)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"\nOutput of sliding_window_max function is: \033[96m{sliding_window_max(arr, k)}\033[97m\n")
