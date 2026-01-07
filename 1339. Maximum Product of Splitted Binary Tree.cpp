class Solution {
public:
    long SUM = 0;
    long maxP = 0;

    int totalSum(TreeNode* root){
        if(root == NULL)
            return 0;
        
        int leftSubTreeSum = totalSum(root->left);
        int rightSubTreeSum = totalSum(root->right);
        int sum             = root->val + leftSubTreeSum +rightSubTreeSum;

        return sum;

    }

    int find(TreeNode* root){
        if(root == NULL)
            return 0;
        
        int leftSum = find(root->left);
        int rightSum = find(root->right);
        int subTreeSum = root->val + leftSum + rightSum;

        long remainingSum = SUM - subTreeSum;

        maxP = max(maxP,subTreeSum*remainingSum);
        
        return subTreeSum;
    }

    int maxProduct(TreeNode* root) {
        if(root==NULL)
            return 0;
        
        SUM = totalSum(root);

        find(root);

        return maxP%(1000000007); 
        
    }
};
