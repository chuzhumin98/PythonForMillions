/*
Solution: Dynamic Discretization
you can see the details in my problem solving link: https://leetcode.cn/problems/my-calendar-iii/solution/by-affine-twc1/
*/
#include<stdio.h>
#include<vector>
#include<iostream>
#define NMAX 810
#define TMAX (2147483647)
using namespace std;
class MyCalendarThree {
public:
    int times[NMAX];
    int counts[NMAX];
    int size;

    MyCalendarThree() {
        size = 2;
        times[0] = -1; times[1] = TMAX;
        counts[0] = 0;
    }

    int find(int t) {
        int low = 0, high = size - 1;
        while (low < high) {
            int mid = (low + high) >> 1;
            if (times[mid] == t) {
                return mid;
            } else if (times[mid] < t) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (times[low] <= t) {
            return low;
        } else {
            return low + 1;
        }
    }

    int get_max() {
        int maxv = 0;
        for (int i = 0; i < size-1; i++) {
            maxv = max(maxv, counts[i]);
        }
        return maxv;
    }
    
    int book(int start, int end) {
        int sidx = this->find(start);
        if (times[sidx] != start) {
            for (int i = size-1; i >= sidx; i--) {
                times[i+1] = times[i];
            }
            times[sidx] = start;
            for (int i = size-2; i >= sidx-1; i--) {
                counts[i+1] = counts[i];
            }     
            size ++;
        }

        int eidx = this->find(end);
        if (times[eidx] != end) {
            for (int i = size-1; i >= eidx; i--) {
                times[i+1] = times[i];
            }
            times[eidx] = end;
            for (int i = size-2; i >= eidx-1; i--) {
                counts[i+1] = counts[i];
            }     
            size ++;
        }

        for (int i = sidx; i < eidx; i++) {
            counts[i] ++;
        }

        return get_max();
    }
};


int main() {
    
    MyCalendarThree* obj = new MyCalendarThree();

    return 0;
}