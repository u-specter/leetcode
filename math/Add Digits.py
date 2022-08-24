class Solution(object):
    def addDigits(self, num):
        ns = str(num)
        while len(ns)!=1:
            sum = 0
            for i in ns:
                sum+=int(i)
            ns = str(sum)
        return int(ns)
        