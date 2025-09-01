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

def pairwise_swap(head):
    temp = head
    while temp and temp.next:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()

if __name__ == "__main__":
    head = None
    head = insert_at_end(head, 1)
    head = insert_at_end(head, 2)
    head = insert_at_end(head, 3)
    head = insert_at_end(head, 4)
    head = insert_at_end(head, 5)

    print("Original List:", end=' ')
    print_list(head)

    head = pairwise_swap(head)
    print("After Pairwise Swap:", end=' ')
    print_list(head)
