class Solution:
    def addTwoNumbers(self, l1, l2 ,carry = 0):
       
        val = l1.val + l2.val + carry
        carry = val // 10
        res = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            res.next = self.addTwoNumbers(l1.next,l2.next,carry)
        return res
