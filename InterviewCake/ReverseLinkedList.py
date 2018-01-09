class MyList:
    class ListNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, value):
        node = self.ListNode(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def reverse(self):
        current = self.head
        self.head = self.head.next
        current.next = None
        while self.head.next:
            temp = self.head.next
            self.head.next = current
            current = self.head
            self.head = temp
        self.head.next = current

    def print_list(self):
        cursor = self.head
        while cursor.next:
            print cursor.value,
            cursor = cursor.next
        print cursor.value

linked_list = MyList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
