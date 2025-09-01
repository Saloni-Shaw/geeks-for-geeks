#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct StackNode {
    char* str;
    struct StackNode* next;
} StackNode;

typedef struct Stack {
    StackNode* top;
} Stack;

void init(Stack* s) {
    s->top = NULL;
}

int isEmpty(Stack* s) {
    return s->top == NULL;
}

void push(Stack* s, const char* str) {
    StackNode* node = malloc(sizeof(StackNode));
    node->str = strdup(str);
    node->next = s->top;
    s->top = node;
}

char* pop(Stack* s) {
    if (isEmpty(s)) return NULL;
    StackNode* temp = s->top;
    char* res = temp->str;
    s->top = temp->next;
    free(temp);
    return res;
}

int main() {
    int Q;
    scanf("%d", &Q);
    Stack s;
    init(&s);
    char current[100000] = "";
    push(&s, current);

    for (int i = 0; i < Q; i++) {
        int t;
        scanf("%d", &t);
        if (t == 1) {
            char w[100000];
            scanf("%s", w);
            strcat(current, w);
            push(&s, current);
        } else if (t == 2) {
            int k;
            scanf("%d", &k);
            int len = strlen(current);
            current[len - k] = '\0';
            push(&s, current);
        } else if (t == 3) {
            int k;
            scanf("%d", &k);
            printf("%c\n", current[k - 1]);
        } else if (t == 4) {
            free(current);
            char* prev = pop(&s);
            if (prev) {
                strcpy(current, prev);
                free(prev);
            }
        }
    }
    // Free remaining stack nodes
    while (!isEmpty(&s)) {
        free(pop(&s));
    }
    return 0;
}

