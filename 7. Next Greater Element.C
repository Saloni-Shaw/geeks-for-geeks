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

void nextGreaterElement(int arr[], int n, int res[]) {
    Stack* s = createStack(n);
    for (int i = n-1; i >= 0; i--) {
        while (!isEmpty(s) && peek(s) <= arr[i])
            pop(s);
        res[i] = isEmpty(s) ? -1 : peek(s);
        push(s, arr[i]);
    }
    free(s->arr);
    free(s);
}

int main() {
    int arr[] = {4, 5, 2, 25};
    int n = sizeof(arr)/sizeof(arr[0]);
    int res[n];
    nextGreaterElement(arr, n, res);
    for (int i = 0; i < n; i++) printf("%d ", res[i]);
    printf("\n");
    return 0;
}
