/*
Solution: find in 1709D.py code
*/

#include <iostream>
using namespace std;
int Abs(int a) {
    if (a >= 0) {
        return a;
    } else {
        return -a;
    }
}
int Max(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}
int get_rmq(int low, int high, int** rmqs, int* log_ns, int* exp2s_list) {
    int logn = log_ns[high - low + 1];
    int max_height = Max(rmqs[low][logn], rmqs[high-exp2s_list[logn]+1][logn]);
    return max_height;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n = 0, m = 0;
    cin >> n >> m;
    int* Ass = new int [m];
    for (int i = 0; i < m; i++) {
        cin >> Ass[i];
    }

    int* log_ns = new int [m+1];
    log_ns[0] = 0;
    log_ns[1] = 0;
    for (int i = 2; i <= m; i++) {
        log_ns[i] = log_ns[i / 2] + 1;
    }

    

    int R = log_ns[m] + 1;
    int* exp2s_list = new int [R];
    exp2s_list[0] = 1;
    for (int i = 1; i < R; i++) {
        exp2s_list[i] = exp2s_list[i-1] * 2;
    }


    int** rmqs = new int* [m];
    for (int i = 0; i < m; i++) {
        rmqs[i] = new int [R];
    }

    for (int i = 0; i < m; i++) {
        rmqs[i][0] = Ass[i];
    }
    for (int j = 1; j < R; j++) {
        for (int i = 0; i < m; i++) {
            rmqs[i][j] = rmqs[i][j-1];
            int idx_new = i + exp2s_list[j-1];
            if (idx_new < m) {
                if (rmqs[idx_new][j-1] > rmqs[i][j])
                    rmqs[i][j] = rmqs[idx_new][j-1];
            }
        }
    }


    int q = 0;
    cin >> q;
    for (int _ = 0; _ < q; _++) {
        int xs, ys, xt, yt, K;
        cin >> xs >> ys >> xt >> yt >> K;
        ys--;
        yt--;

        int deltaX = Abs(xs - xt);
        int deltaY = Abs(ys - yt);

        if (deltaX % K == 0 && deltaY % K == 0) {
            int ylow = ys, yhigh = yt;
            if (ys > yt) {
                ylow = yt;
                yhigh = ys;
            }
            int max_height = get_rmq(ylow, yhigh, rmqs, log_ns, exp2s_list);
            if (max_height < xs) {
                cout << "YES" << endl;
            } else if ((n - xs) / K <= (max_height - xs) / K) {
                cout << "NO" << endl;
            } else {
                cout << "YES" << endl;
            }

        } else {
            cout << "NO" << endl;
        }

    }

    for (int i = 0; i < m; i++){
        delete []rmqs[i];
    }
    delete []rmqs;
    delete []Ass;
    delete []log_ns;
    delete []exp2s_list;

    return 0;
}