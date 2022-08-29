/*
Solution: graph + Dijkstra Algorithm
to get the min path of 0 to k, we just need to conduct Dijkstra algorithm,
as for the min path strategies number, we need to store for this info,
for each value = min value, add the strategies number coming from different vertex, i.e. N(k) = \sum_i N(i), where {i}-set all come with the same min path value
!!!CAUTION!!! Note that problem doesn't confirm that the edge from i to j is unique, so we need to unique it with ourselves!
*/
#include <iostream>
#include <vector>
#include <queue>
#define NMAX 2010
#define INF (32767)
using namespace std;
struct EdgeInfo{
    int out_ver, in_ver;
    short in_dist;
    EdgeInfo(int o, int v, short d) {
        this->out_ver = o; this->in_ver = v; this->in_dist = d;
    }
    friend bool operator<(const EdgeInfo &a,const EdgeInfo &b) { return a.in_dist > b.in_dist; }
};
vector<int> edges[NMAX];
vector<short> dists[NMAX];
int _cnts[NMAX]; // 0 to i path's min dist && the min dist's method number
short min_values[NMAX];
short quchong[NMAX][NMAX];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, E, I, J;
    short C;
    
    scanf("%d%d", &N, &E);
    for (int i = 0; i < N; i++) {
        min_values[i] = INF;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            quchong[i][j] = 11;
        }
    }
    for (int i = 0; i < E; i++) {
        scanf("%d%d%hd", &I, &J, &C);
        I--; J--;  
        if (quchong[I][J] > C) {
            edges[I].push_back(J);
            dists[I].push_back(C);
            quchong[I][J] = C;
        }
    }
    priority_queue<EdgeInfo> pq;
    pq.push(EdgeInfo(N, 0, 0)); _cnts[N] = 1;
    EdgeInfo ei(0, 0, 0);
    int o, v;
    short d;
    while (true) {
        if (pq.size() == 0) { break; }
        ei = pq.top(); pq.pop();
        o = ei.out_ver; v = ei.in_ver; d = ei.in_dist;
        // if (min_values[v] < INF) { continue; }
        if (d > min_values[N-1]) { break; }

        bool need_expand = true;
        if (d < min_values[v]) {
            min_values[v] = d; _cnts[v] = _cnts[o];
        } else if (d == min_values[v]) {
            _cnts[v] += _cnts[o];
            need_expand = false;
        }
        // printf("v = %d, o = %d, min_value = %d, cnt = %d\n", v, o, min_values[v], _cnts[v]);

        if (need_expand) {
            for (int i = 0; i < edges[v].size(); i++) {
                if (min_values[edges[v][i]] == INF)
                    pq.push(EdgeInfo(v, edges[v][i], dists[v][i] + d));                   
                    // printf("%d -> %d: dist = %d\n", v, edges[v][i], dists[v][i] + d);
            }
        } 
    }
    if (min_values[N-1] < INF) {
        printf("%hd %d\n", min_values[N-1], _cnts[N-1]);
    } else {
        printf("No answer");
    }
    return 0;
}