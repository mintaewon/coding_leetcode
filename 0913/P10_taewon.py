'''

while 문을 계속 돌려서 끝지점이 있으면 False고
없으면 언젠간 순환되는 포인트에서 만나니 if 문으로 나와지는듯

'''


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        marker1 = head
        marker2 = head
        while marker2!=None and marker2.next!=None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            if marker2==marker1:
                return True
        return False