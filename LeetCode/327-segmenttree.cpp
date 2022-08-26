/*
Solution: Segment Tree + Discretization
we use discretization to reduce the potential number range from 1 << 32 into 3e5 (O(N * log N))
then each time we query for the number of prefixsum[:k] in interval [prefixsum[k] - upper, prefixsum[k] - lower], that is the interval number whose right edge is nums[k]
in total, we sum up the number for each k, to obtain the total intervals
!!!CAUTION!!! long long is all we need!
*/
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#define N 100010
using namespace std;
class Solution {
public:
    int tr[4*N], size_pn;
    map<long long, int> map2idx;
    long long potential_nums[N * 3];
    Solution() { size_pn = 0; }

    void build(int node,int l,int r)
    {
        if(l==r) tr[node]=0;
        else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            build(left_node,l,mid);
            build(right_node,mid+1,r);
            tr[node]=0;
        }
    }

    int query(int node,int l,int r,int a,int b)
    {
        if(a>r||b<l) return 0;
        else if(a<=l&&b>=r||l==r) return tr[node];
        else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            int left_sum=query(left_node,l,mid,a,b);
            int right_sum=query(right_node,mid+1,r,a,b);
            return left_sum + right_sum;
        }
    }

    void upflow(int node) {
        tr[node] = tr[node<<1] + tr[(node<<1)|1];
        if (node > 1) {
            upflow(node >> 1);
        }
    }

    void modify(int node, int l, int r, int idx, int num) {
        // printf("node=%d, l=%d, h=%d, idx=%d, num=%lld\n", node, l, r, idx, num);
        if (l==r) {
            tr[node] += num;
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

    void push_map(long long val) {
        if (map2idx.find(val) == map2idx.end()) {
            map2idx[val] = 0;
            potential_nums[size_pn++] = val;
        }
    }
    
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        vector<long long> prefix_sums;
        prefix_sums.push_back(0ll);
        for (int i = 0; i < nums.size(); i++) {
            prefix_sums.push_back((long long)nums[i] + prefix_sums[prefix_sums.size() - 1]);
        }
        push_map(0ll);
        long long lowerll = (long long)lower, upperll = (long long)upper;
        for (int i = 1; i < prefix_sums.size(); i++) {
            push_map((long long)(prefix_sums[i]));
            push_map((long long)(prefix_sums[i]) - lowerll);
            push_map((long long)(prefix_sums[i]) - upperll);
        }
        sort(potential_nums, potential_nums + size_pn);
        for (int i = 0; i < size_pn; i++) {
            map2idx[potential_nums[i]] = i;
        }
        // for (int i = 0; i < size_pn; i++) {
        //     printf("%lld ", potential_nums[i]);
        // }
        // printf("\n");
        build(1, 0, size_pn-1);
        modify(1, 0, size_pn-1, map2idx[0ll], 1);
        int _sum = 0;

        for (int i = 1; i < prefix_sums.size(); i++) {
            int low = map2idx[(long long)(prefix_sums[i]) - upperll];
            int high = map2idx[(long long)(prefix_sums[i]) - lowerll];
            int idx = map2idx[(long long)(prefix_sums[i])];
            _sum += query(1, 0, size_pn-1, low, high);
            modify(1, 0, size_pn-1, idx, 1);
            // printf("l = %d, h = %d, idx = %d\n", low, high, idx);
        }
        
        return _sum;
    }
};

int main() {
    int a[10] = {2147483647,-2147483648,-1,0};
    int lower = -1, upper = 0;
    vector<int> nums(a, a+4);
    Solution sol;
    int ans = sol.countRangeSum(nums, lower, upper);
    cout << ans << endl;
    return 0;
}