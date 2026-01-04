class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            count = 0
            divisor_sum = 0

            for i in range(1, int(n ** (0.5) + 1)):
                if n % i == 0:
                    other_fact = n // i
                    if i == other_fact:
                        count += 1
                        divisor_sum += other_fact
                    else:
                        count += 2
                        divisor_sum += i + other_fact

            if count == 4:
                total_sum += divisor_sum

        return total_sum
