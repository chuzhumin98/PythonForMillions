/*
Solution:
first we need to confirm that for all k, if a_k <= b_k satisfies, if not, directly print "No"
Then, we need to find for a_k where a_k = max(a),
(1) if a_k = b_k, then we can add from idx k-1, k-2, ..., k+2, k+1, to check each position can add from a[i] to b[i];
(2) if a_k < b_k, then a_k also need to increase, then we reversely consider it, from idx k+1, k+2, ..., k-2, k-1, to check
if the right one can support the left one to become that height, respectively
*/
#include <iostream>
#define NMAX 200010
using namespace std;
int As[NMAX], Bs[NMAX];
int arg_max(int a[], int n) {
    int midx = 0, mval = a[0];
    for (int i = 1; i < n; i++) {
        if (mval < a[i]) {
            mval = a[i]; midx = i;
        }
    }
    return midx;
}
int main() {
    int t;
    scanf("%d", &t);
    for (int _ = 0; _ < t; _ ++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &As[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &Bs[i]);
        }
        bool is_can = true;
        for (int i = 0; i < n; i++) {
            if (As[i] > Bs[i]) {
                is_can = false;
                break;
            }
        }
        if (!is_can) {
            printf("NO\n");
        } else {
            int maxai = arg_max(As, n);
            if (As[maxai] == Bs[maxai]) {
                for (int i = 0; i < n-1; i++) {
                    int lidx = (maxai-i-1+n) % n;
                    if (Bs[(maxai-i+n)%n] + 1 < Bs[lidx] && As[lidx] != Bs[lidx]) {
                        is_can = false;
                        break;
                    }
                }
            } else {
                int maxbi = arg_max(Bs, n);
                for (int i = 0; i < n-1; i++) {
                    int lidx = (maxbi + i) % n;
                    if (Bs[lidx] - 1 > Bs[(maxbi + i + 1) % n] && Bs[lidx] != As[lidx]) {
                        is_can = false;
                        break;
                    }
                }
            }
            if (is_can) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }

    return 0;
}