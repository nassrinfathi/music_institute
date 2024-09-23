from model.entity.person import Person


class Teacher(Person):
    def __init__(self, id, name, family, national_id, phone, address, skill):
        super().__init__(id, name, family, national_id, phone, address)
        self.skill = skill

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        self._skill = skill
