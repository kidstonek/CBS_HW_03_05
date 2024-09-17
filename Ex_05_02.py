""""Завдання 2

Створити клас Contact з полями surname, name, age, mob_phone, email.
Додати методи get_contact, sent_message.
Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone,
email, job. Додати методи get_message.
Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів:
 __dict__, __base__, __bases__.
 Роздрукувати інформацію на екрані."""


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
    print(' __dict__')
    print(f'for Contact - {contact1.__dict__}')
    print(f'for UpdateContact - {upd_contact1.__dict__}')
    print('__base__')
    print(f'for Contact - {Contact.__base__}')
    print(f'for UpdateContact - {UpdateContact.__base__}')
    print('__bases__')
    print(f'for Contact - {Contact.__bases__}')
    print(f'for UpdateContact - {UpdateContact.__bases__}')
