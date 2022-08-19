/*
Solution: graph + dfs + greedy
We split the problem into 2 symetry subproblem: 
for each node i, what is the minimum buying value from the node that in the path of start to node i? what is the maximum selling value from the node that in the path of node i to end?
To consider the first problem (second is similar), we can first use dfs/bfs to find the node can be arrived from start, then we sort them with the value in increasing order (bucket sort), O(n) complexity,
then we greedly spread the node of min value to the node they can arrived, that is the smallest value they can buy from the path start to this point.
Then, with the two solved subproblem, we can calculate the max delta value to obtain the results.
*/
#include <iostream>
#include <vector>
#define INF 10000000
#define MINF -10000000
using namespace std;
const int NMAX = 100010, VMAX = 100;
vector<int> boxes[VMAX], out_matrix[NMAX], in_matrix[NMAX];
int values[NMAX], min_start2this[NMAX], max_this2end[NMAX], stack[NMAX], sizeS = 0;
bool arrived[NMAX];
void init_array(int arr[], int n, int value) {
    for (int i = 0; i < n; i++) {
        arr[i] = value;
    }
}

void init_array_fromscanf(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
}

void dfs(int s, vector<int> matrix[], int n) {
    for (int i = 0; i < n; i++) {
        arrived[i] = false;
    }
    stack[sizeS++] = s;
    arrived[s] = true;
    while (true) {
        if (sizeS == 0) { break; }
        int node = stack[--sizeS];
        for (int i = 0; i < matrix[node].size(); i++) {
            int nodeN = matrix[node][i];
            if (!arrived[nodeN]) {
                arrived[nodeN] = true;
                stack[sizeS++] = nodeN;
            }
        }
    }
    // sizeS = 0; // clear the stack
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    init_array_fromscanf(values, n);
    init_array(min_start2this, n, INF);
    init_array(max_this2end, n, MINF);
    for (int i = 0; i < m; i++) {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        x--, y--;
        out_matrix[x].push_back(y);
        in_matrix[y].push_back(x);
        if (z == 2) {
            out_matrix[y].push_back(x);
            in_matrix[x].push_back(y);
        }
    }

    // box sort
    for (int i = 0; i < n; i++) {
        boxes[values[i] - 1].push_back(i);
    }

    dfs(0, out_matrix, n); // dfs from start point
    // find the min from start to this point
    for (int v = 0; v < VMAX; v++) {
        for (int j = 0; j < boxes[v].size(); j++) {
            int node = boxes[v][j];
            if (arrived[node]) { // only consider the arriveable node
                // set all the unvisit node to min value v
                stack[sizeS++] = node;
                arrived[node] = false;
                min_start2this[node] = v;
                while (true) {
                    if (sizeS == 0) { break; }
                    int nodeN = stack[--sizeS];
                    for (int k = 0; k < out_matrix[nodeN].size(); k++) {
                        int nodeNN = out_matrix[nodeN][k];
                        if (arrived[nodeNN]) {
                            stack[sizeS++] = nodeNN;
                            arrived[nodeNN] = false;
                            min_start2this[nodeNN] = v;
                        }
                    }
                }
            }
        } 
    }

    dfs(n-1, in_matrix, n); // dfs from end point
    // find the max from this point to end
    for (int v = VMAX - 1; v >= 0; v--) {
        for (int j = 0; j < boxes[v].size(); j++) {
            int node = boxes[v][j];
            if (arrived[node]) { // only consider the arriveable node
                // set all the unvisit node to min value v
                stack[sizeS++] = node;
                arrived[node] = false;
                max_this2end[node] = v;
                while (true) {
                    if (sizeS == 0) { break; }
                    int nodeN = stack[--sizeS];
                    for (int k = 0; k < in_matrix[nodeN].size(); k++) {
                        int nodeNN = in_matrix[nodeN][k];
                        if (arrived[nodeNN]) {
                            stack[sizeS++] = nodeNN;
                            arrived[nodeNN] = false;
                            max_this2end[nodeNN] = v;
                        }
                    }
                }
            }
        } 
    }

    int max_delta = 0;
    for (int i = 0; i < n; i++) {
        max_delta = max(max_delta, max_this2end[i] - min_start2this[i]);
    }    
    printf("%d\n", max_delta);

    return 0;
}