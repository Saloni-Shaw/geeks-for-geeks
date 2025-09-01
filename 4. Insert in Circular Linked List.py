class NodeCLL:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_in_circular_list(head, data):
    new_node = NodeCLL(data)
    if not head:
        new_node.next = new_node
        return new_node
    temp = head
    while temp.next != head:
        temp = temp.next
    temp.next = new_node
    new_node.next = head
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
    head = insert_in_circular_list(head, 10)
    head = insert_in_circular_list(head, 20)
    head = insert_in_circular_list(head, 30)
    print("Circular Linked List:", end=' ')
    print_circular_list(head)
