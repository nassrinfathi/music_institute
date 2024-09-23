from tools.validator import Validator


class Person:
    def __init__(self, id, name, family, national_id, phone,address):
        self.id = id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone = phone
        self.address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, 'Invalid Name')

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.family_validator(family, 'Invalid Family')

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = Validator.national_id_validator(national_id, 'Invalid National_ID')

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = Validator.phone_validator(phone, 'Invalid Phone')

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = Validator.address_validator(address, 'Invalid Address')

    def __repr__(self):
        return f"{self.__dict__}"
