/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode node;
void del(node **head,int pos){
    if(pos==0){
        *head=(*head)->next;
        return;
    }
    node *temp=*head,*prev=NULL;
    while(temp!=NULL && pos--){
        prev=temp;
        temp=temp->next;
    }
    if(temp!=NULL){
        prev->next=temp->next;
        free(temp);
    }
}

struct ListNode* removeElements(struct ListNode* head, int val) {
    int pos=0;
    node *temp=head;
    while(temp!=NULL){
        if(temp->val==val){
            temp=temp->next;
            del(&head,pos);
        }
        else{
            pos++;
            temp=temp->next;
        }
    }
    return head;

}
