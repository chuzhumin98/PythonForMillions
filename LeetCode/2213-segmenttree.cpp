/*
Solution: Segment Tree
for each node, we hold for its satisfied prefix max length (prM), postfix max length (poM), total max length (tM)
then tM(node) = max( tM(lc), tM(rc), prM(node), poM(node), poM(lc)+prM(rc) if the neighbor of them is the same char )
*/
#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
#define N 100010
struct Node {
    int l, r, size;
    int maxlen, maxprefix, maxpostfix;
    Node() {
        l = r = size = maxlen = maxpostfix = maxprefix = 0;
    }
};

class Solution {
public:
    int data[N];
    Node tr[4 * N];
    int size;

    int max4(int a, int b, int c, int d) {
        int maxV = max(a, b);
        maxV = max(maxV, c);
        maxV = max(maxV, d);
        return maxV;
    }

    void build(int node, int l, int r)
    {
        tr[node].l = l; tr[node].r = r; tr[node].size = r - l + 1;
        if(l==r) {
            tr[node].maxlen = 1; tr[node].maxpostfix = 1; tr[node].maxprefix = 1;
        } else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            build(left_node,l,mid);
            build(right_node,mid+1,r);
            int l_lnode = tr[left_node].l, r_lnode = tr[left_node].r;
            int l_rnode = tr[right_node].l, r_rnode = tr[right_node].r;
            if (tr[left_node].maxprefix == tr[left_node].size && data[l_lnode] == data[l_rnode]) {
                tr[node].maxprefix = tr[left_node].maxprefix + tr[right_node].maxprefix;
            } else {
                tr[node].maxprefix = tr[left_node].maxprefix;
            }
            if (tr[right_node].maxpostfix == tr[right_node].size && data[r_rnode] == data[r_lnode]) {
                tr[node].maxpostfix = tr[right_node].maxpostfix + tr[left_node].maxpostfix;
            } else {
                tr[node].maxpostfix = tr[right_node].maxpostfix;
            }
            tr[node].maxlen = max4(tr[left_node].maxlen, tr[right_node].maxlen, tr[node].maxprefix, tr[node].maxpostfix);
            if (data[r_lnode] == data[l_rnode]) {
                tr[node].maxlen = max(tr[node].maxlen, tr[left_node].maxpostfix + tr[right_node].maxprefix);
            }
        }
    }

    void upflow(int node) {
        int left_node = node << 1, right_node = (node << 1) | 1;
        int l_lnode = tr[left_node].l, r_lnode = tr[left_node].r;
        int l_rnode = tr[right_node].l, r_rnode = tr[right_node].r;
        if (tr[left_node].maxprefix == tr[left_node].size && data[l_lnode] == data[l_rnode]) {
            tr[node].maxprefix = tr[left_node].maxprefix + tr[right_node].maxprefix;
        } else {
            tr[node].maxprefix = tr[left_node].maxprefix;
        }
        if (tr[right_node].maxpostfix == tr[right_node].size && data[r_rnode] == data[r_lnode]) {
            tr[node].maxpostfix = tr[right_node].maxpostfix + tr[left_node].maxpostfix;
        } else {
            tr[node].maxpostfix = tr[right_node].maxpostfix;
        }
        tr[node].maxlen = max4(tr[left_node].maxlen, tr[right_node].maxlen, tr[node].maxprefix, tr[node].maxpostfix);
        if (data[r_lnode] == data[l_rnode]) {
            tr[node].maxlen = max(tr[node].maxlen, tr[left_node].maxpostfix + tr[right_node].maxprefix);
        }
        if (node > 1) {
            upflow(node >> 1);
        }
    }

    void modify(int node, int l, int r, int idx, int num) {
        // printf("node=%d, l=%d, h=%d, idx=%d, num=%lld\n", node, l, r, idx, num);
        if (l==r) {
            data[idx] = num;
            upflow(node >> 1);
        } else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            if (idx <= mid) {
                modify(left_node, l, mid, idx, num);
            } else {
                modify(right_node, mid+1, r, idx, num);
            }
        }
    }

    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        vector<int> ans;
        size = s.size();
        for (int i = 0; i < size; i++) {
            data[i] = (int)s[i];
        }
        build(1, 0, size-1);
        for (int i = 0; i < queryIndices.size(); i++) {
            modify(1, 0, size-1, queryIndices[i], int(queryCharacters[i]));
            ans.push_back(tr[1].maxlen);
            // printf("%d: ", i+1);
            // for (int i = 0; i < size; i++) {
            //     printf("%d, ", data[i]);
            // }
            // printf("\n");
        }

        return ans;
    }
};


int main() {
    string s = "geuqjmt", queryCharacters = "bgemoegklm";
    int a[100] = {3,4,2,6,5,6,5,4,3,2};
    vector<int> queryIndices(a, a+queryCharacters.size());
    Solution sol;
    vector<int> ans = sol.longestRepeating(s, queryCharacters, queryIndices);
    for (int i = 0; i < ans.size(); i++) {
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}