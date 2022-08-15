class Solution(object):
    def maximum69Number (self, num):
        
        s1=""
        k=0
        for i in str(num):
            if i=='6' and k==0:
                s1=s1+'9'
                k=1
            else:
                s1=s1+i
        return int(s1)
        