
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode node;
void insert(node **head,int val){
    node *newnode=(node*)malloc(sizeof(node));
    newnode->val=val;
    newnode->next=NULL;
    if(*head==NULL){
        *head=newnode;
    }
    else{
        node *temp=*head;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newnode;
    }
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry=0;
    node *res=NULL;
    while(l1!=NULL && l2!=NULL){
        int sum=l1->val+l2->val+carry;
        if(sum>=10){
            carry=(sum/10);
            sum=sum%10;
        }
        else{
            carry=0;
        }
        insert(&res,sum);
        l1=l1->next;
        l2=l2->next;
    }
    while(l1!=NULL){
        int sum=l1->val+carry;
        if(sum>=10){
            carry=(sum/10);
            sum=sum%10;
        }
        else{
            carry=0;
        }
        insert(&res,sum);
        l1=l1->next;
    }
    while(l2!=NULL){
        int sum=l2->val+carry;
        if(sum>=10){
            carry=(sum/10);
            sum=sum%10;
        }
        else{
            carry=0;
        }
        insert(&res,sum);
        l2=l2->next;
    }
    if(carry){
        insert(&res,carry);
    }
    return res;
    
}
