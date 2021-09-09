class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
        self.cursor = self.head

    def insert(self, node):
        self.num_of_nodes += 1
        prev_node = self.head
        self.head = node
        self.head.next = prev_node

    def __str__(self):

        current = self.head
        print(current)
        to_print = []
        while current != None:
            to_print.append(current.value)
            print(to_print)
            print("inside loop current", current)
            print("current.next:", current.next)
            current = current.next
        return "->".join([str(item) for item in to_print])
        # return "hi"

    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor is not None:
            print(self.cursor.value)
            yield self.cursor.value
            self.cursor = self.cursor.next


if __name__ == "__main__":
    l = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    l.insert(n1)
    l.insert(n2)
    # for i in l:
    #     print(i)
    print(l)
