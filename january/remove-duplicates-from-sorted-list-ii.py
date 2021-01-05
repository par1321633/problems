"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, l1: ListNode) -> ListNode:
        output = ListNode()
        curr = output
        while l1:
            i = 0
            while l1.next and l1.val ==l1.next.val:
                l1 = l1.next
                i = i + 1
            if i == 0:
                curr.next = ListNode(l1.val)
                curr = curr.next
            l1 = l1.next
        return output.next

    @classmethod
    def printList(cls, l):
        while l:
            print(l.val, end=", ")
            l = l.next


if  __name__ == '__main__':
    print ("Running remove duplicates from sorted list")
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next.next = ListNode(5)

    print ("Case 1")
    Solution.printList(l1)
    print("\n")

    sol = Solution().deleteDuplicates(l1)
    print ("Solution : ")
    Solution.printList(sol)
    print("\n")

    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(3)

    print("Case 2")
    Solution.printList(l1)
    print ("\n")

    sol = Solution().deleteDuplicates(l1)
    print("Solution : ")
    Solution.printList(sol)
    print("\n")

