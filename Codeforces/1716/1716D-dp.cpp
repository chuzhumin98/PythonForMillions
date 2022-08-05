/*
Solution: dp
The same idea with 1716D.py, to see it in that file
*/

#include <iostream>
using namespace std;
int main() {
    int P = 998244353;
    int n, k;
    cin >> n >> k;
    int* fs = new int [n+1];
    int* fs_last = new int [n+1];
    int* fs_current = new int [n+1];
    for (int i = 0; i <= n; i++) {
        fs[i] = 0;
        fs_current[i] = 0;
        fs_last[i] = 0;
    }
    fs_last[0] = 1;

    int cnt = k;
    int _min_value = 0;
    while (true) {
        for (int i = _min_value+cnt; i <= n; i++) {
            fs_current[i] = (fs_last[i - cnt] + fs_current[i - cnt]) % P;
            fs[i] = (fs[i] + fs_current[i]) % P;
        }
        _min_value += cnt;
        cnt++;
        if (_min_value + cnt > n) {
            break;
        }

        
        for (int i = 0; i <= n; i++) {
            fs_last[i] = fs_current[i];
            fs_current[i] = 0;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << fs[i] << " ";
    }
    cout << endl;
    return 0;
}