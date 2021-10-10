
class Student:

    def __init__(self, name, r_a, test_1, test_2):
        self.name = name
        self.r_a = r_a
        self.test_1 = test_1
        self.test_2 = test_2

    # getter name
    @property
    def name(self):
        return self._name

    # setter name
    @name.setter
    def name(self, value):
        self._name = value

    # getter r_a
    @property
    def r_a(self):
        return self._r_a

    # setter r_a
    @r_a.setter
    def r_a(self, value):
        self._r_a = value

    # getter test_1
    @property
    def test_1(self):
        return self._test_1

    # setter test_1
    @test_1.setter
    def test_1(self, value):
        self._test_1 = value

    # getter test_2
    @property
    def test_2(self):
        return self._test_2

    @test_2.setter
    def test_2(self, value):
        self._test_2 = value

    def average_grades(self):
        average = (self.test_1 + self.test_2) / 2
        print("Average of ", self.name, "is: ", average)

    def show_student_data(self):
        print(
            "Name:", self.name,
            "Ra:", self.r_a,
            "Test 1:", self.test_1,
            "Test 2:", self.test_2
        )

