import uuid
from datetime import datetime


class CustomerAttendanceRequest:

    def __init__(self, customer, service_type):
        self._attendance_id = uuid.uuid1()
        self._customer = customer
        self._attendance_type = "Preferential" if (customer.age >= 60 or customer.has_especial_necessity) else "Normal"
        self._attendance_requested_at = datetime.now()
        self._service_type = service_type

    # Returns a string that contains a service description
    # that customer is looking.
    @property
    def service_type(self):
        return self._service_type

    # Returns when customer registered a request.
    @property
    def attendance_requested_at(self):
        return self._attendance_requested_at

    # Returns type of attendance that client needs. If is
    # needed a preferential or normal attendance according
    # law Nº 10.048/00.
    @property
    def attendance_type(self):
        return self._attendance_type

    # This function returns a customer data.
    @property
    def customer(self):
        return self._customer

    # Returns id of attendance.
    @property
    def attendance_id(self):
        return self._attendance_id

    # Allow edit service requested by customer.
    @service_type.setter
    def service_type(self, value):
        self._service_type = value
