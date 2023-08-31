class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def solution(headA, headB):
    firstPointer = headA
    secondPointer = headB

    while firstPointer != secondPointer:
        firstPointer = firstPointer.next if firstPointer != None else headB
        secondPointer = secondPointer.next if secondPointer != None else headA

    return firstPointer