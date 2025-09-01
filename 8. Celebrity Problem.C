#include <stdio.h>

#define N 4

int M[N][N] = {
    {0, 0, 1, 0},
    {0, 0, 1, 0},
    {0, 0, 0, 0},
    {0, 0, 1, 0}
};

int knows(int a, int b) {
    return M[a][b];
}

int findCelebrity() {
    int c = 0;
    for (int i = 1; i < N; i++) {
        if (knows(c, i)) c = i;
    }
    for (int i = 0; i < N; i++) {
        if (i != c && (knows(c, i) || !knows(i, c))) return -1;
    }
    return c;
}

int main() {
    int c = findCelebrity();
    if (c == -1) printf("No celebrity\n");
    else printf("Celebrity is %d\n", c);
    return 0;
}
