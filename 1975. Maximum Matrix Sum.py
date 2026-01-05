class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_value = float("inf")

        for row in matrix:
            for num in row:
                total_sum += abs(num)

                if num < 0:
                    negative_count += 1

                min_value = min(min_value, abs(num))

        if negative_count % 2 == 1:
            total_sum -= 2 * min_value

        return total_sum

