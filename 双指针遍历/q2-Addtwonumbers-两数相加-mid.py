"""
Definition for singly-linked list.
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addtwonumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headnode = ListNode(0)
        result = headnode
        carry = 0  # 进位
        p = l1
        q = l2
        while (p is not None) or (q is not None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sumval = x + y + carry
            carry = sumval / 10
            result.next = ListNode(int(sumval % 10))
            result = result.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry >= 1:
            result.next = ListNode(int(carry))
        return headnode.next

