from DataStructure.Student.Student import Student


# Instantiating Student 1
student_1 = Student("Carlos", "123456789", 10, 10)
student_1.test_1 = 9
student_1.test_2 = 7
print("Test 1 result of Student 1:", student_1.test_1)
print("Test 2 result of Student 1:", student_1.test_2)
print("Student 1 name: ", student_1.name)
print("Student 1 RA: ", student_1.r_a)
student_1.average_grades()
student_1.show_student_data()

# Instantiating Student 2
student_2 = Student("Marcos", "123456789", 10, 10)
student_2.test_1 = 9
student_2.test_2 = 10
print("Test 1 result of Student 2:", student_2.test_1)
print("Test 2 result of Student 2:", student_2.test_2)
print("Student 2 name: ", student_1.name)
print("Student 2 RA: ", student_1.r_a)
student_2.average_grades()
student_2.show_student_data()

# Instantiating Student 3
student_3 = Student("Maria", "123456789", 10, 10)
student_3.test_1 = 10
student_3.test_2 = 10
print("Test 1 result of Student 3:", student_3.test_1)
print("Test 2 result of Student 3:", student_3.test_2)
print("Student 3 name: ", student_1.name)
print("Student 3 RA: ", student_1.r_a)
student_2.average_grades()
student_3.show_student_data()

