# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get10num(ListNode1):
            a = 0
            fw = 1
            while ListNode1.next:
                a += fw * ListNode1.val
                fw = 10 * fw

        def getListnode(num):
            while num // 10 > 0:
                ListNode1 = ListNode(num % 10)
                num = num // 10
                ListNode1 = ListNode1.next

        num1 = get10num(l1)
        num2 = get10num(l2)

        result = num1 + num2
        return getListnode(result)


if __name__ == '__main__':
    s = Solution
    ListNode1 = ListNode(342)
    ListNode2 = ListNode(465)
    s.addTwoNumbers()