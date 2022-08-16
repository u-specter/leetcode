class Solution(object):
    def squareIsWhite(self, coordinates):
        alpha = 'abcdefgh'
        a = alpha.index(coordinates[0])+1
        b = int(coordinates[1])
        return (a+b)%2!=0
        