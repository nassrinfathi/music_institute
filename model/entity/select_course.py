class SeletCourse:
    def __init__(self,id,course,teacher,student,date_time,payment,score):
        self.id = id
        self.course = course
        self.teacher = teacher
        self.student = student
        self.date_time = date_time
        self.payment = payment
        self.score= score

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = validator.id_validator(id,  'Invalid Id')

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = validator.course_validator(course, 'Invalid Course')

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        self._teacher = validator.teacher_validator(teacher, 'Invalid Teacher')

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student):
        self._student = validator.student_validator(student, 'Invalid Student')

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = validator.date_validator(date_time, 'Invalid Date')

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        self._payment = validator.payment_validator(payment, 'Invalid Payment')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = validator.score_validator(score, 'Invalid Score')


    def __repr__(self):
        return f"{self.__dict__}"






