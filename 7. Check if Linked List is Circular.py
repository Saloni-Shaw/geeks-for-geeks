class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

def is_circular(head):
    if not head:
        return True
    temp = head.next
    while temp is not None and temp != head:
        temp = temp.next
    return temp == head

if __name__ == "__main__":
    head = None
    head = insert_at_end(head, 10)
    head = insert_at_end(head, 20)
    head = insert_at_end(head, 30)

    print("Is list circular?", "Yes" if is_circular(head) else "No")

    # Make it circular
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = head

    print("After making circular, is list circular?", "Yes" if is_circular(head) else "No")
