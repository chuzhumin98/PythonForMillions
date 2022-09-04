/*
Solution: dp
consider two dumb value 0...0 in the leftmost and rightmost of permutation, we sort all the values of A_i in incresing order
for example: 0 1 2 1 3 3 1 0, for the next 3, it has 7 alteratives to insert, if in the existing order a_i < a_i+1, insert
the new value between them donot change the a_i < a_i+1 number (3 alters in example); if in the existing order a_i >= a_i+1 and
new value v > a_i, then insert v between them can add 1 a_i < a_i+1 condition (7-3-2 = 2 alters), -2 is the v = a_i conditions, so we can
get that:
let f(n, k) be k a_i < a_i+1 condition when we already set n values in the 0..0 array, then
f(n, k) = (k + {a_i = v_n}) * f(n-1, k) + (n - (k-1) - {a_i = v_n}) * f(n-1, k-1)
Finally, f(N, K+1) is the result we need
*/

#include <iostream>
#define P (998244353ll)
#define NMAX 5010
using namespace std;
long long niyuan[NMAX];
int backet[NMAX];
long long fs_pred[NMAX], fs[NMAX];
long long sucimi(long long n, int k) {
    long long res = 1ll;
    long long mi = n;
    while (k > 0) {
        if (k % 2) {
            res = (res * mi) % P;
        }
        mi = (mi * mi) % P;
        k /= 2;
    }
    return res;
}
int main() {
    int N, K, ai;
    scanf("%d%d", &N, &K);
    for (int i = 1; i <= N; i++) {
        backet[i] = 0;
    }
    for (int i = 0; i < N; i++) {
        scanf("%d", &ai);
        backet[ai] ++;
    }
    for (int i = 1; i <= N; i++) {
        niyuan[i] = sucimi((long long)i, P-2);
    }

    for (int i = 1; i <= K+1; i++) {
        fs_pred[i] = 0ll;
    }
    fs_pred[0] = 1ll;
    for (int i = 0; i <= K+1; i++) {
        fs[i] = 0ll;
    }
    int total_posi = 0;
    for (int i = 1; i <= N; i++) {
        if (backet[i] > 0) {
            for (int j = 1; j <= backet[i]; j++) {
                total_posi ++;
                for (int l = 0; l <= K+1; l++) {
                    // fs[l] += (((fs_pred[l] * (long long)(l + j - 1)) % P) * niyuan[j]) % P;
                    // fs[l+1] += (((fs_pred[l] * (long long)(total_posi - l - j + 1)) % P) * niyuan[j]) % P;
                    fs[l] += (fs_pred[l] * (long long)(l + j - 1)) % P;
                    fs[l+1] += (fs_pred[l] * (long long)(total_posi - l - j + 1)) % P;
                }
                // printf("the %d-th num %d:\n", j, i);
                for (int l = 0; l <= K+1; l++) {
                    // printf("%lld ", fs[l]);
                    fs_pred[l] = fs[l] % P;
                    fs[l] = 0ll;
                }
                // printf("\n\n");
            }
        }
    }
    printf("%lld\n", fs_pred[K+1]);

    return 0;
}