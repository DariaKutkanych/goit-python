from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):

        if self.data.get(record.name.value):
            print(f"User name {record.name.value} already exists")
        else:
            self.data[record.name.value] = record
            print(f"User {record.name.value} successfully added")


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Phone(Field):

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Record:

    def __init__(self, name, phone=None):

        self.name = Name(name)
        self.phone_nums = []

        if phone:
            self.phone_nums.append(Phone(phone))

    def __repr__(self):
        return f"{self.name}: {self.phone_nums}"

    def add_phone(self, value):

        num = next(filter(lambda x: x.value == value, self.phone_nums), None)

        if num:
            print("Number already registered")
        else:
            self.phone_nums.append(Phone(value))
            print(f"Phone {value} for {self.name.value} successfully added")

    def del_phone(self, value):

        num = next(filter(lambda x: x.value == value, self.phone_nums), None)
        if num:
            print(f"Phone {num.value} removed")
            self.phone_nums.remove(num)

        else:
            print("Number not registered")

    def change_phone(self, value1, value2):

        new_num_check = next(
            filter(lambda x: x.value == value2, self.phone_nums), None)
        old_num = next(filter(lambda x: x.value ==
                       value1, self.phone_nums), None)

        if not new_num_check and old_num:

            self.phone_nums.remove(old_num)
            self.phone_nums.append(Phone(value2))

            print(f"Number successfully changed to {value2}")

        else:
            print("Number not registered or a new number already exists")


if __name__ == "__main__":

    Book1 = AddressBook()
    rec1 = Record("Dasha", "0969459910")
    rec2 = Record("Masha")
    rec3 = Record("Bob", "0669459910")
    rec4 = Record("Dasha", "0669459910")

    rec1.add_phone("67583786994")
    rec1.add_phone("67583786994")

    rec1.change_phone("67583786994", "09674736465")
    rec1.change_phone("8965978576", "009589697504")
    rec1.add_phone("000")
    rec1.change_phone("09674736465", "000")
    rec1.del_phone("00000")
    rec1.del_phone("000")

    print(rec1.phone_nums)

    Book1.add_record(rec1)
    Book1.add_record(rec2)
    Book1.add_record(rec3)
    Book1.add_record(rec4)

    print(rec1)
    print(rec2)
    print(Book1.items())
