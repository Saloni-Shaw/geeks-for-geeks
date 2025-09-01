#include <stdio.h>
#include <stdlib.h>

typedef struct NodeCLL {
    int data;
    struct NodeCLL* next;
} NodeCLL;

NodeCLL* sortedInsert(NodeCLL* head, int data) {
    NodeCLL* newNode = (NodeCLL*)malloc(sizeof(NodeCLL));
    newNode->data = data;

    if (!head) {
        newNode->next = newNode;
        return newNode;
    }

    NodeCLL* current = head;
    // If new node is to be inserted before head node
    if (data <= head->data) {
        while (current->next != head)
            current = current->next;
        current->next = newNode;
        newNode->next = head;
        head = newNode;
        return head;
    }

    // Locate the node after which the new node is to be inserted
    while (current->next != head && current->next->data < data)
        current = current->next;

    newNode->next = current->next;
    current->next = newNode;

    return head;
}

void printCircularList(NodeCLL* head) {
    if (!head) return;
    NodeCLL* temp = head;
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

int main() {
    NodeCLL* head = NULL;
    head = sortedInsert(head, 20);
    head = sortedInsert(head, 10);
    head = sortedInsert(head, 30);
    head = sortedInsert(head, 25);
    printf("Sorted Circular Linked List: ");
    printCircularList(head);
    return 0;
}
