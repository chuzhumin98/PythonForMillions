/*
Solution: Priority Queue
note that after each time, the min value is A_i % A_j or A_j (if A_i % A_j = 0),
so we no need to auxiliary check the min value each time
Thus, we only need to hold with a max pq, to find the max value each time,
then we just need to simulate this step each time
*/
#include <iostream>
#include <queue>
#include <vector>
#define NMAX 200010
#define INF (2147483647)
using namespace std;
int main() {
    int N, ai;
    priority_queue<int, vector<int>, less<int> > pq;
    scanf("%d", &N);
    int minv = INF;
    for (int i = 0; i < N; i++) {
        scanf("%d", &ai);
        pq.push(ai);
        minv = min(minv, ai);
    }

    int cnt = 0;
    while (pq.size() > 1) {
        cnt++;
        int num = pq.top(); pq.pop();
        int mod = num % minv;
        if (mod > 0) {
            pq.push(mod); minv = mod;
        }
    }
    printf("%d\n", cnt);

    

    return 0;
}