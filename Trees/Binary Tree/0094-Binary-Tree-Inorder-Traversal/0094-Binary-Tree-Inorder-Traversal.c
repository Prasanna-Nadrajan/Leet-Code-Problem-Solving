/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct TreeNode node;

void inorder(node *root,int *result,int *index){
    if(root!=NULL){
        inorder(root->left,result,index);
        result[(*index)++]=root->val;
        inorder(root->right,result,index);
    }
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int *result=(int*)malloc(100*sizeof(int));
    int index=0;
    inorder(root,result,&index);
    *returnSize=index;
    return result;
}
