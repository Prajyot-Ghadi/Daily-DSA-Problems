class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_difference(H):
            below = 0.0
            above = 0.0

            for x, y, l in squares:
                if H <= y:
                    above += l * l
                elif H >= y + l:
                    below += l * l
                else:
                    below += l * (H - y)
                    above += l * ((y + l) - H)

            return above - below

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        while high - low > 1e-6:
            mid = (low + high) / 2
            if area_difference(mid) > 0:
                low = mid
            else:
                high = mid

        return low
