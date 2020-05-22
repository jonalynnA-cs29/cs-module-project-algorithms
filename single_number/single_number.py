'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    for index in range(0, len(arr) - 1):

        duplicates = 0

        for item in arr:
            if item == arr[index]:
                duplicates += 1

        if duplicates <= 1:
            print(arr[index])
            return arr[index]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
