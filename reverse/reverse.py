class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    
#non recursive solution

    def reverse_list(self, node, prev):
        prev = None
        current = self.head

        while current:
          next = current.get_next()
          current.set_next(prev)
          prev = current
          current = next
        self.head = prev

#recursive and confusing to me:
# def reverse_list(self, node, prev):
#         def reverse(node, prev):
#             # If node is None
#             if not node:
#                 # Return prev
#                 return prev
#             # Store the next as the nodes next value
#             next = node.next_node

#             # Safe to switch the next node to prev
#             node.next_node = prev

#             # Prev is now passed in node
#             prev = node

#             # Node is now the next node
#             node = next

#             # Return the recursive call passing in Node and Prev
#             return reverse(node, prev)

#         # Set the head to completed recursion.
#         self.head = reverse(self.head, None)