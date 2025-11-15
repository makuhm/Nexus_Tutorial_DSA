class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        n = len(arr)
        for x in range(n, 1, -1):
            i = arr.index(x)

            if i == x - 1:
                continue
            if i != 0:
                output.append(i + 1)
                arr[0:i + 1] = reversed(arr[0:i + 1])
            output.append(x)
            arr[0:x] = reversed(arr[0:x])
        return output
