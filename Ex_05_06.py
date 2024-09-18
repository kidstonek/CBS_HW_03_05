"""
Завдання 6

Використовуючи код завдання 2 надрукуйте у терміналі всі методи,
які містяться у класі Contact та UpdateContact.

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

    print('methods for Contact:')
    for method in dir(Contact):
        print(method)


    print('\nmethods for UpdateContact:')
    for method in dir(UpdateContact):
        print(method)