#include <stdio.h>
#include <stdlib.h>

typedef struct NodeCLL {
    int data;
    struct NodeCLL* next;
} NodeCLL;

NodeCLL* insertInCircularList(NodeCLL* head, int data) {
    NodeCLL* newNode = (NodeCLL*)malloc(sizeof(NodeCLL));
    newNode->data = data;
    if (!head) {
        newNode->next = newNode;
        return newNode;
    }
    NodeCLL* temp = head;
    while (temp->next != head)
        temp = temp->next;
    temp->next = newNode;
    newNode->next = head;
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
    head = insertInCircularList(head, 10);
    head = insertInCircularList(head, 20);
    head = insertInCircularList(head, 30);
    printf("Circular Linked List: ");
    printCircularList(head);
    return 0;
}
