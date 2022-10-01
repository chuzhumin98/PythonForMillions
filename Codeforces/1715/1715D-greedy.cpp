/*
Solution: greedy
note that for a_i | a_j = x, when we consider it into each bit, we can get two kinds of constraints:
(1) a_i(k) | a_j(k) = 0 where a_i(k) denote the (1 << k) bit of a_i, then a_i(k) = a_j(k) = 0;
(2) a_i(k) | a_j(k) = 1, then a_i(k) and a_j(k) need at least one 1
we use greedy stategy to solve this problem, when we first scan the constraints, we can make each (1) type constraints to determine each a_i(k) = 0;
then we just need to consider (2) type, we consider the number from i: 0 -> n-1, if any constraint linked with i and another node j of type (2) in bit k, and a_j(k) has required to be 0, then set a_i(k) = 1, otherwise set it to be 0
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int NMAX = 100010, BMAX = 30;
vector<int> links[NMAX][BMAX];

int main() {
    // ios::sync_with_stdio(0);
    // cin.tie(0);
    int n, q;
    scanf("%d%d", &n, &q);
    int** bitss = new int* [n];
    for (int i = 0; i < n; i++) {
        bitss[i] = new int [BMAX];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < BMAX; j++) {
            bitss[i][j] = -1;
        }
    }
    
    for (int _ = 0; _ < q; _++) {
        int i, j, x;
        scanf("%d%d%d", &i, &j, &x);
        i--, j--;
        if (i == j) {
            for (int k = 0; k < BMAX; k++) {
                bitss[i][k] = x % 2;
                x /= 2;
            }
            continue;
        }

        for (int k = 0; k < BMAX; k++) {
            int bit_this = x % 2;
            if (bit_this == 0) {
                bitss[i][k] = bitss[j][k] = 0;
            } else {
                links[i][k].push_back(j);
                links[j][k].push_back(i);
            }
            x /= 2;
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < BMAX; j++) {
            bool can_zero = true;
            if (bitss[i][j] == -1) {
                for (int k = 0; k < links[i][j].size(); k++) {
                    if (bitss[links[i][j][k]][j] == 0) {
                        can_zero = false;
                        break;
                    }
                }
                if (can_zero) {
                    bitss[i][j] = 0;
                } else {
                    bitss[i][j] = 1;
                }
            }
        }
    }

    int bases[BMAX];
    bases[0] = 1;
    for (int i = 1; i < BMAX; i++) {
        bases[i] = bases[i-1] * 2;
    }
    for (int i = 0; i < n; i++) {
        int num = 0;
        for (int j = 0; j < BMAX; j++) {
            if (bitss[i][j] == 1) {
                num += bases[j];
            }
        }
        printf("%d ", num);

    }
    printf("\n");



    // for (int i = 0; i < itvs.size(); i++) {
    //     printf("%d, %d: %d\n", itvs[i].left, itvs[i].right, itvs[i].bit_idx);
    // }

    return 0;
}