class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[len(arr) - 1]
        for i in range (len(arr) - 1, -1, -1 ):
            old_val = arr[i]
            arr[i] = current_max
            if old_val > current_max:
                current_max = old_val 
        arr[len(arr) - 1] = -1
        return arr