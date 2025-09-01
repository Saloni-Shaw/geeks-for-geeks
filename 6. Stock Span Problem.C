#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    int* arr;
    int top;
} Stack;

Stack* createStack(int n) {
    Stack* s = malloc(sizeof(Stack));
    s->arr = malloc(sizeof(int)*n);
    s->top = -1;
    return s;
}

int isEmpty(Stack* s) { return s->top == -1; }
void push(Stack* s, int val) { s->arr[++(s->top)] = val; }
int pop(Stack* s) { return isEmpty(s) ? -1 : s->arr[(s->top)--]; }
int peek(Stack* s) { return isEmpty(s) ? -1 : s->arr[s->top]; }

void calculateSpan(int price[], int n, int span[]) {
    Stack* s = createStack(n);
    push(s, 0);
    span[0] = 1;
    for (int i = 1; i < n; i++) {
        while (!isEmpty(s) && price[peek(s)] <= price[i])
            pop(s);
        span[i] = isEmpty(s) ? i + 1 : i - peek(s);
        push(s, i);
    }
    free(s->arr);
    free(s);
}

int main() {
    int price[] = {100, 80, 60, 70, 60, 75, 85};
    int n = sizeof(price)/sizeof(price[0]);
    int span[n];
    calculateSpan(price, n, span);
    for (int i = 0; i < n; i++) printf("%d ", span[i]);
    printf("\n");
    return 0;
}
