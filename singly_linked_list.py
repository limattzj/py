# This is the special import we need for class type annotations.
from __future__ import annotations

from typing import Any, Optional, List


class _Node:
    """
    A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing

    def __repr__(self):
        return str(self.item)


class SinglyLinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # The first node in this linked list, or None if this list is empty.
    head: Optional[_Node]

    def __init__(self, nodes: list = None):
        """Initialize an empty linked list. And if pass in an array of data,
        then initialize a new linked list containing the given items.
        """
        self.head = None

        # if nodes not empty, initialize a linked list with n items
        # (n = length of list of nodes)
        if nodes is not None:
            i = 0
            n = len(nodes)
            new_node = _Node(nodes[0])
            self.head = new_node

            for i in range(1, n):
                new_node.next = _Node(nodes[i])
                new_node = new_node.next

    def __repr__(self):
        results = self.to_list()
        return " -> ".join(results)

    def print_items(self) -> None:
        """Print out each item in this linked list.
        """

        # 1. Initialize curr to the start of the list
        # 2. curr is None if we've reached the end of the list.
        # 3. Do something with the current element
        # 4. "Increment" curr, setting it to refer to the next node.

        curr = self.head
        while curr is not None:
            print(curr)
            curr = curr.next

    def to_list(self) -> List[Any]:
        """Return a (built-in) list that contains the same elements as this list.
        """

        results = []
        curr = self.head
        while curr is not None:
            results.append(str(curr.item))
            curr = curr.next

        results.append("None")
        return results

    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list.

        >>> _lst = SinglyLinkedList()
        >>> _lst.append(2)
        >>> str(_lst)
        '2 -> None'

        >>> _lst = SinglyLinkedList([1,2,3,4])
        >>> _lst.append(100)
        >>> str(_lst)
        '1 -> 2 -> 3 -> 4 -> 100 -> None'

        """

        curr = self.head
        new_node = _Node(item)

        if curr is None:
            self.head = new_node

        else:

            while curr.next is not None:
                # traverse to last node in the linked list
                curr = curr.next

            # add a node after the last node
            curr.next = new_node

    def insert(self, index: int, item: Any) -> None:
        """Insert a new node containing item at position <index>.

        Precondition: index >= 0.

        Note: if index >= len(self), this method adds the item to the end
        of the linked list, which is the same as LinkedList.append.

        >>> lst = SinglyLinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '1 -> 2 -> 300 -> 10 -> 200 -> None'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '1 -> 2 -> 300 -> 10 -> 200 -> -1 -> None'
        """
        i = 0
        curr = self.head
        new_node = _Node(item)

        while (curr is not None) and (i < index - 1):
            i += 1
            curr = curr.next

        # the expressions on the right side are all evaluated before any new values are assigned, meaning that you
        # don’t need to worry about the order in which you write them
        new_node.next, curr.next = curr.next, new_node

    def pop(self, index: int) -> Any:
        """Remove and return node at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index >= len(self).

        >>> lst = SinglyLinkedList([1, 2, 10, 200])
        >>> lst.pop(2)
        10
        >>> str(lst)
        '1 -> 2 -> 200 -> None'
        >>> lst.pop(0)
        1
        >>> str(lst)
        '2 -> 200 -> None'
        """

        i = 0
        curr = self.head
        prev = None

        if curr is None:
            # if the list is empty, then we raise Error since we cannot
            # pop anything
            raise IndexError

        elif index == 0:
            # head points to the next element in the linked list, and
            # we return the current element (the prev head)
            self.head = curr.next
            return curr

        else:
            while i < index and curr is not None:
                # we keep track of the previous element, and prev element points
                # to the next element, thus the current element is no longer
                # in the linked list, and we return the current.
                # if [index] is out of bounds, then we always pop the last element in
                # the linked list.
                i += 1
                prev = curr
                curr = curr.next

            prev.next = curr.next
            return curr


if __name__ == '__main__':
    import doctest

    doctest.testmod()
