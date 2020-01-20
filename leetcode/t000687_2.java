class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        // 自顶向下，暴力搜索.
        int count = 0;
        search_top_down(root, count);
        return count;
    }
    
    // 搜索当前节点，以当前节点为最长路径的根进行搜索.
    int bfs(TreeNode* root, int & count)
    {
        int left = 0, right = 0;
        // 1.递归返回条件
        if (root == NULL) { return left; }

        // 2.递归体
        if (root->left != NULL && root->left->val == root->val)
        { left = bfs(root->left, count); }
        if (root->right != NULL && root->right->val == root->val)
        { right = bfs(root->right, count); }

        // 3.合并子问题.
        int current = max(left, right) + 1;
        count = max(count, left+right);  // 更新count，注意是路径长度，不是节点个数.
        return current;
    }

    // 搜索整棵树.
    void search_top_down(TreeNode * root, int & count)
    {
        // 1.返回条件
        if (root == NULL) { return; }
        
        // 2.搜索当前节点.
        bfs(root, count);

        // 3.搜索子树
        search_top_down(root->left, count);
        search_top_down(root->right, count);
    }
};