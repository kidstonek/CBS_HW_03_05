"""
Завдання 5

Використовуючи код завдання 2 надрукуйте у терміналі інформацію,
яка міститься у класах Contact та UpdateContact та їх екземплярах.
Видаліть атрибут job, і знову надрукуйте стан класів та їх
екземплярів. Порівняйте їх. Зробіть відповідні висновки.
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
    print(dir(Contact))
    print(dir(UpdateContact))
    contact1 = Contact('Petrosky', 'Fedir', 40, '+380971233243', 'pet.fed@gmail.com')
    upd_contact1 = UpdateContact('Fedoriv', 'Ilya', 24, '+380974562312', 'ilyafed@gmail.com', 'lawyer')

    print(' __dict__')
    print(f'for Contact - {contact1.__dict__}')
    print(f'for UpdateContact - {upd_contact1.__dict__}')

    print(f'was {upd_contact1.__dir__()}')
    delattr(upd_contact1, 'job')
    print(f'become {upd_contact1.__dir__()}')

    print(dir(Contact))
    print(dir(UpdateContact))