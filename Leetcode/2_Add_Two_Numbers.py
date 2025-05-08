class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2:
            summ = 0
            
            if l1:
                summ += l1.val
                l1 = l1.next
                
            if l2:
                summ += l2.val
                l2 = l2.next
                
            if carry:
                summ += carry
                
            carry = summ // 10
            summ = summ % 10
            
            currNode = ListNode(summ)
            curr.next = currNode
            curr = curr.next
            
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
            curr = curr.next
            
        return dummy.next
