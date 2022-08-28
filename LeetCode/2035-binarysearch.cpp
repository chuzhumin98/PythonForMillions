/*
Solution: Binary Search
we enumerate all the possibilities of first n nums and last n nums, stored them grouped by selected nums size, then we sort all the groups of selected nums on last n nums.
Finally, for each selection of first n nums (denote as select k nums), we binary search for the last n nums selected (n-k) numbers, with the target of sum(nums) / 2 - sum(k nums)
In total, the complexity is O(2^n + 2^n * log 2^n + 2^n * log 2^n) = O(n*2^n)
*/
#include <iostream>
#include <vector>
using namespace std;
#define NMAX 16
class Solution {
public:
    vector<int> nums;
    vector<int> pms_list_first[NMAX], pms_list_second[NMAX];
    int n;

    void enumerate_pm(int s, vector<int> arr[]) {
        for (int bit = 0; bit < (1 << this->n); bit++) {
            int val = bit, _sum = 0, _sel = 0;
            for (int i = 0; i < this->n; i++) {
                if (val % 2 == 1) {
                    _sum += this->nums[i+s];
                    _sel += 1;
                }
                val /= 2;
            }
            arr[_sel].push_back(_sum);
        }
    }

    int binary_search(vector<int>& arr, int target) {
        int low = 0, high = arr.size() - 1;
        while (true) {
            if (low >= high) { return low; }
            int mid = (low + high) / 2;
            if (arr[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }



    int minimumDifference(vector<int>& nums) {
        this->nums = nums;
        this->n = nums.size() / 2;

        this->enumerate_pm(0, this->pms_list_first);
        this->enumerate_pm(this->n, this->pms_list_second);
        for (int sel_num = 0; sel_num <= this->n; sel_num++) {
            sort(this->pms_list_second[sel_num].begin(), this->pms_list_second[sel_num].end());
        }

        int _sum_total = 0;
        for (int i = 0; i < nums.size(); i++) {
            _sum_total += nums[i];
        }
        int min_delta = 1 << 30;
        for (int sel_num = 0; sel_num <= this->n; sel_num++) {
            vector<int> nums_re = this->pms_list_second[this->n - sel_num];
            for (int i = 0; i < this->pms_list_first[sel_num].size(); i++) {
                int num = this->pms_list_first[sel_num][i];
                int idx = this->binary_search(nums_re, _sum_total / 2 - num);
                if (idx > 0) {
                    min_delta = min(min_delta, abs(nums_re[idx-1] * 2 + num * 2 - _sum_total));
                }
                min_delta = min(min_delta, abs(nums_re[idx] * 2 + num * 2 - _sum_total));
            }
        }
        return min_delta;

        
    }
};
int main() {
    int a[10] = {3,9,7,3};
    vector<int> arr(a, a+4);
    Solution sol;
    int min_delta = sol.minimumDifference(arr);
    cout << min_delta << endl;
    return 0;
}