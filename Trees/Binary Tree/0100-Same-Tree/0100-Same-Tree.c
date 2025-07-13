/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode node; 
void check(node *p,node *q,bool *res){
    if(p!=NULL && q!=NULL){
        if(p->val!=q->val){
            (*res)=false;
        }
        check(p->left,q->left,res);
        check(p->right,q->right,res);
    }
    else if((p!=NULL && q==NULL)||(p==NULL && q!=NULL)){
        (*res)=false;
    }
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    bool res=true;
    check(p,q,&res);
    return res;
}
