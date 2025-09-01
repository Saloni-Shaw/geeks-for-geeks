#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void insertEnd(struct Node** head, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = new_node;
}

int nthFromEnd(struct Node* head, int n) {
    struct Node *main_ptr = head, *ref_ptr = head;
    int count = 0;
    while (count < n) {
        if (ref_ptr == NULL)
            return -1;
        ref_ptr = ref_ptr->next;
        count++;
    }
    while (ref_ptr != NULL) {
        main_ptr = main_ptr->next;
        ref_ptr = ref_ptr->next;
    }
    return main_ptr->data;
}

int main() {
    struct Node* head = NULL;
    insertEnd(&head, 10);
    insertEnd(&head, 20);
    insertEnd(&head, 30);
    printf("%d\n", nthFromEnd(head, 2)); 
    return 0;
}
