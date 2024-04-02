from typing import *

class Solution:
    def __init__(self):
        self.keystore = {}

    def lengthOfLIS(self, nums: List[int]) -> int:

        self.keystore[nums[0]] = 1
        for i in range(1, len(nums)):
            if nums[i] not in self.keystore.keys():
                self.keystore[nums[i]] = 1
            
            for key in list(self.keystore.keys()):
                val = self.keystore[key]

                if key < nums[i]:
                    if (nums[i] in self.keystore) and (val + 1 > self.keystore[nums[i]]):
                        self.keystore[nums[i]] = (val + 1) 
                    elif (nums[i] not in self.keystore):
                        self.keystore[nums[i]] = (val + 1)

        return max(self.keystore.values())

# print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))