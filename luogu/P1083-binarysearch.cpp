/*
Solution can be find in P1083.py, note that you need to store the classroom num by long long rather than int!
*/

#include <iostream>
using namespace std;
struct Order{
    int start, end;
    long long num;
    void set_value(long long n, int s, int e) {
        this->num = n;
        this->start = s;
        this->end = e;
    }
};
bool check(long long* arr, Order** orders, int k, int n, int m) { // check [0, k] is possible?
    long long* deltas = new long long [n+1];
    for (int i = 0; i <= n; i++) {
        deltas[i] = 0ll;
    }
    for (int i = 0; i <= k; i++) {
        deltas[orders[i]->start] += orders[i]->num;
        deltas[orders[i]->end + 1] -= orders[i]->num;
    }
    long long _sum = 0;
    for (int i = 0; i < n; i++) {
        _sum += deltas[i];
        if (_sum > arr[i]) {
            delete []deltas;
            return false;
        }
    }
    delete []deltas;
    return true;
}

int binary_search(long long* arr, Order** orders, int low, int high, int n, int m) {
    if (low >= high) {
        if (check(arr, orders, low, n, m)) {
            return low + 1;
        } else {
            return low;
        }
    }
    int mid = (low + high) >> 1;
    if (check(arr, orders, mid, n, m)) {
        return binary_search(arr, orders, mid+1, high, n, m);
    } else {
        return binary_search(arr, orders, low, mid-1, n, m);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    scanf("%d%d", &n, &m);
    long long* arr = new long long [n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &arr[i]);
    }
    Order** orders = new Order* [m];
    int s, e;
    long long d;
    for (int i = 0; i < m; i++) {
        orders[i] = new Order();
        scanf("%lld%d%d", &d, &s, &e);
        orders[i]->set_value(d, s-1, e-1);
    }

    int order_select = binary_search(arr, orders, 0, m-1, n, m);
    if (order_select == m) {
        printf("0\n");
    } else {
        printf("-1\n%d\n", order_select + 1);
    }





    delete []orders;
    delete []arr;
    return 0;
}