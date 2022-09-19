class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        
        while head:
            temp = head.next
            head.next = answer
            answer = head
            head=temp
        return answer