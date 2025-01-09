"""
This module contains utility functions for checking palindromes, calculating factorials,
and generating the next permutation of a list.
"""

def is_palindrome(word):
    """
    Check if a given word is a palindrome.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The integer to calculate the factorial of.

    Returns:
        int: The factorial of the given integer.

    Raises:
        ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def next_permutation(nums):
    """
    Generate the next lexicographical permutation of a list of numbers.

    Args:
        nums (list of int): The list of integers to permute.

    Returns:
        bool: True if the next permutation was found, False if the input is the last permutation.
    """
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return True

if __name__ == "__main__":
    WORD = "abccba"
    if is_palindrome(WORD):
        print(f"{WORD} is a palindrome.")
    else:
        print(f"{WORD} is not a palindrome.")

    NUM = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {NUM} is {factorial(NUM)}.")

    NUMS = list(map(int, input("Enter a list of numbers for next permutation: ").split()))
    if next_permutation(NUMS):
        print(f"The next permutation is: {NUMS}")
    else:
        print("No next permutation available.")
