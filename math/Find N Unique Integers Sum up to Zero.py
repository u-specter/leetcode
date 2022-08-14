class Solution(object):
    def sumZero(self, n):
        l=[]
        for i in range(0,n//2):
            l.append(-(i+1))
            l.append(i+1)
        if n%2==1:
            l.append(0)
        return l