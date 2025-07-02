/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode node;
void insert(node **list,int val){
    node *newnode=(node*)malloc(sizeof(node));
    newnode->val=val;
    newnode->next=NULL;
    if (*list==NULL){
        *list=newnode;
    }
    else{
        node *temp=*list;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newnode;
    }
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    node *res=NULL;
    while(list1 !=NULL && list2!=NULL){
        if(list1->val <= list2->val){
            insert(&res,list1->val);
            list1=list1->next;
        }
        else{
            insert(&res,list2->val);
            list2=list2->next;
        }
    }

    while(list1!=NULL){
        insert(&res,list1->val);
        list1=list1->next;
    }

    while(list2!=NULL){
        insert(&res,list2->val);
        list2=list2->next;
    }

    return res;
}
