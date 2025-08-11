class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.data)  # Print the data of the current node
        current = current.next  # Move to the next node

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
# Sample input
n = 2
values = [16, 13]

# Create the linked list
head = create_linked_list(values)

# Print the linked list
print_linked_list(head)
