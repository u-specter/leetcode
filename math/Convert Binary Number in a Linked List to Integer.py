class Solution(object):
    def getDecimalValue(self, head):
        
        num = ''
        node = head
        
        while node:
            num += str(node.val)
            node = node.next
        
        return int(num, 2)