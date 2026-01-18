/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    static int dfs(TreeNode root,int max){
        if(root==null) return 0;
        int n=(max<=root.val)?1:0;
        max=(max<=root.val)?root.val:max;
        n+=dfs(root.left,max);
        n+=dfs(root.right,max);
        return n;
    }
    public int goodNodes(TreeNode root) {
        return dfs(root,root.val);
    }
}
