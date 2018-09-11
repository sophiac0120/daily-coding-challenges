##Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
##
##The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
##
##You may assume the integer does not contain any leading zero, except the number 0 itself.
##
##Example 1:
##
##Input: [1,2,3]
##Output: [1,2,4]
##Explanation: The array represents the integer 123.
##Example 2:
##
##Input: [4,3,2,1]
##Output: [4,3,2,2]
##Explanation: The array represents the integer 4321.

def plus_one(li):
    carry = 1
    for i in range(-1, -len(li) - 1, -1):
        if carry == 1:
            li[i] += 1
            carry = 0
            if li[i] > 9:
                li[i] = 0
                carry = 1
    if carry == 1:
        return [1] + li
    return li
