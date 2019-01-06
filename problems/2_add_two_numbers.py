import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            # print(l1)
            return l2
        if not l2:
            return l1

        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])
        # print(num1, num2)
        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(int(tmp[0]))
        run_res = res
        for i in range(1, len(tmp)):
            run_res.next = ListNode(int(tmp[i]))
            run_res = run_res.next
        return res


    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers2(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumbers2(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s1 = Solution()
ans = s1.addTwoNumbers(l1, l2)
print(ans.val, ans.next.val, ans.next.next.val)

ans = s1.addTwoNumbers2(l1, l2)
print(ans.val, ans.next.val, ans.next.next.val)
