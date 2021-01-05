"""
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @classmethod
    def printList(cls, l):
        while l:
            print (l.val, end=", ")
            l = l.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        curr = output
        while l1 and l2:
            l1val, l2val = (l1.val, l2.val)
            print(l1val, l2val)
            if l1val < l2val:
                print("L1 Is greater", l1val)
                curr.next = ListNode(val=l1val)
                curr = curr.next
                l1 = l1.next
            else:
                print("L2 Is greater", l2val)
                curr.next = ListNode(val=l2val)
                curr = curr.next
                l2 = l2.next

        if l1:
            while l1:
                l1val = l1.val
                print("L1", l1val)
                curr.next = ListNode(val=l1val)
                curr = curr.next
                l1 = l1.next

        if l2:
            while l2:
                l2val = l2.val
                print("L2", l2val)
                curr.next = ListNode(val=l2val)
                curr = curr.next
                l2 = l2.next

        return output.next


if  __name__ == '__main__':
    print ("Running merge two sorted linked list")
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print ("Case 1,\nL1:")
    Solution.printList(l1)

    print ("L2:")
    Solution.printList(l2)
    print("\n")

    sol = Solution().mergeTwoLists(l1,l2)
    print ("Solution : ")
    Solution.printList(sol)
    print ("\n")