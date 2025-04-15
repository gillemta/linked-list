from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(0)

my_linked_list.print_list_items()

my_linked_list.delete_node(6)

my_linked_list.print_list_items()

my_linked_list.print_reversed()