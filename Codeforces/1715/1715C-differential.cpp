/*
Solution: differential
note that if a[i] = a[i+1] (index from 0 to n-1), then compared with a[i] != a[i+1], we need to decrease
the sum of awesomeness with (i + 1) * (n - i - 1), where i + 1 is the left end select num, n - i - 1 is the
right end select num;
so when we modify a[k] from s to t, we just need to check if a[k-1] = s or t, a[k+1] = s or t,
then add or minus the corresponding delta, to gain the lastest sum
*/

#include <iostream>
#define ll (long long)
using namespace std;
const int NMAX = 100010;
int arr[NMAX];
void init_array_fromscanf(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
}
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    init_array_fromscanf(arr, n);
    long long init_value = 0;
    for (int i = 1; i <= n; i++) {
        init_value += ll(i) * ll(n+1-i);
    }
    for (int i = 0; i < n-1; i++) {
        if (arr[i] == arr[i+1]) {
            init_value -= ll(i+1) * ll(n - i - 1);
        }
    }

    for (int _ = 0; _ < m; _++) {
        int i, x;
        scanf("%d%d", &i, &x);
        i--;
        if (x == arr[i]) {
            printf("%lld\n", init_value);
        } else {
            if (i > 0) {
                if (arr[i-1] == arr[i]) {
                    init_value += ll(i) * ll(n-i);
                } else if (arr[i-1] == x) {
                    init_value -= ll(i) * ll(n-i);
                }
            }
            if (i < n-1) {
                if (arr[i+1] == arr[i]) {
                    init_value += ll(i+1) * ll(n-1-i);
                } else if (arr[i+1] == x) {
                    init_value -= ll(i+1) * ll(n-1-i);
                }
            }
            printf("%lld\n", init_value);
            arr[i] = x;
        }
    }


    return 0;
}