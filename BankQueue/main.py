from datetime import date
from Customer import Customer
from BankQueue import BankQueue
from CustomerAttendanceRequest import CustomerAttendanceRequest


# Defining customers to create a queue
customer_1 = Customer('111.111.111-11', 'Carlos', date(1998, 5, 9), False)
customer_2 = Customer('222.222.222-22', 'Maria ', date(1999, 4, 1), True)
customer_3 = Customer('333.333.333-33', 'John S', date(1942, 7, 3), False)
customer_4 = Customer('444.444.444-44', 'Fabio ', date(1945, 9, 4), True)
customer_5 = Customer('555.555.555-55', 'Robson', date(2002, 3, 6), False)

# Defining a customers attendance register (generating a random attendance id)
attendance_request_1 = CustomerAttendanceRequest(customer_1, 'Unblock credit card')
attendance_request_2 = CustomerAttendanceRequest(customer_2, 'Create Bank Account')
attendance_request_3 = CustomerAttendanceRequest(customer_3, 'Realize Bank Loan')
attendance_request_4 = CustomerAttendanceRequest(customer_4, 'Investing in the stock exchanges')
attendance_request_5 = CustomerAttendanceRequest(customer_5, 'Close Bank Account')

# Instantiating a Bank Queue
queue = BankQueue()

# Populating Bank Queue
queue.attendance = attendance_request_1
queue.attendance = attendance_request_2
queue.attendance = attendance_request_3
queue.attendance = attendance_request_4
queue.attendance = attendance_request_5

# Showing how the queue became populated
queue.show_all_attendance_request()

# Introducing elements at prioritized attendance queue
queue.prioritized_attendance

# Introducing elements at normal queue
queue.attendance

# Solving some customer requests
queue.solve_demand()
queue.solve_demand()
queue.solve_demand()

# Showing queue state with some customer attendance request done
queue.show_all_attendance_request()

# Solving some customer requests
queue.solve_demand()
queue.solve_demand()
queue.solve_demand()

# Showing final attendance request
queue.show_all_attendance_request()
