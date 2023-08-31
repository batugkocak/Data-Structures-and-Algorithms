#  RemoveNthNode From End Of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeFromEnd(head: ListNode, n: int) -> ListNode:
    leftPointer = head
    rightPointer = head

    while n > 0 and rightPointer:
        rightPointer = rightPointer.next
        n -= 1
    while rightPointer and rightPointer.next:
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next
    if leftPointer == head and not rightPointer:  # if LinkedList has 1 element
        return head.next

    leftPointer.next = leftPointer.next.next  # leftPointer.next is going to trash
