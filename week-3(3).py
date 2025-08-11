class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def delete_node(head, x):
    if head is None:
        return None  # If the list is empty, return None
    
    # If we need to delete the head node
    if x == 1:
        return head.next  # Return the new head (second node)
    
    current = head
    # Traverse to the (x-1)th node
    for _ in range(x - 2):
        if current is None:
            return head  # If x is out of bounds, return the original list
        current = current.next
    
    # If current is None, x is out of bounds
    if current is None or current.next is None:
        return head  # If x is out of bounds, return the original list
    
    # Delete the x-th node
    current.next = current.next.next  # Bypass the x-th node
    
    return head  # Return the head of the modified linked list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "")
        current = current.next
    print()  # For a new line at the end

# Example usage:
# Creating a linked list: 1 -> 3 -> 4
head1 = ListNode(1, ListNode(3, ListNode(4)))

# Deleting the 3rd node
head1 = delete_node(head1, 3)
print_linked_list(head1)  # Output: 1->3

# Creating another linked list: 1 -> 5 -> 2 -> 9
head2 = ListNode(1, ListNode(5, ListNode(2, ListNode(9))))

# Deleting the 2nd node
head2 = delete_node(head2, 2)
print_linked_list(head2)  # Output: 1->2->9
