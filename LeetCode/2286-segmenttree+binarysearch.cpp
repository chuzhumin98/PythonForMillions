/*
Solution: Segment Tree + Binary Search
We need a data structure to use O(log n) to find the maximum value of a[:k] (gather) and the sum of a[:k] (scatter), naturally we think to use segment tree to hold for this information
gather part: to find the smallest p to satisfy a[p] >= k && p <= maxRow, we use binary search to find the edge condition of max(a[:p]); O(log^2 n) complexity
scatter part: we first calculate sum of a[:maxRow] to check if possible to scatter, if so, we need to delete from cidx (hold for the first non-zero value, to prevent the 0......0 m condition) to maxRow until k value deleted; O(log n) complexity
In total, complexity is O(m * log^2 n + n * log n), where m is operation number
*/
#include<stdio.h>
#include<algorithm>
#include<iostream>
#define N 50010
#define MINF (-2147483648)
using namespace std;

class BookMyShow {
public:
    int data[N],tr[4*N];
    long long tr_sum[4*N];
    int n, cidx, m;

    void build(int node,int l,int r)
    {
        if(l==r) {
            tr[node]=data[l];
            tr_sum[node] = (long long)data[l];
        } else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            build(left_node,l,mid);
            build(right_node,mid+1,r);
            tr[node]=max(tr[left_node], tr[right_node]);
            tr_sum[node] = tr_sum[left_node] + tr_sum[right_node];
        }
    }

    int query(int node,int l,int r,int a,int b)
    {
        if(a>r||b<l) return MINF;
        else if(a<=l&&b>=r||l==r) return tr[node];
        else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            int left_val=query(left_node,l,mid,a,b);
            int right_val=query(right_node,mid+1,r,a,b);
            return max(left_val, right_val);
        }
    }

    long long query_sum(int node,int l,int r,int a,int b)
    {
        if(a>r||b<l) return 0ll;
        else if(a<=l&&b>=r||l==r) return tr_sum[node];
        else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            long long left_val=query_sum(left_node,l,mid,a,b);
            long long right_val=query_sum(right_node,mid+1,r,a,b);
            return left_val + right_val;
        }
    }


    void upflow(int node) {
        tr[node] = max(tr[node<<1], tr[(node<<1)|1]);
        tr_sum[node] = tr_sum[node<<1] + tr_sum[(node<<1)|1];
        if (node > 1) {
            upflow(node >> 1);
        }
    }

    void modify(int node, int l, int r, int idx, int num) {
        // printf("node=%d, l=%d, h=%d, idx=%d, num=%lld\n", node, l, r, idx, num);
        if (l==r) {
            tr[node] -= num;
            tr_sum[node] -= (long long)num;
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

    void print() {
        for (int i = 0; i < n; i++) {
            printf("%d ", data[i]);
        }
        printf("\n");
    }

    BookMyShow(int n, int m) {
        this->n = n; this->m = m;
        cidx = 0;
        for (int i = 0; i < n; i++) {
            data[i] = m;
        }
        build(1, 0, n-1);
    }
    
    vector<int> gather(int k, int maxRow) {
        vector<int> output;
        int low = 0, high = maxRow;
        while (low < high) {
            int mid = (low + high) / 2;
            if (query(1, 0, n-1, 0, mid) >= k) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        if (data[low] < k) low++;
        if (data[low] >= k && low <= maxRow) {
            output.push_back(low);
            output.push_back(this->m - data[low]);
            data[low] -= k;
            modify(1, 0, n-1, low, k);
        }
        // printf("complete gather: \n");
        // for (int i = 0; i < output.size(); i++) {
        //     printf("%d ", output[i]);
        // }
        // printf("\n");
        // print();
        return output;
    }
    
    bool scatter(int k, int maxRow) {
        long long _sum = query_sum(1, 0, n-1, 0, maxRow);
        // printf("sum = %lld\n", _sum);
        if (_sum >= (long long)k) {
            int rm_va = k;
            while (rm_va > 0) {
                if (rm_va >= data[cidx]) {
                    rm_va -= data[cidx];
                    modify(1, 0, n-1, cidx, data[cidx]);
                    data[cidx] = 0;
                    cidx++;
                } else {
                    modify(1, 0, n-1, cidx, rm_va);
                    data[cidx] -= rm_va;
                    rm_va = 0;
                    break;
                }
            }
            // print();
            return true;
        } else {
            // print();
            return false;
        }
    }
};




// int main() {
//     BookMyShow* obj = new BookMyShow(n, m);
//     vector<int> param_1 = obj->gather(k, maxRow);
//     bool param_2 = obj->scatter(k, maxRow);


//     return 0;
// }