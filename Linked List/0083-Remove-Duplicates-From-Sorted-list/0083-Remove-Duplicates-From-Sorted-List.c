/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode node;
int check(node *h1,int val){
    node *temp=h1;
    while(temp!=NULL){
        if(temp->val==val){
            return 1;
        }
        temp=temp->next;
    }
    return 0;
}

node *insert(node *h1,int val){
    node *nn=(node*)malloc(sizeof(node));
    nn->val=val;
    nn->next=NULL;
    if(h1==NULL){
        h1=nn;
        return h1;
    }
    else{
        node *temp=h1;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=nn;
        return h1;
    }
}

struct ListNode* deleteDuplicates(struct ListNode* head) {
    node *h2=NULL,*temp=head;
    while(temp!=NULL){
        if(!check(h2,temp->val)){
            h2=insert(h2,temp->val);
        }
        temp=temp->next;
    }
    return h2;
}
