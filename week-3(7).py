class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def remove_loop(head):
    if head is None:
        return False  # If the list is empty, no loop to remove

    slow = head
    fast = head

    # Detect loop using Floyd's Cycle Detection Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Loop detected
            break
    else:
        return False  # No loop detected

    # Find the starting point of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Now `slow` (or `fast`) is at the start of the loop
    # Find the last node in the loop
    while fast.next != slow:
        fast = fast.next

    # Remove the loop
    fast.next = None
    return True  # Loop removed

# Helper function to create a linked list from a list of values
def create_linked_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    loop_start_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos - 1:  # pos is 1-based index
            loop_start_node = current

    if loop_start_node:
        current.next = loop_start_node  # Create a loop

    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    visited = set()
    while current and current not in visited:
        visited.add(current)
        print(current.data, end="->" if current.next else "")
        current = current.next
    if current:
        print("... (loop detected)")
    else:
        print()  # For a new line at the end

# Example usage:
values = [1, 3, 4]
head = create_linked_list(values, pos=2)
result = remove_loop(head)
print(result)  # Output: True
print_linked_list(head)  # Should print the list without a loop

values = [1, 8, 3, 4]
head = create_linked_list(values, pos=0)
result = remove_loop(head)
print(result)  # Output: True
print_linked_list(head)  # Should print the list without a loop

values = [1, 2, 3, 4]
head = create_linked_list(values, pos=1)
result = remove_loop(head)
print(result)  # Output: True
print_linked_list(head)  # Should print the list without a loop
