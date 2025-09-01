#include <stdio.h>
#include <ctype.h>

#define MAX 100

typedef struct Stack {
    char arr[MAX];
    int top;
} Stack;

void init(Stack* s) { s->top = -1; }
int isEmpty(Stack* s) { return s->top == -1; }
void push(Stack* s, char c) { s->arr[++(s->top)] = c; }
char pop(Stack* s) { return isEmpty(s) ? '\0' : s->arr[(s->top)--]; }
char peek(Stack* s) { return isEmpty(s) ? '\0' : s->arr[s->top]; }

int precedence(char c) {
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    return 0;
}

void infixToPostfix(char* infix, char* postfix) {
    Stack s;
    init(&s);
    int k = 0;
    for (int i = 0; infix[i]; i++) {
        char c = infix[i];
        if (isalnum(c))
            postfix[k++] = c;
        else if (c == '(')
            push(&s, c);
        else if (c == ')') {
            while (!isEmpty(&s) && peek(&s) != '(')
                postfix[k++] = pop(&s);
            pop(&s);
        }
        else {
            while (!isEmpty(&s) && precedence(peek(&s)) >= precedence(c))
                postfix[k++] = pop(&s);
            push(&s, c);
        }
    }
    while (!isEmpty(&s))
        postfix[k++] = pop(&s);
    postfix[k] = '\0';
}

int main() {
    char infix[] = "a+b*(c-d)+e";
    char postfix[100];
    infixToPostfix(infix, postfix);
    printf("%s\n", postfix);
    return 0;
}
