"""
https://leetcode.com/explore/rotate-list

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        print(head)
        if head is None:
            return head
        current = head

        count = 0
        while (current is not None):
            current = current.next
            count += 1
        print(count)
        print(k)
        k = k % count
        for i in range(k):
            #print("HEAD VAL : {}".format(head.val))
            current = head
            i = 0
            while (current.next):
                print(i, current.val)
                i = i + 1
                if i == count - 1:
                    #print(current.next.val)
                    current.next.next = head
                    head = current.next
                    current.next = None
                    #print("DO HERE : {}".format(current.val))
                    # current.next  = head
                else:
                    current = current.next
            # head = current
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    z = Solution().rotateRight(head, 2)
    print ("Solution")
    while (z):
        print(z.val, end=' ')
        z = z.next