"""
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_len = self.get_len_linked_list(l1)
        l2_len = self.get_len_linked_list(l2)
        if l1_len > l2_len:
            l2 = self.append_zero_linked_list(l2, l1_len - l2_len)
        elif l1_len < l2_len:
            l1 = self.append_zero_linked_list(l1, l2_len - l1_len)
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        output = None
        while l1:
            val = l1.val + l2.val + carry
            output = self.add_head(output, val % 10)
            carry = val // 10
            l1 = l1.next
            l2 = l2.next
        if carry > 0:
            output = self.add_head(output, carry)
        return output

    def add_head(self, output, val):
        if output is None:
            return ListNode(val)
        return ListNode(val, output)

    def append_zero_linked_list(self, li: ListNode, count):
        for i in range(count):
            li = ListNode(0, li)
        return li

    def get_len_linked_list(self, li):
        li_len = 0
        current = li
        while current:
            li_len = li_len + 1
            current = current.next
        return li_len

    def reverse(self, l1):
        prev = None
        current = l1
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def print_linked_list(self, li):
        current = li
        while current:
            print(current.val, end='-')
            current = current.next
        print("NULL \n")


if __name__ == '__main__':
    print ("Case 1")
    li = ListNode(7)
    li.next = ListNode(2)
    li.next.next = ListNode(4)
    li.next.next.next = ListNode(3)
    print ("Linked List 1 : ")
    Solution().print_linked_list(li)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print("Linked List 2 : ")
    Solution().print_linked_list(l2)
    sol = Solution().addTwoNumbers(li, l2)
    print("Sol : ")
    Solution().print_linked_list(sol)

