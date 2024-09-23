class Payment:
    def __init__(self, id, select_course, amount, description):
        self.id = id
        self.selectCourse = select_course
        self.amount = amount
        self.description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = validator.id_validator(id, 'Invalid Id')

    @property
    def select_course(self):
        return self._select_course

    @select_course.setter
    def select_course(self, select_course):
        self._select_course = validator.select_course_validator(select_course, 'Invalid Select course')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = validator.amount_validator(amount, 'Invalid Amount')

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = validator.description_validator(description, 'Invalid description')


    def __repr__(self):
        return f"{self.__dict__}"