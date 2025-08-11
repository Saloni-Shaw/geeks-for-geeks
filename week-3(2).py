class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insert_in_middle(head, x):
    new_node = ListNode(x)  # Create a new node with the value x
    
    if head is None:
        return new_node  # If the list is empty, return the new node as the head
    
    # Initialize slow and fast pointers
    slow = head
    fast = head
    prev = None  # To keep track of the node before slow
    
    # Use the fast and slow pointer technique to find the middle
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Insert the new node after the current middle node
    if prev is None:
        # This means the list had only one element
        new_node.next = head
        return new_node  # New node becomes the new head
    else:
        new_node.next = slow
        prev.next = new_node
    
    return head  # Return the head of the modified linked list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "")
        current = current.next
    print()  # For a new line at the end

# Example usage:
# Creating a linked list: 1 -> 2 -> 4
head1 = ListNode(1, ListNode(2, ListNode(4)))

# Inserting 3 in the middle
head1 = insert_in_middle(head1, 3)
print_linked_list(head1)  # Output: 1->2->3->4

# Creating another linked list: 10 -> 20 -> 40 -> 50
head2 = ListNode(10, ListNode(20, ListNode(40, ListNode(50))))

# Inserting 30 in the middle
head2 = insert_in_middle(head2, 30)
print_linked_list(head2)  # Output: 10->20->30->40->50
