/*
Solution: bruteforce enumeration
two kinds of emueration:
(1) words permutation, that is N!;
(2) position of "_", that is C(T-\sum_{S_i}+N-2, N-2), where C(m, n) is combination number;
note that N! * C(T-\sum_{S_i}+N-2, N-2) <= N! * C(T-2, N-2) <= N! * C(14, N-2)
<= 8! * C(14, 6) (this is N <= 8) = 14 * 13 * 12 * 11 * 10 * 9 = 2162160, solveable!
thus, we can just store all valid string, then use O(M * 1) to query.
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#define INF (2147483647)
#define SMAX 8
using namespace std;
string templates[SMAX];
int perms[SMAX], cache[SMAX], status[SMAX], xiahuacnts[SMAX];
const int LMIN = 3, LMAX = 16;
string sp = "_______________________";
bool nextPerm(int N) {
    int c = N-2;
    while (c >= 0) {
        if (perms[c] < perms[c + 1]) {
            break;
        }
        c --;
    }
    if (c == -1) {
        return false;
    }
    int biggeridx = N-1;
    while (perms[c] > perms[biggeridx]) {
        biggeridx --;
    }
    int temp = perms[c];
    perms[c] = perms[biggeridx];
    perms[biggeridx] = temp;
    for (int i = c+1; i < N; i++) {
        cache[i] = perms[i];
    }
    for (int i = c+1; i < N; i++) {
        perms[i] = cache[N-i+c];
    }
    return true;
}

bool nextStatus(int N, int MAXV) {
    int idx = N-1;
    while (idx >= 0) {
        if (status[idx] != MAXV) {
            break;
        }
        idx --;
    }
    if (idx == -1) { return false; }
    status[idx] ++;
    for (int i = idx+1; i < N; i++) {
        status[i] = status[idx];
    }
    return true;
}
int main() {
    int N, M;
    scanf("%d %d\n", &N, &M);
    int ssize = 0;
    for (int i = 0; i < N; i++) {
        getline(cin, templates[i]);
        // printf("%d: %s", i, templates[i].c_str());
        ssize += templates[i].size();
    }
    ssize += N - 1;
    for (int i = 0; i < N; i++) {
        perms[i] = i;
    }
    string s;
    set<string> constrs;
    for (int i = 0; i < M; i++) {
        getline(cin, s);
        constrs.insert(s);
    }

    if (N == 1) {
        if (constrs.find(templates[0]) != constrs.end() || templates[0].size() < LMIN) {
            printf("-1\n");
        } else {
            printf("%s\n", templates[0].c_str());
        }
    } else {
        int rm_size = LMAX - ssize; // insert free _
        bool hasFangan = false;
        while (true) {
            for (int rms = 0; rms <= rm_size; rms++) {
                for (int i = 0; i < rms; i++) {
                    status[i] = 0;
                }
                while (true) {
                    for (int i = 0; i < N-1; i++) {
                        xiahuacnts[i] = 1;
                    }
                    for (int i = 0; i < rms; i++) {
                        xiahuacnts[status[i]] ++;
                    }
                    string total = templates[perms[0]];
                    for (int i = 0; i < N-1; i++) {
                        total += sp.substr(0, xiahuacnts[i]);
                        total += templates[perms[i+1]];
                    }
                    if (constrs.find(total) == constrs.end()) {
                        printf("%s\n", total.c_str());
                        hasFangan = true;
                        break;
                    }
                    if (!nextStatus(rms, N-2)) { break; }
                }
                if (hasFangan) { break; }
            } 
            
            if (hasFangan) { break; }
            if (!nextPerm(N)) { break; }
        }

        if (!hasFangan) {
            printf("-1\n");
        }

    }


    return 0;
}