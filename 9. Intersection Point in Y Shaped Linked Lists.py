class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_count(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count

def get_intersection_node(d, head1, head2):
    for _ in range(d):
        if not head1:
            return None
        head1 = head1.next
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

def find_intersection(head1, head2):
    c1 = get_count(head1)
    c2 = get_count(head2)
    if c1 > c2:
        d = c1 - c2
        return get_intersection_node(d, head1, head2)
    else:
        d = c2 - c1
        return get_intersection_node(d, head2, head1)

if __name__ == "__main__":
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)
    head2.next.next.next = head1.next  # Intersection at node with data 15

    inter_node = find_intersection(head1, head2)
    if inter_node:
        print("Intersection at node with data =", inter_node.data)
    else:
        print("No intersection found")
