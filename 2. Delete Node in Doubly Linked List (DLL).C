#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next, *prev;
} Node;

Node* insertAtEnd(Node* head, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    if (head == NULL) return newNode;

    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

Node* deleteNode(Node* head, Node* del) {
    if (head == NULL || del == NULL) return head;
    if (head == del) head = del->next;
    if (del->next) del->next->prev = del->prev;
    if (del->prev) del->prev->next = del->next;
    free(del);
    return head;
}

void printList(Node* head) {
    Node* temp = head;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);
    printf("Original DLL: ");
    printList(head);

    // Delete middle node (20)
    Node* temp = head->next;
    head = deleteNode(head, temp);
    printf("DLL after deleting 20: ");
    printList(head);

    // Delete head node (10)
    head = deleteNode(head, head);
    printf("DLL after deleting 10: ");
    printList(head);

    return 0;
}
