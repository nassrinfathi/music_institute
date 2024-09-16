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
        self._id = id

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        self._teacher = teacher

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student):
        self._student = student

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        self._payment = payment

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score









