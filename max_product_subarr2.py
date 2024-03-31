
'''
https://leetcode.com/problems/maximum-product-subarray
Maximum product subarray solved using kadane's modified algorithm for maximum sum subarray
'''
from typing import *
from sys import maxsize

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = -maxsize
        max_tillnow = nums[0]
        min_tillnow = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], nums[i]*max_tillnow, nums[i]*min_tillnow)
            min_tillnow = min(nums[i], nums[i]*max_tillnow, nums[i]*min_tillnow)
            max_tillnow = new_max

            if max_< max_tillnow:
                max_ = max_tillnow

        return max_
# print(Solution().maxProduct([2,3,-2,4]))
# print(Solution().maxProduct([-2,0,-1]))

print(Solution().maxProduct([7,-2,-4]))