
class Node:
    right = None
    left = None

    def __init__(self, key='', value=0, prev=None, next=None, right=None, left=None):
        self.key=key
        self.value=value
        self.prev=prev
        self.next=next

    def setnext(self, n):
        self.next = n

    def setprev(self, p):
        self.prev = p

    def setvalue(self, v):
        self.value=v

    def getnext(self):
        return self.next

    def getprev(self):
        return self.prev

    def getvalue(self):
        return self.value

    def getkey(self):
        return self.key


class MYQueue:
    size = 0
    header = Node()
    tail = Node()

    def __init__(self):
        self.header.setnext(self.tail)
        self.tail.setprev(self.header)
        size = 2

    def insert(self, k, v):
        newnode = Node(k, v)
        temp = self.tail.getprev()
        self.tail.setprev(newnode)
        newnode.setnext(self.tail)
        newnode.setprev(temp)
        temp.setnext(newnode)
        self.size += 1
        return newnode

    def display(self):
        temp = self.header.getnext()
        while temp.getnext() is not None:
            print(temp.getkey())
            print(temp.getvalue())
            temp = temp.getnext()

    def removemin(self):
        itr=self.header.getnext()
        temp=itr
        minval=itr.getvalue()
        while itr.getnext() is not None:
            if minval>itr.getvalue():
                temp=itr
                minval=itr.getvalue()
            itr=itr.getnext()
        tempprev=temp.getprev()
        tempprev.setnext(temp.getnext())
        temp.getnext().setprev(tempprev)
        self.size-= 1
        return temp


def inorder(root):
    if root is not None:
        print(root.getkey())
        inorder(root.left)
        inorder(root.right)