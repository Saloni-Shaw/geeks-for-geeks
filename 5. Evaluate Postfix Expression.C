#include <stdio.h>
#include <ctype.h>

#define MAX 100

typedef struct Stack {
    int arr[MAX];
    int top;
} Stack;

void init(Stack* s) { s->top = -1; }
int isEmpty(Stack* s) { return s->top == -1; }
void push(Stack* s, int val) { s->arr[++(s->top)] = val; }
int pop(Stack* s) { return isEmpty(s) ? -1 : s->arr[(s->top)--]; }

int evaluatePostfix(char* exp) {
    Stack s;
    init(&s);
    for (int i = 0; exp[i]; i++) {
        char c = exp[i];
        if (isdigit(c))
            push(&s, c - '0');
        else {
            int val2 = pop(&s);
            int val1 = pop(&s);
            if (c == '+') push(&s, val1 + val2);
            else if (c == '-') push(&s, val1 - val2);
            else if (c == '*') push(&s, val1 * val2);
            else if (c == '/') push(&s, val1 / val2);
        }
    }
    return pop(&s);
}

int main() {
    char exp[] = "231*+9-";
    printf("%d\n", evaluatePostfix(exp));
    return 0;
}
