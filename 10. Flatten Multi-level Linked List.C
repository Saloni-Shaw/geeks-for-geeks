#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* right;
    struct Node* down;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->right = NULL;
    newNode->down = NULL;
    return newNode;
}

Node* merge(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;

    Node* result;

    if (a->data < b->data) {
        result = a;
        result->down = merge(a->down, b);
    } else {
        result = b;
        result->down = merge(a, b->down);
    }
    result->right = NULL;
    return result;
}

Node* flatten(Node* root) {
    if (!root || !root->right)
        return root;
    root->right = flatten(root->right);
    root = merge(root, root->right);
    return root;
}

void printList(Node* head) {
    while (head) {
        printf("%d ", head->data);
        head = head->down;
    }
    printf("\n");
}

int main() {
    Node* root = createNode(5);
    root->right = createNode(10);
    root->right->right = createNode(19);
    root->right->right->right = createNode(28);

    root->down = createNode(7);
    root->down->down = createNode(8);
    root->down->down->down = createNode(30);

    root->right->down = createNode(20);

    root->right->right->down = createNode(22);
    root->right->right->down->down = createNode(50);

    root->right->right->right->down = createNode(35);
    root->right->right->right->down->down = createNode(40);
    root->right->right->right->down->down->down = createNode(45);

    root = flatten(root);

    printf("Flattened list: ");
    printList(root);

    return 0;
}
