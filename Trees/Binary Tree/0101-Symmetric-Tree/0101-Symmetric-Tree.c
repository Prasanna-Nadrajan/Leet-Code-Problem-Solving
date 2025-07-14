/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode node;


void inorder(node *r1,node *r2,bool *res){
    if(r1!=NULL && r2!=NULL){
        inorder(r1->left,r2->right,res);
        if(r1->val!=r2->val){
            (*res)=false;
        }
        inorder(r1->right,r2->left,res);
    }
    else if((r1==NULL && r2!=NULL) || (r1!=NULL && r2==NULL)){
        (*res)=false;
        return;
    }
}

bool isSymmetric(struct TreeNode* root) {
    bool res=true;
    inorder(root,root,&res);
    return res;
}
