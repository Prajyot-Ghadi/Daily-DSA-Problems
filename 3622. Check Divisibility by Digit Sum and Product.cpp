class Solution {
public:
    bool checkDivisibility(int n) {
        int num = n;
        int digitSum = 0;
        int digitProduct = 1;

        while (n != 0) {
            int digit = n % 10;
            digitSum += digit;
            digitProduct *= digit;
            n /= 10;
        }
        if(num%(digitSum+digitProduct)==0){
            return true;
        }
        return false;
    }
};
