class Solution:
    def maximumSwap(self, num: int) -> int:
        num0 = num
        arr = []
        while num > 0:
            arr.append(num % 10)
            num //= 10
        if len(arr) == 0:
            return 0
        else:
            arr = list(reversed(arr))
            arr_sort = list(sorted(arr, reverse=True))
            if arr == arr_sort:
                return num0
            else:
                idx = 0
                while arr[idx] == arr_sort[idx]:
                    idx += 1
                swapidx = len(arr) - 1
                val = arr_sort[idx]
                while arr[swapidx] != val:
                    swapidx -= 1
                arr[idx], arr[swapidx] = val, arr[idx]
                return int(''.join([str(j) for j in arr]))