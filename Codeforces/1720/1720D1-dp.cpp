/*
Solution: dp
note that 0 <= a_i <= 200, then we only need to consider the last appeared a_i of each value, when we use dp to consider
which positions can be the pred adjacent node of the sequence
let f(m) be the longest sequence length of beautiful subsequence ends at a[m], the final result is just max{f(m)}
let d[v] denote the lastest index i (i < m, dynamic holds) that a[i] = v, then
f(m) = max_{v: a[d[v]] ^ m < a[m] ^ d[v] }( f(d[v] ) + 1
*/
#include <iostream>
using namespace std;
const int MAX_NUM = 300010, ARR_NUM = 201;
int arr[MAX_NUM], last_arr_idxs[ARR_NUM], max_lens[MAX_NUM];
int get_xor(int a, int b) {
    return (a & (~b)) | ((~a) & b);
}
int Max(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}
int main() {
    int t = 0;
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
        for (int i = 0; i < ARR_NUM; i++) {
            last_arr_idxs[i] = -1;
        }
        for (int i = 0; i < n; i++) {
            max_lens[i] = 1;
        }
        last_arr_idxs[arr[0]] = 0;
        for (int i = 1; i < n; i++) {
            int num = arr[i];
            int _max = 1;
            for (int j = Max(0, i - 256); j < i; j++) {
                if (get_xor(arr[j], i) < get_xor(num, j)) {
                    if (max_lens[j] + 1 > _max) {
                        _max = max_lens[j] + 1;
                    }
                }
            }
            last_arr_idxs[num] = i;
            max_lens[i] = _max;
        }

        int total_max = 1;
        for (int i = 1; i < n; i++) {
            if (max_lens[i] > total_max) {
                total_max = max_lens[i];
            }
        }
        printf("%d\n", total_max);

    }
    return 0;
}