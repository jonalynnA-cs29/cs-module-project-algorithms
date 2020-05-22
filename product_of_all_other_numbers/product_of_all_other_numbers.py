'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    total = 1
    new_arr = []
    # remove first number and save it
    last_num = arr.pop(0)
    for i in range(len(arr)):
        # get multiplied total of all numbers left
        total = total * arr[i]
    # append that total to new array
    new_arr.append(total)
    # return new_arr
    for i in range(0, len(arr)):
        arr.append(last_num)
        print('append: ', last_num)
        last_num = arr.pop(0)
        print('pop: ', last_num)
        total = 1
        for i in range(len(arr)):
            total = total * arr[i]
        new_arr.append(total)
    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
