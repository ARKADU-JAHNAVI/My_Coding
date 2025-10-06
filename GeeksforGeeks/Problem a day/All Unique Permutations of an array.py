class Solution:
    def uniquePerms(self, arr):
        # code here 
        arr.sort()
        n = len(arr)
        used = [False] * n
        out, curr = [], []

        def backtrack():
            if len(curr) == n:
                out.append(curr[:])
                return
            for i in range(n):
                # skip if already used
                if used[i]:
                    continue
                # skip duplicates: only the first unused twin can be taken at this depth
                if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                curr.append(arr[i])
                backtrack()
                curr.pop()
                used[i] = False

        backtrack()
        return out