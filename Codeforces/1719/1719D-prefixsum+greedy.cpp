/*
Solution: prefix sum + greedy
supplement for tutorial: how to find the maximum non-intersection intervals?
We can use greedy strategy to get it.
First we can sort all the xor-zero intervals with right end, (only consider the small interval, if [l, m], [m+1, r], [l, r] are all possible interval, we can just remove [l, r] as there exist two better interval to replace it)
Then we just need to record, for choosing the most K intervals, what is the smallest idx for the K-th interval's right end?
thus, we can just get the maximum intervals in O(n) visit time!

following is copyed from the tutorial (https://codeforces.com/blog/entry/106049):
There is an answer where the time spent is minimal and the lengths of all the segments taken are 1 and 2. because of the segment 𝑙,𝑟,𝑥 can be replaced to ⌈𝑟−𝑙+1 / 2⌉ of segments of length 2 and 1, or rather [𝑙,𝑙+1,𝑥],[𝑙+2,𝑙+3,𝑥],…,[𝑟,𝑟,𝑥](or [𝑟−1,𝑟,𝑥] if (𝑙−𝑟+1) even).

Note that if 𝑎𝑙⊕𝑎𝑙+1⊕…⊕𝑎𝑟=0 is executed for 𝑙,𝑟, then we can fill the 𝑙,𝑟 subsections with zeros for 𝑟−𝑙 seconds with queries [𝑙,𝑙+1,𝑎𝑙],[𝑙+1,𝑙+2,𝑎𝑙⊕𝑎𝑙+1],...[𝑟−1,𝑟,𝑎𝑙⊕𝑎𝑙+1⊕…⊕𝑎𝑟].

Note that if a segment of length 2 intersects with a segment of length 1, they can be changed to 2 segments of length 1.

It follows from all this that the answer consists of segments of length 1 and cover with segments of length 2. Then it is easy to see that the answer is (𝑛 minus (the maximum number of disjoint sub-segments with a xor of 0)), because in every sub-segments with a xor of 0 we can spend 1 second less as I waited before. this amount can be calculated by dynamic programming or greedily. Our solution goes greedy with a set and if it finds two equal prefix xors(𝑝𝑟𝑒𝑓𝑖𝑥𝑙=𝑝𝑟𝑒𝑓𝑖𝑥𝑟 means that 𝑎𝑙+1⊕𝑎𝑙+2⊕…⊕𝑎𝑟=0), it clears the set. 168724728

The complexity of the solution is 𝑂(𝑛log(𝑛)).
*/

#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
struct interval {
    int left, right;
    void set_value(int l, int r) {
        this->left = l;
        this->right = r;
    }
};
bool cmp_interval(const interval &a, const interval &b) {
     return a.left < b.right; // increasing order
}

const int NMAX = 100010;
int arr[NMAX], size_itvs = 0;
interval itvs[NMAX];
void init_array_fromscanf(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
}

int get_xor(int a, int b) {
    return ((~a) & b) | (a & (~b));
}

int main() {
    int t = 0;
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        int n = 0;
        scanf("%d", &n);
        init_array_fromscanf(arr, n);
        map<int, int> value2idx;
        value2idx[0] = -1; 
        int _xor_sum = 0;
        for (int i = 0; i < n; i++) {
            _xor_sum = get_xor(_xor_sum, arr[i]);
            if (value2idx.find(_xor_sum) != value2idx.end()) {
                itvs[size_itvs++].set_value(value2idx[_xor_sum], i);               
            }
            value2idx[_xor_sum] = i;
            // printf("%d: %d\n", i, _xor_sum);
        }

        // for (int i = 0; i < size_itvs; i++) {
        //     printf("left = %d, right = %d\n", itvs[i].left, itvs[i].right);
        // }


        int max_intervals = 0, rightmost = -1;
        for (int i = 0; i < size_itvs; i++) {
            if (itvs[i].left >= rightmost) {
                max_intervals++;
                rightmost = itvs[i].right;
            }
        }
        printf("%d\n", n - max_intervals);

        size_itvs = 0;
        

    }

    return 0;
}