"""
Завдання 3

Використовуючи код з завдання 2,
використати функції hasattr(), getattr(), setattr(), delattr().
Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
"""


class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str) -> None:
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f'{self.name} has mobile {self.mob_phone} and email {self.email}'

    def sent_message(self):
        return f'the message was sent trough email {self.email}'


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str, job) -> None:
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f'messages from the number {self.mob_phone}'



if __name__ == '__main__':
    contact1 = Contact('Petrosky', 'Fedir', 40, '+380971233243', 'pet.fed@gmail.com')
    upd_contact1 = UpdateContact('Fedoriv', 'Ilya', 24, '+380974562312', 'ilyafed@gmail.com', 'lawyer')
    print('hasattr()')
    print(hasattr(contact1,'surname'))
    print(hasattr(upd_contact1, 'get_message'))
    print('getattr()')
    print(getattr(upd_contact1, 'get_contact'))
    print(getattr(upd_contact1, 'name'))
    print('setattr()')
    print(f'was {contact1.__dict__}')
    setattr(contact1, 'name', 'New_name')
    print(f'become {contact1.__dict__}')
    print('delattr()')
    print(f'was {upd_contact1.__dict__}')
    delattr(upd_contact1, 'job')
    print(f'become {upd_contact1.__dict__}')


