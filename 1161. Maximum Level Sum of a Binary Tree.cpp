class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int max_sum = INT_MIN;
        int resultLevel = 0;

        queue<TreeNode*> que;
        que.push(root);
        int currLevel = 1;

        while (!que.empty()) {

            int n = que.size();
            int sum = 0;

            while (n--) {
                TreeNode* temp = que.front();
                que.pop();

                sum += temp->val;

                if (temp->left) {
                    que.push(temp->left);
                }
                if (temp->right) {
                    que.push(temp->right);
                }
            }
            if (sum > max_sum) {
                max_sum = sum;
                resultLevel = currLevel;
            }
            currLevel++;
        }
        return resultLevel;
    }
};
