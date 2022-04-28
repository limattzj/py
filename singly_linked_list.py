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
    _first: Optional[_Node]

    def __init__(self):
        """Initialize an empty linked list.
        TODO: Initialize a new linked list containing the given items.
        """
        self._first = None

    def print_items(self) -> None:
        """Print out each item in this linked list.
        """

        _curr = self._first              # 1. Initialize curr to the start of the list
        while _curr is not None:        # 2. curr is None if we've reached the end of the list.
            print(_curr)                # 3. Do something with the current element
            _curr = _curr.next          # 4. "Increment" curr, setting it to refer to the next node.

    def to_list(self) -> List[Any]:
        """Return a (built-in) list that contains the same elements as this list.
        """

        _results = []
        _curr = self._first
        while _curr is not None:
            _results.append(_curr.item)
            _curr = _curr.next

        return _results

    def append(self, item: Any) -> None:
        """TODO: Add the given item to the end of this linked list."""
        pass

    def insert(self, index: int, item: Any) -> None:
        """Insert a new node containing item at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index > len(self).

        Note: if index == len(self), this method adds the item to the end
        of the linked list, which is the same as LinkedList.append.

        >>> _lst = SinglyLinkedList([1, 2, 10, 200])
        >>> _lst.insert(2, 300)
        >>> str(_lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> _lst.insert(5, -1)
        >>> str(_lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        """
        pass

    def pop(self, index: int) -> Any:
        """Remove and return node at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index >= len(self).

        >>> lst = SinglyLinkedList([1, 2, 10, 200])
        >>> lst.pop(2)
        10
        >>> lst.pop(0)
        1
        """


if __name__ == '__main__':
    linky = SinglyLinkedList()          # linky is empty
    node1 = _Node(10)
    node2 = _Node(20)
    node3 = _Node(30)
    node1.next = node2
    node2.next = node3

    linky._first = node1

    linky.print_items()
    lst = linky.to_list()
    print(f'linky contains {lst}')
