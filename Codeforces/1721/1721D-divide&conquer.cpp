/*
Solution: divide and conquer
we just need to consider this problem from the max bit to min bit
for each bit (1 << b), we have divided the indexs into many group, suppose one group is i1, i2, i3, ..., ik
we will try to set (a[il] ^ b[il]) = 1 for each l = 1, 2, ..., k, that is just to place a[il] = 0 with b[il] = 1
while also place a[il]=1 with b[il]=0, then we just need to count for this two numbers, to check if they equals,
if all groups' two numbers equal, then (1 << b) would be considered as one part of the answer, also we need to divide
each group into two: a[il]=0,b[il]=1 group and a[il]=1,b[il]=0, or else we do not need to divide
then, we iterate considering for (1 << (b-1))...
finally, all of the valid (1<<b) sum up for the answer
*/
#include <iostream>
#include <vector>
using namespace std;
const int NMAX = 100010, BMAX = 30;
int As[NMAX], Bs[NMAX], bitsA[NMAX], bitsB[NMAX], base2[NMAX];
int cacheA0[NMAX], cacheA1[NMAX], cacheB0[NMAX], cacheB1[NMAX]; // index
int sizeA0 = 0, sizeA1 = 0, sizeB0 = 0, sizeB1 = 0;
int main() {
    int t, n;
    scanf("%d", &t);
    base2[0] = 1;
    for (int i = 1; i < NMAX; i++) {
        base2[i] = base2[i-1] * 2;
    }
    for (int _ = 0; _ < t; _++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &As[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &Bs[i]);
        }
        vector<int> sp_nums;
        sp_nums.push_back(0);
        sp_nums.push_back(n);

        int _sum = 0;
        for (int i = BMAX-1; i >= 0; i--) {
            if (i == BMAX-1) {
                for (int j = 0; j < n; j++) {
                    bitsA[j] = As[j] / base2[i];
                    bitsB[j] = Bs[j] / base2[i];
                }
            } else {
                for (int j = 0; j < n; j++) {
                    bitsA[j] = (As[j] % base2[i+1]) / base2[i];
                    bitsB[j] = (Bs[j] % base2[i+1]) / base2[i];
                }
            }
            bool canxor = true;
            for (int j = 0; j < sp_nums.size()-1; j++) {
                int zeroA = 0, oneB = 0;
                for (int k = sp_nums[j]; k < sp_nums[j+1]; k++) {
                    if (bitsA[k] == 0) {
                        zeroA ++;
                    }
                    if (bitsB[k] == 1) {
                        oneB ++;
                    }
                }
                if (zeroA != oneB) {
                    canxor = false;
                    break;
                }
            }

            if (canxor) {
                _sum += base2[i];
                vector<int> sp_nums_new;
                for (int j = 0; j < sp_nums.size()-1; j++) {
                    sp_nums_new.push_back(sp_nums[j]);
                    sizeA0 = 0; sizeA1 = 0; sizeB0 = 0; sizeB1 = 0;
                    int zeroA = 0;
                    for (int k = sp_nums[j]; k < sp_nums[j+1]; k++) {
                        if (bitsA[k] == 0) {
                            cacheA0[sizeA0++] = As[k];
                            zeroA++;
                        } else {
                            cacheA1[sizeA1++] = As[k];
                        }
                        if (bitsB[k] == 0) {
                            cacheB0[sizeB0++] = Bs[k];
                        } else {
                            cacheB1[sizeB1++] = Bs[k];
                        }
                    }
                    int idx = sp_nums[j];
                    for (int k = 0; k < zeroA; k++) {
                        Bs[idx] = cacheB1[k];
                        As[idx++] = cacheA0[k];         
                    }
                    for (int k = 0; k < sp_nums[j+1] - sp_nums[j] - zeroA; k++) {
                        Bs[idx] = cacheB0[k];
                        As[idx++] = cacheA1[k];
                    }
                    if (zeroA != 0 && zeroA != sp_nums[j+1] - sp_nums[j]) {
                        sp_nums_new.push_back(sp_nums[j] + zeroA);
                    }
                }
                sp_nums_new.push_back(n);
                sp_nums = sp_nums_new;
            }
        }
        printf("%d\n", _sum);
    }


    return 0;
}