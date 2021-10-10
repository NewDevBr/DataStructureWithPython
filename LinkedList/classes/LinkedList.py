from DataStructure.LinkedList.classes.phone import Phone
import random


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
    def show(self):
        current_phone = self.init
        for i in range(0, self.size - 1):
            print(
                "Name:", current_phone.name,
                "Number:", current_phone.number,
                "Description:", current_phone.description,
                "Address:", current_phone.full_address
            )
            current_phone = current_phone.next

    # Create a new element at first position of list
    def insert_on_init(self, name, number, description, address):
        phone = Phone(name, number, description, address)
        phone.next = self._init
        self._init = phone
        self._size += 1

    # Helps insert elements in specific positions
    def insert(self, position, name, number, description, address):
        if position == 0:
            self.insert_on_init(name, number, description, address)
            return
        previous_phone = self._phone(position - 1)
        phone = Phone(name, number, description, address)
        phone.next = previous_phone.next
        previous_phone.next = phone
        self._size += 1

    def _phone(self, position):
        self.validate_position(position)
        current_phone = self.init
        for i in range(0, position):
            current_phone = current_phone.next
        return current_phone

    # Help determines if a position is valid. This is
    # used to various functions
    def validate_position(self, position):
        if 0 <= position < self.size:
            return True
        raise IndexError(
            "Invalid position {}".format(position))

    # Remove the first element at product linked list
    def remove_from_init(self):
        removed = self._init
        self._init = self._init.next
        removed.next = None
        self._size -= 1
        return removed

    # Removes a element at parameterized position
    def remove(self, position):
        if position == 0:
            return self.remove_from_init()
        previous_phone = self._phone(position - 1)
        removed = previous_phone.next
        previous_phone.next = removed.next
        removed.next = None
        self._size -= 1
        return removed

    # This method return a product at parameter position
    def item_at(self, position):
        if position <= (self._size - 1):
            print(
                "Name:", self._phone(position).name,
                "Number:", self._phone(position).number,
                "Description:", self._phone(position).description,
                "Address:", self._phone(position).full_address
            )
        else:
            print("The position entered does not exist, you can't see this register")

    # This method remove a random product
    def remove_random_register(self):
        number = random.randint(0, (self._size - 1))
        removed_phone = self.remove(number)
        print('Random contact removed is: ', removed_phone.description)
