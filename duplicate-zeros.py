class Solution(object):
    def duplicateZeros(self, arr):
        arr2 = []
        for i in arr:
            if i == 0:
                arr2.append(0)
                arr2.append(0)
            else:
                arr2.append(i)
        for x in range(len(arr)):
            arr[x] = arr2[x]
        return arr
