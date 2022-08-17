/*
Solution can be found at P1198.py
*/

#include <iostream>
using namespace std;
const int N = 200010;
long long stacks[N];
int idxs[N], size = 0;
int binary_search(int num) {
    int low = 0, high = size - 1;
    while (true) {
        if (low >= high) {
            if (idxs[low] >= num) {
                return low;
            } else {
                return low + 1;
            }
        }
        int mid = (low + high) / 2;
        if (idxs[mid] < num) {
            low = mid + 1;
        } else if (idxs[mid] > num) {
            high = mid - 1;
        } else {
            return mid;
        }
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int M;
    long long D;
    scanf("%d %lld\n", &M, &D);

    int idx_now = 0;
    long long t = 0ll;
    for (int i = 0; i < M; i++) {
        char oper;
        long long n;
        scanf("%c %lld\n", &oper, &n);
        if (oper == 'A') {
            
            long long val = (t + n) % D;
            while (true) {
                if (size == 0) { break; }
                if (stacks[size - 1] > val) { break; }
                size--;
            }
            stacks[size] = val;
            idxs[size] = idx_now;
            size++;
            idx_now++;
        } else if (oper == 'Q') {
            int idx_use = binary_search(idx_now - int(n));
            printf("%lld\n", stacks[idx_use]);
            t = stacks[idx_use];
        } else {
            continue;
        }
    }


    return 0;
}