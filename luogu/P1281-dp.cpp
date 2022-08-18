/*
Solution: range dp
suppose f(p, b) be the min time to copy b books with p people
then f(p, b) = min_i{ max(f(p-1, b-i), sum(pages[b-i+1:b]))}
note that this method is O(k*n^2), but also,
we find that sum(pages[b-i+1:b]) is increasing when i leads to be larger,
so when it is bigger than current f(p, b), interupt loop! (a simple pruning)
*/
#include <iostream>
using namespace std;
const int MAX_NUM = 500;
int pages[MAX_NUM], MIN_TIME[MAX_NUM][MAX_NUM], pathes[MAX_NUM][MAX_NUM]; // p, b
int lefts[MAX_NUM], rights[MAX_NUM];
int main() {
    int m, k;
    scanf("%d %d", &m, &k);
    for (int i = 0; i < m; i++) {
        scanf("%d", &pages[i]);
    }
    MIN_TIME[0][0] = pages[0];
    for (int i = 1; i < m; i++) {
        MIN_TIME[0][i] = MIN_TIME[0][i-1] + pages[i];
        pathes[0][i] = 0;
    }
    for (int p = 1; p < k; p++) {
        for (int b = 0; b < m; b++) {
            int pk_start = b, pk_pagesum = 0, time_min = MIN_TIME[p-1][b];
            pathes[p][b] = pk_start + 1;
            while (true) {
                if (pk_start < 0) { break; }
                pk_pagesum += pages[pk_start];
                pk_start--;
                int min_this = pk_pagesum;
                if (pk_start >= 0) {
                    min_this = std::max(min_this, MIN_TIME[p-1][pk_start]);
                }
                if (min_this <= time_min) {
                    time_min = min_this;
                    pathes[p][b] = pk_start + 1;
                } else {
                    break;
                }
            }
            MIN_TIME[p][b] = time_min;
        }
    }

    // BUG OUTPUT with data:
    // 10 4
    // 1 1 1 1 1 1 1 1 1 1
    // int book_id = m - 1;
    // for (int p = k-1; p >= 0; p--) {
    //     rights[p] = book_id + 1;
    //     lefts[p] = pathes[p][book_id] + 1;
    //     book_id = pathes[p][book_id] - 1;
    // }

    // for (int p = 0; p < k; p++) {
    //     printf("%d %d\n", lefts[p], rights[p]);
    // }

    // CORRECT OUTPUT
    int _sum = 0, high = m - 1, person = k-1;
    for (int b = m-1; b >= 0; b--) {
        _sum += pages[b];
        if (_sum > MIN_TIME[k-1][m-1]) {
            rights[person] = high + 1;
            lefts[person] = b + 2;
            high = b;
            person--;
            _sum = pages[b];
        }
    }
    lefts[0] = 1;
    rights[0] = high + 1;

    for (int p = 0; p < k; p++) {
        printf("%d %d\n", lefts[p], rights[p]);
    }

    // for (int p = 0; p < k; p++) {
    //     printf("p=%d: ", p);
    //     for (int b = 0; b < m; b++) {
    //         printf("%d ", MIN_TIME[p][b]);
    //     }
    //     printf("\n");
    // }
    // printf("%d\n", MIN_TIME[k-1][m-1]);
    // for (int p = 0; p < k; p++) {
    //     printf("p=%d: ", p);
    //     for (int b = 0; b < m; b++) {
    //         printf("%d ", pathes[p][b]);
    //     }
    //     printf("\n");
    // }

    return 0;
}