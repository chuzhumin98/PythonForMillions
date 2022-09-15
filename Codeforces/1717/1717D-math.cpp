/*
Solution: math, combinatorics
the min value is the number of player can win with no less than k swap operation
we no matter suppose the win one of the original arrangement is l-l-l-l-...-l player (l: left, r: right)
one swap: l-l-r-l-...-l-l sequence with one r, C(n, 1),
k swap (k <= n), sequence with at most k times r, C(n, k)
thus, the result is \sum_{i <= min(k, n)} C(n, i)
then, we can use the inverse element to quickly calculate C(m, n)
*/
#include <iostream>
#define P (1000000007ll)
#define NMAX 100010
using namespace std;
long long sucimi(long long n, long long p) { // n ^ p
    long long res = 1ll;
    long long nmi = n;
    while (p > 0) {
        if (p % 2 == 1) {
            res = (res * nmi) % P;
        }
        p /= 2;
        nmi = (nmi * nmi) % P;
    }
    return res;
}
int main() {
    long long n, k;
    scanf("%lld%lld", &n, &k);
    long long jiechengs[NMAX], niyuan[NMAX];
    jiechengs[0] = 1ll;
    for (long long i = 1ll; i <= n; i++) {
        jiechengs[i] = (jiechengs[i-1] * i) % P;
    }
    long long mi = P - 2ll;
    for (int i = 0; i <= n; i++) {
        niyuan[i] = sucimi(jiechengs[i], mi);
    }
    long long ans = 0ll;
    for (int i = 0; i <= min(n, k); i++) {
        long long delta = (jiechengs[n] * niyuan[i]) % P;
        delta = (delta * niyuan[n-i]) % P;
        ans = (ans + delta) % P;
    }
    printf("%lld\n", ans);

    return 0;
}