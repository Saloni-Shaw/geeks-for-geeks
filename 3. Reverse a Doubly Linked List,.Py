class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    return head

def reverse_dll(head):
    current = head
    temp = None
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp:
        head = temp.prev
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()

if __name__ == "__main__":
    head = None
    head = insert_at_end(head, 10)
    head = insert_at_end(head, 20)
    head = insert_at_end(head, 30)
    print("Original DLL:", end=' ')
    print_list(head)

    head = reverse_dll(head)
    print("Reversed DLL:", end=' ')
    print_list(head)
