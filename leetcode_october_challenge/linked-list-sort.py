"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Input: head = [4,2,1,3]
Output: [1,2,3,4]


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        middle = self.getMiddle(head)
        nexttomiddle = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a

        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def getMiddle(self, head):
        if (head == None):
            return head
        slow = head
        fast = head
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        unsorted = True
        while unsorted:
            unsorted = False
            current = head
            while current.next:
                print (current.val)
                print (current.next.val)
                if current.val > current.next.val:
                    current.val , current.next.val = current.next.val, current.val
                    unsorted = True
                current = current.next
        return head

def printList(llist):
    temp = llist
    while temp != None:
        print (temp.val, end='')
        temp = temp.next


if __name__ == '__main__':
    lhead = ListNode(4)
    lhead.next = ListNode(2)
    lhead.next.next = ListNode(1)
    lhead.next.next.next = ListNode(3)
    print ("Input : {}".format(printList(lhead)))
    ans = Solution().sortList(head=lhead)
    printList(ans)