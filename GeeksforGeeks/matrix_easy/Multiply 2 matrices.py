class Solution:
    def multiply(self, mat1, mat2):
        # Code here
        r1 = len(mat1)
        c1 = len(mat1[0])
        r2 = len(mat2)
        c2 = len(mat2[0])

        if c1 != r2:
            return -1

        res = [[0] * c2 for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res
