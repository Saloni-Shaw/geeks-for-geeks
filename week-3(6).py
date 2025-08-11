class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def detect_loop(head, pos):
    if head is None:
        return False  # If the list is empty, there is no loop

    # Create a loop if pos is not 0
    if pos > 0:
        loop_start_node = None
        current = head
        for i in range(1, pos + 1):
            if current is None:
                return False  # If pos is greater than the number of nodes
            if i == pos:
                loop_start_node = current
            current = current.next
        
        # Connect the last node to the loop start node
        if current is not None:
            current.next = loop_start_node

    # Detect loop using Floyd's Cycle Detection Algorithm
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Loop detected

    return False  # No loop detected

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage:
values = [1, 3, 4]
head = create_linked_list(values)
pos = 2
result = detect_loop(head, pos)
print(result)  # Output: True

values = [1, 8, 3, 4]
head = create_linked_list(values)
pos = 0
result = detect_loop(head, pos)
print(result)  # Output: False

values = [1, 2, 3, 4]
head = create_linked_list(values)
pos = 1
result = detect_loop(head, pos)
print(result)  # Output: True
