#include <stdio.h>
#include <string.h>

#define MAX 1000

typedef struct Stack {
    char arr[MAX];
    int top;
} Stack;

void init(Stack* s) { s->top = -1; }
int isEmpty(Stack* s) { return s->top == -1; }
void push(Stack* s, char c) { s->arr[++(s->top)] = c; }
char pop(Stack* s) { return isEmpty(s) ? '\0' : s->arr[(s->top)--]; }

int isMatchingPair(char a, char b) {
    return (a == '(' && b == ')') || (a == '{' && b == '}') || (a == '[' && b == ']');
}

int isBalanced(char* expr) {
    Stack s;
    init(&s);
    for (int i = 0; expr[i]; i++) {
        if (expr[i] == '(' || expr[i] == '{' || expr[i] == '[')
            push(&s, expr[i]);
        else if (expr[i] == ')' || expr[i] == '}' || expr[i] == ']') {
            if (isEmpty(&s)) return 0;
            if (!isMatchingPair(pop(&s), expr[i])) return 0;
        }
    }
    return isEmpty(&s);
}

int main() {
    char expr[] = "{([])}";
    printf(isBalanced(expr) ? "Balanced\n" : "Not Balanced\n");
    return 0;
}
