class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def kth_from_end(head, k):
    if head is None:
        return -1  # If the list is empty, return -1
    
    first = head
    second = head
    
    # Move the first pointer k nodes ahead
    for _ in range(k):
        if first is None:
            return -1  # If k is greater than the number of nodes
        first = first.next
    
    # Move both pointers until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next
    
    return second.data  # The second pointer is now at the k-th node from the end

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
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = create_linked_list(values)

k = 2
result = kth_from_end(head, k)
print(result)  # Output: 8

k = 5
result = kth_from_end(head, k)
print(result)  # Output: 5

k = 10
result = kth_from_end(head, k)
print(result)  # Output: -1
