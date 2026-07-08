class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.len+=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.len+=1
    def traversal(self):
        curr=self.head
        c=0
        if self.head==None:
            print(self.head)
        while curr is not None and c<20 :
            print(curr.val,end=" ")
            curr=curr.next
            c+=1
    def insert(self,pos,val):
        if pos>=self.len:
            self.append(val)
        else:
            nn=Node(val)
            p=self.head
            if pos==0:
                nn.next=self.head
                self.head=nn
                self.len+=1
            else:
                c=0
                while p is not None and c<pos-1:
                    p=p.next
                    c+=1
                
                nn.next=p.next
                p.next=nn
                self.len+=1
                if self.tail==p:
                    self.tail=nn
    def delete(self,val):
        if self.head.val==val:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del temp
            self.len-=1
        else:
            fo=False
            pre=None
            cur=self.head
            while cur is not None:
                if cur.val==val:
                    fo=True
                    break
                pre=cur
                cur=cur.next
            if fo:
                pre.next=cur.next
                self.len-=1
                return
            else:
                print("Node not found")
    def reverse(self):
        pre=None
        self.tail=self.head
        cur=self.head
        while cur is not None:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        self.head=pre
            
            

            


        
            
