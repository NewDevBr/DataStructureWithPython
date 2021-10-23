from LinkedList import LinkedList


class Stack:

    def __init__(self):
        self.stack = LinkedList()

    # print top pile register
    def show_register_on_pile_top(self):
        return self.stack.show_stack_top()

    # return true if pile is empty
    def pile_is_empty(self):
        return self.stack.size == 0

    # insert on stack top
    def stack_up(self, task):
        self.stack.insert_on_top(task)

    # remove from stack top
    def unstack_from_top(self):
        self.stack.remove_from_top()

    # show all stack registers
    def show_stack(self):
        self.stack.show_stack()
