'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    i = 0
    move = 0
    while i < len(arr):
        if(arr[move] == 0):
            arr.pop(move)
            arr.append(0)
            i += 1
        else:
            move += 1
            i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
