class node{
    public:
    int val;
    node *next;
    node(int data)
    {
        val=data;
        next=NULL;
    }
};


class MyLinkedList {
public:
    node* head;
    MyLinkedList() {
        head=NULL;
    }

    int get(int index) {
        int c=1;
        if (head==NULL) return -1;
        node* ptr=head;
        while(ptr->next !=NULL && index!=0){
            ptr=ptr->next;
            index-=1;
        }
        if(index!=0) return -1;
        return ptr->val;
    }
    
    void addAtHead(int val) {
        node* ptr=new node(val);
        ptr->next=head;
        head=ptr;
    }
    
    void addAtTail(int val) {
        node* ptr=new node(val);
        node* cur=head;
        if (head==NULL){
            head=ptr;
            return;
        }
        while(cur->next!=NULL){
            cur=cur->next;
        }
        cur->next=ptr;
    }
    
    void addAtIndex(int index, int value) {
        node*new_node=new node(value);
        if(index==0){
            addAtHead(value);
        }
        else{
            int count=0;
            node*temp=head;
            while(temp!=NULL && count<index-1){
                temp=temp->next;
                count++;
            }
            if (temp == NULL) return;
            node*right=temp->next;
            temp->next=new_node;
            new_node->next=right;
        }
    }
    
    void deleteAtIndex(int k) {
        if (head == NULL) return;
        else if(k==0){
            node*del=head;
            head=head->next;
            delete del;
        }
        else{
            int count=0;
            node*temp=head;
            while(count<k-1){
                temp=temp->next;
                count++;
            }
            if (temp == NULL || temp->next == NULL) return;
            node*del=temp->next;
            temp->next=temp->next->next;
            delete del;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */