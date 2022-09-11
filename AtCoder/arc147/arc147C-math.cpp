/*
Solution: math
the ideal position of each people is the position nearest with the middle position!
the middle position is the middle point of N-th and N+1-th interval ends (totally 2N ends)
*/
#include <iostream>
#include <algorithm>
#define NMAX 300010
using namespace std;
int intervals[NMAX][2], flat[NMAX*2], results[NMAX];
int main() {
    int N, ai, bi;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d%d", &ai, &bi);
        intervals[i][0] = flat[i*2] = ai;
        intervals[i][1] = flat[i*2+1] = bi;
    }
    sort(flat, flat+N*2);
    int pivot = (flat[N] + flat[N-1]) / 2;
    int cnt_low = 0, cnt_eql = 0, cnt_high = 0;
    for (int i = 0; i < N; i++) {
        if (intervals[i][0] > pivot) {
            results[i] = intervals[i][0];
            cnt_high ++;
        } else if (intervals[i][1] <= pivot) {
            results[i] = intervals[i][1];
            cnt_low ++;
        } else {
            results[i] = pivot;
            cnt_eql ++;
        }
    }
    sort(results, results+N);
    long long _sum = 0ll;
    for (int i = 0; i < cnt_low; i++) {
        _sum += (long long)(pivot - results[i]) * (long long)(N - 1 - i * 2);
    }
    for (int i = 0; i < cnt_high; i++) {
        _sum += (long long)(results[N-1-i] - pivot) * (long long)(N - 1 - i * 2);
    }
    printf("%lld\n", _sum);
    return 0;
}