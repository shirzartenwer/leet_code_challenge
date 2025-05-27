class Solution:
    def __init__(self):
        self.sum = 0

    def numberOfArithmeticSlices(self, A):
        self.slices(A, len(A) - 1)
        return self.sum

    def slices(self, A, i):
        if i < 2:
            return 0
        ap = 0
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            ap = 1 + self.slices(A, i - 1)
            self.sum += ap
        else:
            self.slices(A, i - 1)
        return ap
