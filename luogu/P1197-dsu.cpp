#include <iostream>
#include <vector>
using namespace std;
const int NMAX = 400010;
vector<int> edges[NMAX], cuihuis;
bool huifu[NMAX];
int unionset[NMAX];
int get_parent(int node) {
    if (unionset[node] == node) {
        return node;
    } else {
        int par = unionset[node];
        int root = get_parent(par);
        unionset[node] = root;
        return root;
    }
}
bool merge(int nA, int nB) {
    int parA = get_parent(nA), parB = get_parent(nB);
    if (parA != parB) {
        unionset[parB] = parA;
        return true;
    } else {
        return false;
    }
}
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    int x, y;
    for (int i = 0; i < m; i ++) {
        scanf("%d%d", &x, &y);
        edges[x].push_back(y);
        edges[y].push_back(x);
    }
    int k = 0;
    scanf("%d", &k);
    for (int i = 0; i < n; i++) {
        huifu[i] = true;
    }
    int c;
    for (int i = 0; i < k; i++) {
        scanf("%d", &c);
        cuihuis.push_back(c);
        huifu[c] = false;
    }

    for (int i = 0; i < n; i++) {
        unionset[i] = i;
    }
    int cnt_lian = n;
    for (int node = 0; node < n; node++) {
        if (huifu[node]) {
            for (int i = 0; i < edges[node].size(); i++) {
                int nodeN = edges[node][i];
                if (huifu[nodeN]) {
                    if (merge(node, nodeN)) {
                        cnt_lian --;
                    }
                }
            }
        }
    }

    cnt_lian -= k;
    vector<int> results;
    results.push_back(cnt_lian);
    for (int i = k-1; i >= 0; i--) {
        int node = cuihuis[i];
        huifu[node] = true;

        cnt_lian ++;
        for (int j = 0; j < edges[node].size(); j++) {
            int nodeN = edges[node][j];
            if (huifu[nodeN]) {
                if (merge(node, nodeN)) {
                    cnt_lian --;
                }
            }
        }

        results.push_back(cnt_lian);
    }

    for (int i = results.size()-1; i >= 0; i--){
        printf("%d\n", results[i]);
    }

    return 0;
}