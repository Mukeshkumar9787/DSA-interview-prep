class ListNode:
    def __init__(self, val, nextNode= None):
        self.val = val;
        self.nextNode = nextNode;

class LinkedList:
    
    def __init__(self):
        self.head = None;
        self.tail = self.head;
    
    def get(self, index: int) -> int:
        if self.head == None:
            return -1;
        curr = self.head;
        i = 0;
        while i < index and curr:
            i = i+1;
            curr = curr.nextNode;
        if curr:
            return curr.val;
        return -1;


    def insertHead(self, val: int) -> None:
        self.head = ListNode(val, self.head);
        if(self.tail is None):
            self.tail = self.head;

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val);
        else:
            self.tail.nextNode = ListNode(val);
            self.tail = self.tail.nextNode;

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False;
        
        if index == 0:
            self.head = self.head.nextNode;
            if self.head is None:
                self.tail = None;
            return True;

        curr = self.head;
        i = 0;
        while i < index - 1 and curr:
            i = i+1;
            curr = curr.nextNode;

        if curr is None or curr.nextNode is None:
            return False;

        nodeToRemove = curr.nextNode;
        curr.nextNode = nodeToRemove.nextNode;

        if nodeToRemove == self.tail:
            self.tail = curr;

        return True;

    def getValues(self) -> List[int]:
        result = list();
        curr = self.head;
        while curr:
            result.append(curr.val);
            curr = curr.nextNode;
        return result;
