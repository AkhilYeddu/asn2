class Node:
    def __init__(self, data: int):
        self.val = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def length(self) -> int:
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def get(self, i: int) -> int:
        len_list = self.length()
        if self.head is None or i >= len_list:
            return -1
        count = 0
        temp = self.head
        while count < i:
            temp = temp.next
            count += 1
        return temp.val

    def addAtHead(self, val: int):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def addAtIndex(self, i: int, val: int):
        if i == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            count = 0
            temp = self.head
            while temp is not None and count < i - 1:
                temp = temp.next
                count += 1
            if temp is None:
                return
            new_node.next = temp.next
            temp.next = new_node

    def deleteAtIndex(self, i: int):
        if self.head is None:
            return
        if i == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            count = 0
            temp = self.head
            while count < i - 1 and temp is not None:
                temp = temp.next
                count += 1
            if temp is None or temp.next is None:
                return
            to_delete = temp.next
            temp.next = temp.next.next
            del to_delete
