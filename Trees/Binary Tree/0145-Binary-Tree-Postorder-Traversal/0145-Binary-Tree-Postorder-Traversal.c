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
void postorder(node *root,int *result,int *index){
    if(root!=NULL){
        postorder(root->left,result,index);
        postorder(root->right,result,index);
        result[(*index)++]=root->val;
    }
}


int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=(int*)malloc(101*sizeof(int));
    int index=0;
    postorder(root,arr,&index);
    *returnSize=index;
    return arr;
}



