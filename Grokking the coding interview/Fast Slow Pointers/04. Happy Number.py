# Happy Number

# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Example 1:
# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:
# 2^2 + 3^2 = 4 + 9 = 13
# 1^2 + 3^2 = 1 + 9 = 10
# 1^2 + 0^2 = 1 + 0 = 1

def find_happy_number(number):
    fast, slow = number
    while fast != slow:
        slow = sum_square_of_digits(slow)
        fast = sum_square_of_digits(sum_square_of_digits(fast))
    
    return slow == 1

def sum_square_of_digits(number):
    sum = 0
    for digitString in str(number):
        digit = int(digitString)
        sum += digit * digit
    
    return sum

# alternative

def find_square_sum(number):
    sum = 0
    while number > 0:
        digit = num % 10
        sum += digit * digit
        num //= 10
    
    return sum

# Time complexity 
# The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

# This sequence behavior tells us two things:

# If the number N is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
# For N>1000, suppose the number has ‘M’ digits and the next number is ‘N1’. From the above Wikipedia link, we know that the sum of the squares of the digits of ‘N’ is at most 9^2M
# 81M (this will happen when all digits of ‘N’ are ‘9’).
# This means:
# N1 < 81M
# As we know M = log(N + 1)
# Therefore: N1 < 81 * log(N + 1) => N1 = O(logN)
# This concludes that the above algorithm will have a time complexity of O(logN).

# Space Complexity
# The algorithm runs in constant space O(1).