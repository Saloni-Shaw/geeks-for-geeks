class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev      # Reverse the current node's pointer
        prev = current           # Move prev to current node
        current = next_node      # Move current to next node
    
    return prev  # prev becomes the new head

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

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()  # For a new line at the end

# Example usage:
values = [1, 2, 3, 4]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed list:")
print_linked_list(reversed_head)

values = [2, 7, 10, 9, 8]
head = create_linked_list(values)
print("\nOriginal list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed list:")
print_linked_list(reversed_head)

values = [2]
head = create_linked_list(values)
print("\nOriginal list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed list:")
print_linked_list(reversed_head)
