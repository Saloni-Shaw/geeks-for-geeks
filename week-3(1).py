class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insert_at_end(head, x):
    new_node = ListNode(x)  # Create a new node with the value x
    
    if head is None:
        return new_node  # If the list is empty, return the new node as the head
    
    # Traverse to the end of the linked list
    current = head
    while current.next:
        current = current.next
    
    # Link the new node at the end
    current.next = new_node
    return head  # Return the head of the modified linked list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "")
        current = current.next
    print()  # For a new line at the end

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Inserting 6 at the end
head = insert_at_end(head, 6)
print_linked_list(head)  # Output: 1->2->3->4->5->6

# Inserting 1 at the end of another linked list: 5 -> 4
head2 = ListNode(5, ListNode(4))
head2 = insert_at_end(head2, 1)
print_linked_list(head2)  # Output: 5->4->1
