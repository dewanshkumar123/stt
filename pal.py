def is_palindrome(word):
   
    left, right = 0, len(cleaned_word) - 1
    while left < right:
        if cleaned_word[left] != cleaned_word[right]:
            return False
        left += 1
        right -= 1
    return True

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def next_permutation(nums):
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


word = input()
if is_palindrome(word):
  print(f"{word} is a palindrome.")
else:
  print(f"{word} is not a palindrome.")

number = int(input())
try:
  print(f"Factorial of {number} is {factorial(number)}.")
except ValueError as e:
  print(e)

nums = list(map(int, input("Enter a list of numbers for next permutation: ").split()))
if next_permutation(nums):
  print(f"The next permutation is: {nums}")
else:
  print("No next permutation available.")

