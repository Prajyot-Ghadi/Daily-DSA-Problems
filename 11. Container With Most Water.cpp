class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int maxWater = 0;
        int lp = 0;
        int rp = n - 1;

        while (lp < rp) {
            int width = rp - lp;
            int ht = min(height[lp], height[rp]);
            int area = width * ht;
            maxWater = max(maxWater, area);

            if (height[lp] < height[rp]) {
                lp++;
            } else {
                rp--;
            }
        }
        return maxWater;
    }
};
