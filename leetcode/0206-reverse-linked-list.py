from typing import List, Optional


class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a singly linked list, reverse the list.

    [1,2,3,4,5] -> [5,4,3,2,1]

    Args:
        head: a pointer that points to the head of the linked list.

    Returns:
        a pointer that is the new head of the reversed linked list.
    """
    prev = None
    curr = head

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
