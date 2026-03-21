class Solution(object):
    def checkValid(self, matrix):

        kt = list(range(1, len(matrix) + 1))

        for i in range(len(matrix)):
            if sorted(matrix[i]) != kt:
                return False

        for j in range(len(matrix)):
            cot = []
            for i in range(len(matrix)):
                cot.append(matrix[i][j])
            if sorted(cot) != kt:
                return False

        return True
