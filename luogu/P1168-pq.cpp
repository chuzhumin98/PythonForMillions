/*
Solution: see in P1168.python
*/

#include <iostream>
#include <queue>
using namespace std;
struct cmp_small{
    bool operator ()(int a,int b){
        return a>b;    //最小值优先
    }
};
struct cmp_large{
    bool operator ()(int a,int b){
        return a<b;    //最大值优先
    }
};
const int NMAX = 100010;
int arr[NMAX];
int main() {
    priority_queue<int, vector<int>, cmp_small> pq_high;
    priority_queue<int, vector<int>, cmp_large> pq_low;

    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    if (N == 0) {
        return 0;
    } else if (N <= 2) {
        return arr[0];
    } else {
        pq_low.push(arr[0]);
        printf("%d\n", arr[0]);
        for (int i = 1; i < N; i++) {
            if (pq_low.top() >= arr[i]) {
                pq_low.push(arr[i]);
            } else {
                pq_high.push(arr[i]);
            }
            // note that pq_low.size() return value is unsigned long int type, so if you write pq_low.size() - pq_high.size() > 1, then it would error!!! as -1 is the maximum value!
            if (pq_low.size() > pq_high.size() + 1) {
                pq_high.push(pq_low.top());
                pq_low.pop();
            } else if (pq_high.size() > pq_low.size() + 1) {
                pq_low.push(pq_high.top());
                pq_high.pop();
            }

            if (i % 2 == 0) {
                if (pq_low.size() > pq_high.size()) {
                    printf("%d\n", pq_low.top());
                } else {
                    printf("%d\n", pq_high.top());
                }
            }
        }
        
    }

    return 0;
}