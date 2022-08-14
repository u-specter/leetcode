class Solution(object):
    def reverse(self, x):
       
        reversed = (-1 if x < 0 else 1) * int(str(x)[::-1].replace("-",""))
        if reversed > pow(2,31) - 1 or reversed < -1 * pow(2, 31):
            return 0
        return reversed