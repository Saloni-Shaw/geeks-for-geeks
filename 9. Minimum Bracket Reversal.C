#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    char* arr;
    int top;
} Stack;

Stack* createStack(int n) {
    Stack* s = malloc(sizeof(Stack));
    s->arr = malloc(sizeof(char)*n);
    s->top = -1;
    return s;
}

int isEmpty(Stack* s) { return s->top == -1; }
void push(Stack* s, char c) { s->arr[++(s->top)] = c; }
char pop(Stack* s) { return isEmpty(s) ? '\0' : s->arr[(s->top)--]; }

int countMinReversals(char* expr) {
    int len = 0;
    while (expr[len]) len++;
    if (len % 2 != 0) return -1;
    Stack* s = createStack(len);
    for (int i = 0; i < len; i++) {
        if (expr[i] == '{') push(s, expr[i]);
        else {
            if (!isEmpty(s) && s->arr[s->top] == '{') pop(s);
            else push(s, expr[i]);
        }
    }
    int red_len = s->top + 1, n_open = 0;
    while (!isEmpty(s) && s->arr[s->top] == '{') {
        pop(s);
        n_open++;
    }
    free(s->arr);
    free(s);
    return (red_len / 2 + n_open % 2);
}

int main() {
    char expr[] = "}{{}}{{{";
    int res = countMinReversals(expr);
    if (res == -1) printf("Invalid\n");
    else printf("%d\n", res);
    return 0;
}
