class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def search_linked_list(head, key):
    current = head
    while current:
        if current.data == key:
            return True  # Key found
        current = current.next
    return False  # Key not found

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
values = [1, 2, 3, 4]
head = create_linked_list(values)

key = 3
result = search_linked_list(head, key)
print(result)  # Output: True

key = 5
result = search_linked_list(head, key)
print(result)  # Output: False
