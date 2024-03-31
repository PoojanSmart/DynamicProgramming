'''
https://leetcode.com/problems/maximum-product-subarray
'''
from typing import *
from sys import maxsize

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = -maxsize
        for i in range(len(nums)):
            product = 1
            cnt_neg = 0
            has_zero = False
            for j in range(i, len(nums)):
                if nums[j] < 0:
                    cnt_neg +=1
                if nums[j] == 0:
                    has_zero = True
                product *= nums[j]
                if (i == 0) and (j == (len(nums) -1)):
                    if cnt_neg == 0 and has_zero == False:
                        return product
                if product > max:
                    max = product
        return max

# print(Solution().maxProduct([2,3,-2,4]))
# print(Solution().maxProduct([-2,0,-1]))

print(Solution().maxProduct([7,-2,-4]))