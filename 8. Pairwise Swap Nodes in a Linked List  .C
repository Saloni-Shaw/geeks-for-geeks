#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* insertAtEnd(Node* head, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    if (!head) return newNode;

    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
    return head;
}

Node* pairwiseSwap(Node* head) {
    Node* temp = head;

    while (temp != NULL && temp->next != NULL) {
        int k = temp->data;
        temp->data = temp->next->data;
        temp->next->data = k;
        temp = temp->next->next;
    }
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
    head = insertAtEnd(head, 1);
    head = insertAtEnd(head, 2);
    head = insertAtEnd(head, 3);
    head = insertAtEnd(head, 4);
    head = insertAtEnd(head, 5);

    printf("Original List: ");
    printList(head);

    head = pairwiseSwap(head);
    printf("After Pairwise Swap: ");
    printList(head);

    return 0;
}
