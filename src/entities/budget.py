class Budget:
    """
    A class representing a Budget object of a user.
    """

    def __init__(self, user: str,
                 amount: float,
                 category: str,
                 date: str,
                 tag: str = None,
                 budget_id: int = None):
        self._id = budget_id
        self._user = user
        self._amount = amount
        self._category = category
        self._date = date
        self._tag = tag

    @property
    def id(self):
        return self._id

    @property
    def user(self):
        return self._user

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def date(self):
        return self._date

    @property
    def tag(self):
        return self._tag

    def add_income(self, income):
        self._amount += income

    def __eq__(self, other):
        if not isinstance(other, Budget):
            return False
        return (
            self._user == other._user and
            self._amount == other._amount and
            self._category == other._category and
            self._date == other._date
        )

    def __repr__(self):
        return f"Budget({self._user}, {self._amount}, {self._category}, {self._date}, {self._tag})"
