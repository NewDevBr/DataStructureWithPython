

class LinkedList:

    def __init__(self):
        self._init = None
        self._size = 0

    @property
    def init(self):
        return self._init

    @property
    def size(self):
        return self._size

    # Scrolls through the entire linked list displaying element by element
    def show_stack(self):
        current_task = self._init
        for i in range(0, self.size):
            self.show_element(current_task.code_id, current_task.title, current_task.description, current_task.deadline)
            current_task = current_task.next

    # Create a new element at first position of list
    def insert_on_top(self, task):
        task.next = self._init
        self._init = task
        self._size += 1

    # Remove the first element at product linked list
    def remove_from_top(self):
        removed = self._init
        self._init = self._init.next
        removed.next = None
        self._size -= 1
        return removed

    def _task(self, position):
        current_task = self.init
        for i in range(0, position):
            current_task = current_task.next
        return current_task

    def show_stack_top(self):
        self.show_element(self._task(0).code_id, self._task(0).title, self._task(0).description, self._task(0).deadline)
        return self._init

    @staticmethod
    def show_element(code_id, title, description, deadline):
        print(
            "Id code: " + str(code_id) + '\n',
            "Title: " + title + '\n',
            "Description: " + description + '\n',
            "Deadline: " + deadline.strftime('%d/%m/%Y, %H:%M:%S') + '\n' + '\n'
        )
