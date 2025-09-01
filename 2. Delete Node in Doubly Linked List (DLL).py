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

def delete_node(head, del_node):
    if not head or not del_node:
        return head
    if head == del_node:
        head = del_node.next
    if del_node.next:
        del_node.next.prev = del_node.prev
    if del_node.prev:
        del_node.prev.next = del_node.next
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

    # Delete middle node (20)
    temp = head.next
    head = delete_node(head, temp)
    print("DLL after deleting 20:", end=' ')
    print_list(head)

    # Delete head node (10)
    head = delete_node(head, head)
    print("DLL after deleting 10:", end=' ')
    print_list(head)
