class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_start(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        else:
            self.head = value.next
            self.head = value

    def print_info(self):
        current_element = self.head
        while current_element:
            print(current_element.value)
            current_element = current_element.next


my_list = LinkedList()
my_list.add_to_start({
    "Name": "Ani",
    "age": 44
})
my_list.add_to_start({
    "Name": "Anna",
    "age": 20
})
my_list.add_to_start({
    "Name": "Anush",
    "age": 23
})

print(my_list)
