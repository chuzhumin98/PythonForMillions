/*
Solution: Binary Search + Prefix Sum
note that y(w) is a non-decreasing function, so we can use binary search to find the optimal w!
for each bin-search w0, we just need to save for two prefix sum [w >= w0] and [w >= w0] * v, then we can use O(1) to calculate for each interval's yi
in total, the complexity is O((m + n) * log W)
*/
#include <iostream>
#define INF (4611686018427387904ll)
using namespace std;
const int NMAX = 200010, MMAX = 200010;
int intervals[MMAX][2];
long long weights[NMAX], values[NMAX], prefix_sumWs[NMAX], prefix_sumVs[NMAX];
int main() {
    int n, m, li, ri;
    long long s, v, w;
    scanf("%d%d%lld", &n, &m, &s);
    for (int i = 1; i <= n; i ++) {
        scanf("%lld%lld", &w, &v);
        weights[i] = w;
        values[i] = v;
    }
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &li, &ri);
        intervals[i][0] = li;
        intervals[i][1] = ri;
    }
    
    int low = 0, high = 1000001;
    long long min_delta = INF;
    while (true) {
        int weight = (low + high) / 2;
        long long weightl = (long long)weight;
        prefix_sumWs[0] = 0ll;
        prefix_sumVs[0] = 0ll;
        for (int i = 1; i <= n; i++) {
            prefix_sumWs[i] = prefix_sumWs[i-1];
            prefix_sumVs[i] = prefix_sumVs[i-1];
            if (weights[i] >= weightl) {
                prefix_sumWs[i] += 1ll;
                prefix_sumVs[i] += values[i];
            }
        }
        long long _sum = 0ll;
        for (int i = 0; i < m; i++) {
            li = intervals[i][0]; ri = intervals[i][1];
            _sum += (prefix_sumWs[ri] - prefix_sumWs[li-1]) * (prefix_sumVs[ri] - prefix_sumVs[li-1]);
        }
        if (_sum >= s) {
            low = weight + 1;
        } else {
            high = weight - 1;
        }
        min_delta = min(min_delta, abs(_sum - s));
        if (high < low) {
            break;
        }
    }
    printf("%lld\n", min_delta);

    return 0;
}