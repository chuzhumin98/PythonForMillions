/*
Solution: ST Table + Double Pointer
we first use O(n*log n) complexity to hold for a ST table (then each range min query operation is O(1))
then we use double pointer to hold for the just invalid interval [l, r], i.e. rmq(l, r) > p and rmq(l-1, r) <= p, then the valid selection number with right idx = r is the number of the i \in [0, l) which satisfies b[i] == b[r], this step is O(n*k) complexity
so totally complexity is O(n * log n + n * k)
*/

#include <iostream>
using namespace std;
const int NMAX = 200010, NLOGMAX = 19;
int As[NMAX], Bs[NMAX], st_table[NMAX][NLOGMAX], logsn[NMAX], mis2[NLOGMAX];
void init_st_table(int n) {
    mis2[0] = 1;
    for (int i = 1; i < NLOGMAX; i++) {
        mis2[i] = mis2[i-1] * 2;
    }
    logsn[1] = 0;
    for (int i = 2; i <= n; i++) {
        logsn[i] = logsn[i / 2] + 1;
    }
    for (int i = 0; i < n; i++) {
        st_table[i][0] = Bs[i];
    }
    int logn_used = logsn[n] + 1;
    for (int j = 1; j < logn_used; j++) {
        for (int i = 0; i < n; i++) {
            st_table[i][j] = st_table[i][j-1];
            int idx_add = i + mis2[j-1];
            if (idx_add < n) {
                st_table[i][j] = min(st_table[i][j], st_table[idx_add][j-1]);
            }
        }
    }
}

int get_rmq(int low, int high) {
    int logn_this = logsn[high - low + 1];
    return min(st_table[low][logn_this], st_table[high-mis2[logn_this]+1][logn_this]);
}

int main() {
    
    int n, k, p;
    scanf("%d%d%d", &n, &k, &p);
    int ai, bi;
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &As[i], &Bs[i]);
    }
    init_st_table(n);
    int logn_used = logsn[n] + 1;
    long long _sum = 0ll;
    for (int c = 0; c < k; c++) { // for each color
        int left_idx = 0, cur_leftC = 0;
        for (int i = 0; i < n; i++) {
            if (As[i] == c) {
                while (true) {
                    if (left_idx == i) { break; }
                    if (get_rmq(left_idx, i) > p) { break; }
                    if (As[left_idx] == c) {
                        cur_leftC ++;
                    }
                    left_idx++;
                }
                _sum += (long long)(cur_leftC);
            }
        }
    }
    printf("%lld\n", _sum);

    return 0;
}