class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = ListNode(value)
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

    def delete_node(self, node_to_delete):
        # get the input node's next node, the one we want to skip to
        next_node = node_to_delete.next

        if next_node:
            # replace the input node's value and pointer with the next
            # node's value and pointer. the previous node now effectively
            # skips over the input node
            node_to_delete.value = next_node.value
            node_to_delete.next = next_node.next

        else:

            # eep, we're trying to delete the last node!
            raise Exception("Can't delete the last node with this technique!")


linked_list = MyList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
linked_list.delete_node(ListNode(3))
