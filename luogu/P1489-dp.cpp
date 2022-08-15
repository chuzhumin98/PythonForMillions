/*
Solution: find in P1489.py code
*/

#include <iostream>
using namespace std;
int Sum(int* a, int n) {
    int _sum = 0;
    for (int i = 0; i < n; i++) {
        _sum += a[i];
    }
    return _sum;
}
int Abs(int a) {
    if (a >= 0) {
        return a;
    } else {
        return -a;
    }
}
int main() {
    int n = 0;
    scanf("%d", &n);
    int* As = new int [n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &As[i]);
    }
    if (n == 1) {
        printf("0 %d\n", As[0]);
    } else {
        int select_num = n / 2;
        int total_sum = Sum(As, n);
    
        bool** fs = new bool* [select_num + 1];
        for (int i = 0; i <= select_num; i++) {
            fs[i] = new bool [total_sum + 1];
            for (int j = 0; j <= total_sum; j++) {
                fs[i][j] = false;
            }
        }
        fs[0][0] = true;
        for (int i = 0; i < n; i++) {
            int ai = As[i];
            for (int k = select_num; k > 0; k--) {
                for (int _sum = total_sum; _sum >= ai; _sum--) {
                    fs[k][_sum] = fs[k][_sum] || fs[k-1][_sum - ai];
                }
            }
        }

        int delta_min = 1 << 30;
        int sum_min = 0;
        for (int i = 0; i <= total_sum; i++) {
            if (fs[select_num][i]) {
                int abs_delta = Abs(2 * i - total_sum);
                if (abs_delta < delta_min) {
                    delta_min = abs_delta;
                    sum_min = i;
                }
            }
        }

        printf("%d %d\n", sum_min, total_sum - sum_min);




        delete []As;
        for (int i = 0; i <= select_num; i++) {
            delete []fs[i];
        }
        delete []fs;
    }
    return 0;
}