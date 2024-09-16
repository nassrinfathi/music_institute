class Student:
    def __init__(self,id, name,family,national_id,phone,address):
        self.id = id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone = phone
        self.address=address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = national_id

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address


    def __repr__(self):
        return f"{self.__dict__}"

