/*
Solution: DP + Segment Tree
A template problem. let f(n) be the max length of subarray ends with a[n], then
f(n) = max_{i < n and a[n] - k <= a[i] < a[k]} {f(i)} + 1
note that when we add f(n) into a[n] (denote as Tr[a[n]] = f[n]) from n = 0, 1, ..., N-1, then we just need to take max(Tr[a[n]-k:a[n]]) + 1, and set this value into Tr[a[n]], that is just a interval query && point modify max segment tree!
the final result is just max(Tr[...])
*/
#include<stdio.h>
#include<algorithm>
#include<iostream>
#define INF (-2147483647)
#define MINF (-2147483648)
#define N 100010
using namespace std;

struct Node {
    int value;
    int tag; // fuzhi, INF indicates unused
    int size;
    Node() { this->value = 0ll; this->tag = INF; this->size = 1; } 
};

class Solution {
public:
    int data[N];
    Node tr[4*N];

    void build(int node,int l,int r)
    {
        tr[node].size = r - l + 1;
        if(l==r) tr[node].value=data[l];
        else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            build(left_node,l,mid);
            build(right_node,mid+1,r);
            tr[node].value=max(tr[left_node].value, tr[right_node].value);
        }
    }

    void downflow(int node) {
        int tag = tr[node].tag;
        if (tag != INF && tr[node].size > 1) {
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            tr[left_node].tag = max(tr[left_node].tag, tag);
            tr[right_node].tag = max(tr[right_node].tag, tag); // note considering pred tag!!!
            tr[left_node].value = max(tr[left_node].tag, tr[left_node].value);
            tr[right_node].value = max(tr[right_node].tag, tr[right_node].value);
            tr[node].tag = INF;
        }
    }

    int query(int node,int l,int r,int a,int b)
    {
        if(a>r||b<l) return MINF;
        else if(a<=l&&b>=r||l==r) return tr[node].value;
        else {
            downflow(node);
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            int left_sum=query(left_node,l,mid,a,b);
            int right_sum=query(right_node,mid+1,r,a,b);
            return max(left_sum, right_sum);
        }
    }

    void upflow(int node) {
        tr[node].value = max(tr[node<<1].value, tr[(node<<1)|1].value);
        if (node > 1) {
            upflow(node >> 1);
        }
    }


    void modify_interval(int node, int l, int r, int mli, int mri, int num) {
        if(mli>r||mri<l) return;
        else if(mli<=l && mri>=r || l==r) {
            downflow(node);
            if (tr[node].tag != INF) {
                tr[node].tag = max(tr[node].tag, num); // note considering pred tag
            } else {
                tr[node].tag = num;
            } 
            tr[node].value = max(tr[node].value, num);
            upflow(node >> 1);
            return;
        } else {
            downflow(node);
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            modify_interval(left_node, l, mid, mli, mri, num);
            modify_interval(right_node, mid+1, r, mli, mri, num);
        }
    }
    int lengthOfLIS(vector<int>& nums, int k) {
        for (int i = 0; i < N; i++) {
            data[i] = 0;
        }
        build(1, 0, N-1);
        for (int i = 0; i < nums.size(); i++) {
            int l = max(0, nums[i]-k);
            int val = query(1, 0, N-1, l, nums[i]-1) + 1;
            int val0 = query(1, 0, N-1, nums[i], nums[i]);
            val = max(val, val0);
            modify_interval(1, 0, N-1, nums[i], nums[i], val);
            for (int i = 1; i < 10; i++) {
                printf("%d: %d, ", i, query(1, 0, N-1, i, i));
            }
            printf("\n");
            printf("%d: %d, val = %d\n", i, nums[i], val);
        }
        int _ans = query(1, 0, N-1, 0, N-1);
        return _ans;
    }
};