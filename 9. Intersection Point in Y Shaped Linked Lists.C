#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* newNode(int data) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

int getCount(Node* head) {
    int count = 0;
    while (head) {
        count++;
        head = head->next;
    }
    return count;
}

Node* getIntersectionNode(int d, Node* head1, Node* head2) {
    for (int i = 0; i < d; i++) {
        if (head1 == NULL) return NULL;
        head1 = head1->next;
    }
    while (head1 && head2) {
        if (head1 == head2)
            return head1;
        head1 = head1->next;
        head2 = head2->next;
    }
    return NULL;
}

Node* findIntersection(Node* head1, Node* head2) {
    int c1 = getCount(head1);
    int c2 = getCount(head2);
    int d;
    if (c1 > c2) {
        d = c1 - c2;
        return getIntersectionNode(d, head1, head2);
    } else {
        d = c2 - c1;
        return getIntersectionNode(d, head2, head1);
    }
}

int main() {
    Node* newNode1;
    Node* head1 = newNode(10);
    head1->next = newNode(15);
    head1->next->next = newNode(30);

    Node* head2 = newNode(3);
    head2->next = newNode(6);
    head2->next->next = newNode(9);
    head2->next->next->next = head1->next; // Intersection at node with data 15

    Node* interNode = findIntersection(head1, head2);
    if (interNode)
        printf("Intersection at node with data = %d\n", interNode->data);
    else
        printf("No intersection found\n");
    return 0;
}
