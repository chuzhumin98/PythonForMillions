/*
Solution: differential
we just to consider the two-degree differential function of the frustration sum
when the dish turns with counterclockwise, for each person-dish pair, the frustration changes with +1, -1 or 0 (only when odd number could occur 0), the
change point is dish t sets on position t (-1 -> +1), 
even condition: position t + n/2 (+1 -> -1);
odd condition: position t + (n-1)/2 (+1 -> 0), position t + (n+1)/2 (0 -> -1);
that is two-degree differential, using it we can get differential number, 
so as to current frustration sum.
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#define INF (2147483647)
#define NMAX 200010
using namespace std;
int changes[NMAX];
int main() {
    
    int N, num, _delta0 = 0;
    long long _sum = 0ll;
    scanf("%d", &N);
    for (int i = 0; i < N; i++ ) {
        changes[i] = 0;
    }
    for (int i = 0; i < N; i++) {
        scanf("%d", &num);
        int d = (i + N - num) % N; // after it -1 -> 1
        // printf("d = %d\n", d);
        changes[d] += 2;
        if (N % 2 == 0) {
            int dmax = (d + N/2) % N;
            changes[dmax] += -2; // 1 -> -1
            if (d < dmax) {
                _delta0 += -1;
            } else {
                _delta0 += 1;
            }
        } else {
            int dmax1 = (d + N/2) % N;
            int dmax2 = (dmax1 + 1) % N;
            if (dmax1 > dmax2) {
                int temp = dmax1;
                dmax1 = dmax2;
                dmax2 = temp;
            }
            changes[dmax1]--; // 1 -> 0
            changes[dmax2]--; // 0 -> -1
            if (dmax1 < d && dmax2 < d) {
                _delta0 += 1;
            } else if (dmax1 > d && dmax2 > d) {
                _delta0 += -1;
            } else {
                _delta0 += 0;
            }
        }
        _sum += (long long)min((i - num + N) % N, (num + N - i) % N);  
    }
    // printf("_sum = %d, _delta0 = %d\n", _sum, _delta0);
    // for (int i = 0; i < N; i++) {
    //     printf("%d ", changes[i]);
    // }
    // printf("\n");
    long long minv = _sum;
    for (int i = 0; i < N; i++) { 
        _delta0 += changes[i];     
        _sum += (long long)_delta0;
        minv = min(minv, _sum); 
    }
    printf("%lld\n", minv);
    return 0;
}