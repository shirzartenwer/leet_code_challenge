
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool isSameTree(TreeNode *left, TreeNode *right)
    {
        if (left != nullptr && right != nullptr)
        {
            if (left->val != right->val)
            {
                return false;
            }
        }
        else
        {
            if (left == nullptr && right == nullptr)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        return isSameTree(left->left, right->left) && isSameTree(left->right, right->right);
    }

    bool isSubtree(TreeNode *root, TreeNode *subRoot)
    {
        if (!subRoot)
            return true;
        if (root == nullptr)
        {
            return false;
        }

        // isSubroot is a single Node
        if (subRoot->left == nullptr && subRoot->right == nullptr)
        {
            if (root->left != nullptr || root->right != nullptr)
            {
                return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
            }
            else
            {
                return subRoot->val == root->val;
            }
        }
        else
        {
            // the following if condition caused an early stop in the solution, failed at the edge case and stoped early
            // root: 1- null -1 - null- 1- null -1 -null -1 -2 and subroot: 1- null -1 -2

            // if (root->val == subRoot->val){
            //     return isSameTree(root, subRoot);

            if (isSameTree(root, subRoot))
            {
                return true;
            }
            else
            {
                return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
            }
        }
    }
};