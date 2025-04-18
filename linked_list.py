from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
            
            new_node.next = runner
            previous.next = new_node
    
    def print_list_items(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print()
    
    def count_nodes(self):
        count = 0
        runner = self.head

        while runner is not None:
            count += 1
            runner = runner.next

        return count

    def find_node(self, target_val):
        runner = self.head

        while runner is not None:
            if runner.value == target_val:
                return True
            runner = runner.next
        
        return False
    
    def delete_node(self, target_val):
        if self.head is None:
            return False
        elif self.head.value == target_val:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next
            while (runner is not None) and (target_val > runner.value):
                previous = previous.next
                runner = runner.next

            if (runner is not None) and (runner.value == target_val):
                previous.next = runner.next
                return True
            else:
                return False
            
    def print_reversed(self):
        self.print_reversed_recursive(self.head)
        print()
    
    def print_reversed_recursive(self, node):
        if node is not None:
            self.print_reversed_recursive(node.next)
            print(node.value, end=" ")
        