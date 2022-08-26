#include<stdio.h>
#include<algorithm>
#include<iostream>
#define INF (9223372036854775807ll)
using namespace std;
const int N=1000010;


struct Node {
    long long value;
    long long tag; // fuzhi, INF indicates unused
    long long tag_add; // add value, INF indicates unused
    int size;
    Node() { this->value = 0ll; this->tag = INF; this->tag_add=INF; this->size = 1; } 
};

long long data[N];
Node tr[4*N];
int TRMAX;

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
    long long tag = tr[node].tag;
    long long tag_add = tr[node].tag_add;
    int left_node=node<<1;
    int right_node=(node<<1)|1;
    if (tag != INF) {      
        tr[left_node].tag = tr[right_node].tag = tag;
        tr[left_node].tag_add = tr[right_node].tag_add = INF;
        tr[left_node].value = tag;
        tr[right_node].value = tag;
        tr[node].tag = INF;
    }
    if (tag_add != INF) {
        if ((left_node << 1) <= TRMAX) {
            if (tr[left_node].tag != INF) {
                downflow(left_node);
            }      
        }
        if ((right_node << 1) <= TRMAX) {
            if (tr[right_node].tag != INF) {
                downflow(right_node);
            }
        }
        if (tr[left_node].tag_add == INF) {
            tr[left_node].tag_add = 0ll;
        }
        tr[left_node].tag_add += tag_add;
        tr[left_node].value += tag_add;

        if (tr[right_node].tag_add == INF) {
            tr[right_node].tag_add = 0ll;
        }
        tr[right_node].tag_add += tag_add;
        tr[right_node].value += tag_add;

        tr[node].tag_add = INF;
    }
}

long long query(int node,int l,int r,int a,int b)
{
    if(a>r||b<l) return -INF;
    else if(a<=l&&b>=r||l==r) return tr[node].value;
    else {
        downflow(node);
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        long long left_max=query(left_node,l,mid,a,b);
        long long right_max=query(right_node,mid+1,r,a,b);
        return max(left_max, right_max);
    }
}

void upflow(int node) {
    tr[node].value = max(tr[node<<1].value, tr[(node<<1)|1].value);
    if (node > 1) {
        upflow(node >> 1);
    }
}



void modify(int node, int l, int r, int idx, long long num, int type) { // type: 1 equal to, 2 add with
    // printf("node=%d, l=%d, h=%d, idx=%d, num=%lld\n", node, l, r, idx, num);
    if (l==r) {
        if (type == 1) { tr[node].value = num; }
        else { tr[node].value += num; }
        upflow(node >> 1);
    } else {
        downflow(node);
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        if (idx <= mid) {
            modify(left_node, l, mid, idx, num, type);
        } else {
            modify(right_node, mid+1, r, idx, num, type);
        }
    }
}


void modify_interval(int node, int l, int r, int mli, int mri, long long num, int type) { // type: 1 equal to, 2 add with
    if(mli>r||mri<l) return;
    else if(mli<=l && mri>=r || l==r) {
        if (l < r) downflow(node);
        if (type == 1) {
            tr[node].tag = num;
            tr[node].value = num;
        } else {
            tr[node].tag_add = num;
            tr[node].value += num;
        }       
        upflow(node >> 1);
        return;
    } else {
        downflow(node);
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        modify_interval(left_node, l, mid, mli, mri, num, type);
        modify_interval(right_node, mid+1, r, mli, mri, num, type);
    }
}



int main() {
    // freopen("./points/P1253_2.in", "r", stdin);
    // freopen("./points/P1253_2_me.out", "w", stdout); 
    
    int n, q;
    TRMAX = 2 * n - 1;
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &data[i]);
    }
    build(1, 0, n-1);
    int oper, l, r;
    long long x;
    for (int i = 0; i < q; i++) {
        scanf("%d%d%d", &oper, &l, &r);
        if (oper <= 2) {
            scanf("%lld", &x);
            modify_interval(1, 0, n-1, l-1, r-1, x, oper);
        } else {
            printf("%lld\n", query(1, 0, n-1, l-1, r-1));
        }

    }
    // for (int i = 1; i < 10; i++) {
    //     printf("%d: %lld, tag_add = %lld\n", i, tr[i].value, tr[i].tag_add);
    // }
    return 0;
}