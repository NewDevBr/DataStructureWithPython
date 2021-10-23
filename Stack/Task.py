import uuid
import datetime


class Task:

    def __init__(self, title, description):
        self.code_id = uuid.uuid1()
        self.title = title
        self.description = description
        self.deadline = datetime.datetime.now()

    # getter title
    @property
    def title(self):
        return self._title

    # setter title
    @title.setter
    def title(self, value):
        self._title = value

    # getter description
    @property
    def description(self):
        return self._description

    # setter description
    @description.setter
    def description(self, value):
        self._description = value

    # getter deadline
    @property
    def deadline(self):
        return self._deadline

    # setter deadline
    @deadline.setter
    def deadline(self, value):
        self._deadline = value
