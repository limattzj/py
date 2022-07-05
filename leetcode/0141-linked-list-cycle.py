

# Definition for the singly linked list
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __eq__(self, other):
		if other is not None:
			if self.val == other.val:
				return True

		return False


def hasCycle(head):
	"""
	Given head of a linked list, determine if the linked list has a cycle in it.

	Args:
		head: head pointer of the linked list

	Returns:
		True if the linked list contains a cycle


	Loop Termination Condition:
		if fast is None or fast.next is None

	"""
	if head is None:
		return False

	slow = head
	fast = head

	while (fast is not None and fast.next is not None):
		slow = slow.next
		fast = fast.next.next

		if (slow == fast):
			return True

	return False


if __name__ == "__main__":

	a = ListNode(3)
	b = ListNode(2)
	c = ListNode(0)
	d = ListNode(4)

	a.next = b
	b.next = c
	c.next = d
	d.next = b

	head = a
	

	result = hasCycle(head)
	print(f'result 1: {result}')


	a1 = ListNode(3)
	b1 = ListNode(2)
	c1 = ListNode(0)
	d1 = ListNode(4)

	a1.next = b1
	b1.next = c1
	c1.next = d1

	head = a1

	result = hasCycle(head)
	print(f'result 2: {result}')




