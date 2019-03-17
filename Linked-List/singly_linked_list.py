import string


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.tail = node
            self.head = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def delete(self, data):
        curr_node = self.head
        prev_node = self.head
        while curr_node:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                del curr_node
                curr_node = prev_node.next
                self.size -= 1
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def search(self, data):
        curr_node = self.head
        counter = 0
        search = []
        while curr_node:
            if curr_node.data == data:
                search.append(counter)
            curr_node = curr_node.next
            counter += 1
        if not search:
            return "{0} doesn't exist".format(str(data))
        return search

    def get_size(self):
        return self.size

    def display(self):
        if self.head is None:
            return "Empty List"
        curr_node = self.head
        while curr_node:
            print(str(curr_node.data) + "|" + str(id(curr_node)))
            curr_node = curr_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    linked_list = LinkedList()
    list(map(linked_list.add, string.ascii_uppercase))
    linked_list.delete("F")
    linked_list.display()
    print(linked_list.get_size())
    print(linked_list.search("X"))



