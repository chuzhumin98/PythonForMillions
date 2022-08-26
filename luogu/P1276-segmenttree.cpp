/*
Solution: Segment Tree
we need to use segment tree to store for the tree status: tree (2), tiny tree (1), hole (0), mixture (-1). operation: whole query && interval modify
Each time we split into several segment to store for the lazy status
*/
#include<stdio.h>
#include<algorithm>
#include<iostream>
#define INF (2147483647ll)
using namespace std;
const int N=300010;
int cut_miao = 0;

struct Node {
    long long value;
    long long tag; // fuzhi, INF indicates unused
    int size;
    int tag_type; // 0: hole, 1: tree miao, 2: tree, -1: mixture
    Node() { this->value = 0ll; this->tag = INF; this->size = 1; this->tag_type = 2; } 
};

long long data[N];
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
        tr[node].value=tr[left_node].value + tr[right_node].value;
    }
}

void downflow(int node) {
    long long tag = tr[node].tag;
    if (tag != INF) {
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        tr[left_node].tag = tr[right_node].tag = tag;
        tr[left_node].value = tag * (long long)(tr[left_node].size);
        tr[right_node].value = tag * (long long)(tr[right_node].size);
        tr[node].tag = INF;
        if (tr[node].tag_type >= 0) {
            tr[left_node].tag_type = tr[right_node].tag_type = tr[node].tag_type;
        }
    }
}

long long query(int node,int l,int r,int a,int b)
{
    if(a>r||b<l) return 0ll;
    else if(a<=l&&b>=r||l==r) return tr[node].value;
    else {
        downflow(node);
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        long long left_sum=query(left_node,l,mid,a,b);
        long long right_sum=query(right_node,mid+1,r,a,b);
        return left_sum + right_sum;
    }
}

int query_miao(int node, int l, int r) {
    if (l == r) {
        return tr[node].tag_type == 1 ? 1 : 0;
    } else {
        if (tr[node].tag_type >= 0) {
            return tr[node].tag_type == 1 ? tr[node].size : 0;
        } else {
            int mid=l+((r-l)>>1);
            int left_node=node<<1;
            int right_node=(node<<1)|1;
            int left_cnt=query_miao(left_node,l,mid);
            int right_cnt=query_miao(right_node,mid+1,r);
            return left_cnt + right_cnt;
        }
    }
}

void upflow(int node) {
    tr[node].value = tr[node<<1].value + tr[(node<<1)|1].value;
    if (tr[node<<1].tag_type == tr[(node<<1)|1].tag_type) {
        tr[node].tag_type = tr[node << 1].tag_type;
    } else {
        tr[node].tag_type = -1;
    }
    if (node > 1) {
        upflow(node >> 1);
    }
}



void modify(int node, int l, int r, int idx, long long num) {
    // printf("node=%d, l=%d, h=%d, idx=%d, num=%lld\n", node, l, r, idx, num);
    if (l==r) {
        tr[node].value = num;
        upflow(node >> 1);
    } else {
        downflow(node);
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


void modify_interval(int node, int l, int r, int mli, int mri, long long num) {
    if(mli>r||mri<l) return;
    else if(mli<=l && mri>=r || l==r) {
        if (num == 0ll) {
            int cnt_miao = query_miao(node, l, r);
            cut_miao += cnt_miao;
            tr[node].tag_type = 0;
            tr[node].tag = num;
            tr[node].value = num * (long long)(tr[node].size);
            upflow(node >> 1);
        } else {
            if (tr[node].tag_type == 0 || tr[node].tag_type == 1) {
                tr[node].tag_type = (int)(num);
                tr[node].tag = num;
                tr[node].value = num * (long long)(tr[node].size);
                upflow(node >> 1);
            } else if (tr[node].tag_type == -1) {
                downflow(node);
                int mid=l+((r-l)>>1);
                int left_node=node<<1;
                int right_node=(node<<1)|1;
                modify_interval(left_node, l, mid, mli, mri, num);
                modify_interval(right_node, mid+1, r, mli, mri, num);
            }
        }
    } else {
        downflow(node);
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        modify_interval(left_node, l, mid, mli, mri, num);
        modify_interval(right_node, mid+1, r, mli, mri, num);
    }
}



int main() {
    int L, N;
    scanf("%d%d", &L, &N);
    for (int i = 0; i <= L; i++) {
        data[i] = 1ll;
    }
    build(1, 0, L);
    for (int i = 0; i < N; i++) {
        int flag, A, B;
        scanf("%d%d%d", &flag, &A, &B);
        modify_interval(1, 0, L, A, B, (long long)flag);
    }
    
    // for (int i = 1; i < 22; i++) {
    //     printf("%d: %lld, tag = %d\n", i, tr[i].value, tr[i].tag_type);
    // }

    // printf("%lld, %d, %d\n", tr[1].value, cut_miao, query_miao(1, 0, L));

    printf("%d\n%d\n", query_miao(1, 0, L), cut_miao);

    return 0;
}