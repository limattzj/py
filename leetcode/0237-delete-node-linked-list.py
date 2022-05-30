# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteNode(node):
    """A function to delete a node in a singly-linked list.
    Args:
        node: pointer of the node to be deleted.

    Returns:
        None

    """

    # the current node becomes the next node
    node.val = node.next.val
    node.next = node.next.next
