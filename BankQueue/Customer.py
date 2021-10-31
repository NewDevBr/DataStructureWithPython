from datetime import date


class Customer:

    def __init__(self, cpf, full_name, born_date, has_especial_necessity):
        self._cpf = cpf
        self._full_name = full_name
        self._born_date = born_date
        self._has_especial_necessity = has_especial_necessity

    # Getter cpf. It's have no setter because it's
    # can't be changed during processing.
    @property
    def cpf(self):
        return self._cpf

    # Getter full name.
    @property
    def full_name(self):
        return self._full_name

    # Setter full name.
    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    # Getter born_date.
    @property
    def born_date(self):
        return self._full_name

    # It's sets a date value.
    @born_date.setter
    def born_date(self, value):
        self._born_date = value

    # It's used to know if customer has another especial
    # necessity beyond advanced age. Know if customer is
    # a pregnant woman, have little children or is lactating,
    # is obese or have another deficiency
    @property
    def has_especial_necessity(self):
        return self._has_especial_necessity

    # It's sets a boolean var that helps know if customer
    # has especial necessities.
    @has_especial_necessity.setter
    def has_especial_necessity(self, value):
        self._has_especial_necessity = value

    # This function calculates and return age of customer.
    # It treat cases that customers born in a leap year.
    # It's used to define attendance treat.
    @property
    def age(self):
        today = date.today()
        try:
            birthday = self._born_date.replace(year=today.year)
        except ValueError:
            birthday = self._born_date.replace(year=today.year, mouth=self._born_date.mouth + 1, day=1)
        if birthday > today:
            years_old = today.year - self._born_date.year - 1
        else:
            years_old = today.year - self._born_date.year
        return years_old
