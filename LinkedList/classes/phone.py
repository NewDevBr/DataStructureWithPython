class Phone:

    def __init__(self, name, number, description, full_address):
        self.name = name
        self.number = number
        self.description = description
        self.full_address = full_address

    # getter name
    @property
    def name(self):
        return self._name

    # setter name
    @name.setter
    def name(self, value):
        self._name = value

    # getter number
    @property
    def number(self):
        return self._number

    # setter number
    @number.setter
    def number(self, value):
        self._number = value

    # getter description
    @property
    def description(self):
        return self._description

    # setter description
    @description.setter
    def description(self, value):
        self._description = value

    # getter address
    @property
    def full_address(self):
        return self._full_address

    # setter address
    @full_address.setter
    def full_address(self, value):
        self._full_address = value
