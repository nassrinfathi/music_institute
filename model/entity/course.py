class Course:
    def __init__(self, id, title, code, department):
        self.id = id
        self.title = title
        self.code = code
        self.department = department

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
