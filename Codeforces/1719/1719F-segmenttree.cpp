/*
Solution: segment tree
supplement for tutorial:
we need to hold the following values in segment tree:
select k = 1, n/p_i + j, where p_i can choose all the factor of n, j can choose the integers 0,1,2,...,n/p_i - 1
note that in worst case, that is O(n) large.
Also, when we need to modify one value of original array, we need to modify 1 + |set(pi)| times in segment tree, the times is no larger then 7,
as 2 * 3 * 5 * 7 * 11 * 13 * 17 > 10^5, so the prime factor can be no larger than 6


following is copyed from the tutorial (https://codeforces.com/blog/entry/106049):
Let's note that the answer for ð=ð¥ and ð=gcd(ð¥,ð) is the same.

Indeed, for the number ð, we will visit numbers with indices ð +ððmodð for ð from 0 to ðâ1 inclusive, from this we can see that the index of the ð-th number coincides with the index of ð+ðgcd(ð,ð), and if we look at two indexes, the difference between which is ð and ð<ðgcd(ð,ð), then they are different, since ðâðmodðâ 0, therefore, the answer is (the sum of numbers with indices ð +ððmodð for ð from 0 to ðgcd(ð,ð)â1) âgcd(ð,ð).

Now let's prove that the first gcd(ð,ð) numbers are the same for (ð ,ð¥) and (ð ,gcd(ð¥,ð)), note that only those indices that have the same remainder as ð  when divided by gcd(ð¥,ð) are suitable, but there are only ðgcd(ð,ð) of such indices, and we proved that we should have ðgcd(ð,ð) of different indices, so they are all represented once, therefore the answer for ð=ð¥ and ð=gcd(ð¥,ð) is the same, because the sum consists of the same numbers.

So, we need to consider only ð being divisors of ð, this is already passes tests if we write, for example, a segment tree, but we don't want to write a segment tree, so we go further, prove that for ð1=ð¥, the answer is less or equal than for ð2=ð¥âð¦ if ð1 and ð2 are divisors of ð, why is this so?

Note that for the number ð, the answer beats for gcd(ð,ð) groups of numbers, so that in each group there is exactly ð/gcd(ð,ð) and each number is in exactly one group, and for different ð  the answer will be (the sum in the group that ð  belongs to) âgcd(ð,ð).

Let's look at the answer for the optimal ð  for ð1, let's call the set at which it is reached ð¡, note that in ð2 for different ð  there are ð independent sets that are subsets of ð¡. Let ðð be the sum in the ð-th set. Now note that we need to prove ððð¥(ð1,ð2,â¦,ðð¦)âð¦â¥ð1+ð2+â¦ðð¦ this is true for any ðð, easy to see.

So you need to iterate the divisors which equals to ðð where ð is prime, now it can be passed with a set. Hurray!

For the divisor ð, it is proposed to store answers for all pairs (ð ,ð), where ð â¤ðð and the maximum among them, they can be counted initially for ð(ððððð) for one ð, each request is changing one of the values, this can be done for ð(ðððð).

The complexity of the author's solution is ð(6âðlog(ð)), where 6 is the maximum number of different prime divisors of the number ð.
*/

#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;

const int N=300010;

long long data[N],tr[4*N],d_orig[N];

void build(int node,int l,int r)
{
    if(l==r) tr[node]=data[l];
    else {
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        build(left_node,l,mid);
        build(right_node,mid+1,r);
        tr[node]=std::max(tr[left_node],tr[right_node]);
    }
}

long long query(int node,int l,int r,int a,int b)
{
    if(a>r||b<l) return -0x7f7f7f7f;
    else if(a<=l&&b>=r||l==r) return tr[node];
    else {
        int mid=l+((r-l)>>1);
        int left_node=node<<1;
        int right_node=(node<<1)|1;
        long long left_max=query(left_node,l,mid,a,b);
        long long right_max=query(right_node,mid+1,r,a,b);
        return std::max(left_max,right_max);
    }
}

void upflow(int node) {
    tr[node] = std::max(tr[node<<1], tr[(node<<1)|1]);
    if (node > 1) {
        upflow(node >> 1);
    }
}

void modify(int node, int l, int r, int idx, long long num) {
    // printf("node=%d, l=%d, h=%d, idx=%d, num=%d\n", node, l, r, idx, num);
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



int main()
{
    int PN = 20;
    int primes[PN], deltas[PN];
    int t = 0;
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        int n, q;
        scanf("%d%d",&n,&q);
        int pn = 1;
        int remained = n;
        int cur_p = 2;
        deltas[0] = 1;
        primes[0] = n;
        while (true) {
            if (remained % cur_p == 0){
                deltas[pn] = n / cur_p;
                primes[pn++] = cur_p;

                remained /= cur_p;
                while (remained % cur_p == 0) {
                    remained /= cur_p;
                }
            }
            cur_p += 1;
            if (remained == 1) break;
        }

        // for (int i = 0; i < pn; i++) {
        //     printf("%d(%d) ", primes[i], deltas[i]);
        // }
        // printf(" this prime\n");
        // cout << endl;


        for(int i=0;i<n;i++) scanf("%lld",&d_orig[i]);
        int allN = 0;
        for (int i = 0; i < pn; i++) {
            for (int j = 0; j < deltas[i]; j++) {
                long long _sum = 0;
                for (int k = 0; k < primes[i]; k++) {
                    _sum += d_orig[j + k * deltas[i]];
                }
                data[++allN] = _sum * (long long)deltas[i];
            }
        }
        // printf("Len data = %d\n", allN);
        // for (int i = 1; i <= allN; i++) {
        //     printf("%d ", data[i]);
        // }
        // printf("\n");
        build(1,1,allN);
        int p;
        long long x;
        printf("%lld\n", query(1, 1, allN, 1, allN));
        for(int i=0;i<q;++i)
        {
            scanf("%d%lld",&p,&x);
            long long delta = x - d_orig[p-1];
            d_orig[p-1] = x;
            int idx = 1;

            // for (int k = 1; k < 8; k++) {
            //     printf("%d ", data[k]);
            // }
            // printf("\n");
            // for (int k = 1; k < 8; k++) {
            //     printf("%d ", tr[k]);
            // }
            // printf("\n");
            for (int j = 0; j < pn; j++) {
                int cur_idx = idx + (p-1) % deltas[j];
                // printf("cur_idx = %d, cur_p = %d\n", cur_idx, primes[j]);
                // printf("modify allN = %d, cur_idx = %d\n", allN, cur_idx);
                modify(1, 1, allN, cur_idx, delta * (long long)(deltas[j]));
                // for (int k = 1; k < 8; k++) {
                //     printf("%d ", tr[k]);
                // }
                // printf("\n");

                idx += n / primes[j];
            }
            printf("%lld\n", query(1, 1, allN, 1, allN));
        }
    }
    
    return 0;
}