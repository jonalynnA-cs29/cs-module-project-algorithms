'''
Input: an integer
Returns: an integer
'''
import sys
import random


def eating_cookies(n, cache={}):
    if n < 0:
        return 0
    if n <= 1:
        return 1

    if n not in cache:
        cache[n] = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are \033[96m{eating_cookies(num_cookies)} ways\033[97m for Cookie Monster to eat \033[96m{num_cookies} cookies\033[97m")
