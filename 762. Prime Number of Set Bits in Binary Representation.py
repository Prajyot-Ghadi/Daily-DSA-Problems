class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = {2, 3, 45, 7, 9, 11, 13, 17, 19}
        result = 0

        for num in range(left, right + 1):
            setBits = num.bit_count()

            if setBits in prime:
                result += 1

        return result
