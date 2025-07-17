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
void preorder(node *root,int *result,int *index){
    if(root!=NULL){
        result[(*index)++]=root->val;
        preorder(root->left,result,index);
        preorder(root->right,result,index);
    }
}


int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=(int*)malloc(101*sizeof(int));
    int index=0;
    preorder(root,arr,&index);
    *returnSize=index;
    return arr;
}
