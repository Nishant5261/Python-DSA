class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None
    def insert_athead(val):
        nn=Node(val)
        nn.next=self.head
        self.head.prev=nn
        self.head=nn
    def append(self,val):
        nn=Node(val)
        if self.head == None:
            self.head=nn
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=nn
            nn.prev=cur
    def traverse(self):
        cur=self.head
        while cur is not None:
            print(cur.val,end=' ')
            cur=cur.next
        print()
    def insert(self,pos,val):        
        if pos==0:
            self.insert_athead(val)
        else:            
            cur=self.head
            for i in range(pos-1):
                if cur==None:
                    self.append(val)
                    return
                cur=cur.next
            nn=Node(val)
            nn.next=cur.next
            nn.prev=cur
            if cur.next:
                cur.next.prev=nn
            cur.next=nn
    def delete(self,pos):
        if pos==0:
            temp=self.head
            self.head=self.head.next
            self.head.prev=None
            del temp
        else:
            cur=self.head
            c=0
            while c<pos:
                if cur is None:
                    print("out of range")
                    return
                cur=cur.next
                c+=1
            
            n=cur.next
            p=cur.prev
            p.next=n
            if n:
                n.prev=p
            del cur
    def reverse(self):
        cur = self.head
        while cur != None:
            if cur.next==None:
                self.head=cur
                
            cur.next,cur.prev=cur.prev,cur.next
            cur=cur.prev
            
            
        
        

            
