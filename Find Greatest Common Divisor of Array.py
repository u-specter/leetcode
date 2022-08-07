class Solution(object):
    def findGCD(self, nums):
        s = []
        nums.sort()
        d = max(nums)
        e = min(nums)
        if d > e:
            smaller = e
        else:
            smaller = d
        for i in range(1,smaller+1):
            if((d % i == 0) and (e % i == 0)):
                hcf = i 
        return hcf
        