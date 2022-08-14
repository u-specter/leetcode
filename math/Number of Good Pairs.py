class Solution(object):
    def numIdenticalPairs(self, nums):
        x = 0
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                print(nums[j]==nums[k])
                if nums[j]==nums[k]:
                    x+=1
        return x
        