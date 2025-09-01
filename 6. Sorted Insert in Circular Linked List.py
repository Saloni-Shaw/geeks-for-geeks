class NodeCLL:
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = NodeCLL(data)
    if not head:
        new_node.next = new_node
        return new_node
    current = head
    if data <= head.data:
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        head = new_node
        return head
    while current.next != head and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

def print_circular_list(head):
    if not head:
        return
    temp = head
    while True:
        print(temp.data, end=' ')
        temp = temp.next
        if temp == head:
            break
    print()

if __name__ == "__main__":
    head = None
    head = sorted_insert(head, 20)
    head = sorted_insert(head, 10)
    head = sorted_insert(head, 30)
    head = sorted_insert(head, 25)
    print("Sorted Circular Linked List:", end=' ')
    print_circular_list(head)
