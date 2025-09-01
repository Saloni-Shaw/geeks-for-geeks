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

    if (head == NULL) return newNode;

    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
    return head;
}

int isCircular(Node* head) {
    if (!head) return 1; // empty list is considered circular
    Node* temp = head->next;
    while (temp != NULL && temp != head)
        temp = temp->next;
    return (temp == head);
}

int main() {
    Node* head = NULL;
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);

    printf("Is list circular? %s\n", isCircular(head) ? "Yes" : "No");

    // Making list circular
    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = head;

    printf("After making circular, is list circular? %s\n", isCircular(head) ? "Yes" : "No");
    return 0;
}
