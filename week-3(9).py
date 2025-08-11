class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def add_two_numbers(head1, head2):
    # Initialize a dummy node to help build the result list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Pointers for both linked lists
    p1 = head1
    p2 = head2

    while p1 or p2 or carry:
        # Get the values from the current nodes, or 0 if we've reached the end
        val1 = p1.data if p1 else 0
        val2 = p2.data if p2 else 0

        # Calculate the sum and the carry
        total = val1 + val2 + carry
        carry = total // 10  # Update carry for the next iteration
        current.next = ListNode(total % 10)  # Create a new node with the digit

        # Move to the next nodes in the lists
        current = current.next
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    # The result is in the next of the dummy head
    return dummy_head.next

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
head1 = create_linked_list([4, 5])
head2 = create_linked_list([3, 4, 5])
result = add_two_numbers(head1, head2)
print("Sum of linked lists:")
print_linked_list(result)  # Output: 3 -> 9 -> 0

head1 = create_linked_list([0, 0, 6, 3])
head2 = create_linked_list([0, 7])
result = add_two_numbers(head1, head2)
print("Sum of linked lists:")
print_linked_list(result)  # Output: 7 -> 0
