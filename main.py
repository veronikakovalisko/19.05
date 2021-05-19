'''Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions.
 If all nums inside the list are positive, execute the first function on that list and return the result of it.
 Otherwise, return the result of the second one'''

def choose_func(nums, func1, func2):
    nums1 = list(filter(lambda it: it > 0, nums))
    if len(nums) == len(nums1):
        return func1(nums)
    else:
        return func2(nums)
def square_nums(nums):
    return [i**2 for i in nums]
def remove_negatives(nums):
    return [i for i in nums if i >= 0]
if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))
"""Task 2
Write a Python program to access a function inside a function 
(Tips: use function, which returns another function)"""
def func(words):
    return [i+' + ' for i in words]
def access_function(a):
    if len(a) > 0:
        return func(a)
if __name__ == '__main__':
    a = ["hello", "word"]
    print(access_function(a))
'''Task 1
Write a Python program to detect the number of local variables declared in a function.'''


