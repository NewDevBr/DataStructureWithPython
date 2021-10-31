from queue import Queue


class BankQueue:

    # This class implements two bank queues: one to prioritized
    # attendance (according law Nº 10.048/00.) and other to normal
    # attendance.
    def __init__(self):
        self._attendance = Queue()
        self._prioritized_attendance = Queue()

    # This static function shows all customer attendance requested.
    @staticmethod
    def __show_queue_elements(attendance_queue):
        for attendance in attendance_queue.queue:
            print(
                "Code:", str(attendance.attendance_id) + ",",
                "Customer name:", attendance.customer.full_name + ",",
                "Attendance type:", attendance.attendance_type + ",",
                "Attendance requested at:", attendance.attendance_requested_at.strftime('%d/%m/%Y, %H:%M:%S')
            )

    # It's used to show and get prioritized attendance client queue.
    @property
    def prioritized_attendance(self):
        self.__show_queue_elements(self._prioritized_attendance)
        return self._prioritized_attendance

    # It's used to show and get normal attendance client queue.
    @property
    def attendance(self):
        self.__show_queue_elements(self._attendance)
        return self._attendance

    # Utils for increase attendance queue.
    @attendance.setter
    def attendance(self, attendance_request):
        if attendance_request.attendance_type == "Normal":
            self._attendance.put(attendance_request)
        else:
            self._prioritized_attendance.put(attendance_request)

    # Show and returns attendance queues.
    def show_all_attendance_request(self):
        self.__show_queue_elements(self._prioritized_attendance)
        self.__show_queue_elements(self._attendance)
        return self._prioritized_attendance, self._attendance

    # This function is used to register that a
    # customer demand has been solved.
    def solve_demand(self):
        if not self._prioritized_attendance.empty():
            self._prioritized_attendance.get()
        elif not self._attendance.empty():
            self._attendance.get()
        else:
            print("There is no one in bank queue. Congratulations attendance team!")
