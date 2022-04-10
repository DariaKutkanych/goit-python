from collections import UserDict
from copyreg import pickle
from datetime import datetime
import re
import pickle


class AddressBook(UserDict):

    def __init__(self):

        super().__init__()
        self.max_number = 0
        self.current_records = 0

    def __next__(self):

        if len(self.data.items()) > self.current_records:
            display_piece = list(self.data.items())[
                self.current_records:self.current_records + self.max_number]
            self.current_records = self.current_records + self.max_number

            return display_piece
        else:
            print("No more data")
            raise StopIteration

    def __iter__(self):
        return self

    def add_record(self, record):

        if self.data.get(record.name.value):
            print(f"User name {record.name.value} already exists")
        else:
            self.data[record.name.value] = record
            print(f"User {record.name.value} successfully added")

    def iterator(self, number):
        self.max_number = number

        for rec in self:
            print(rec)
            return rec

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def save_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    def open_instance(self, file_name):
        with open(file_name, "rb") as file:
            return pickle.load(file)

    def quick_search(self, text):
        result = []
        for user in self.data.values():
            if text in user.name.value or [phone for phone in user.phone_nums if text in phone.value]:
                result.append(user)
        return result, text


class Field:

    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        test1 = 20 > len(value) >= 10
        test2 = next(filter(lambda x: x.isalpha() or x in [
                     ".", ",", "="], value), False)

        if test1 and (not test2):
            self.__value = value
        else:
            print("Wrong data format")


class Birthday(Field):

    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        date_form = re.sub("[- //]", ".", value)

        try:
            bd = datetime.strptime(date_form, "%d.%m.%Y").date()
            self.__value = bd

        except ValueError:
            print("Wrong birthday format")


class Record:

    def __init__(self, name, phones=[], birthday=None):

        self.name = name
        self.phone_nums = [phone for phone in phones if phone.value != None]
        self.birthday = None

        if birthday and (birthday.value != None):
            self.birthday = birthday

    def __repr__(self):
        return f"{self.name}: {self.phone_nums}, {self.birthday}"

    def add_phone(self, phone):

        if phone.value:
            num = next(filter(lambda x: x.value ==
                              phone.value, self.phone_nums), None)
            if num:
                print("Number already registered")
            else:
                self.phone_nums.append(phone)
                print(
                    f"Phone {phone.value} for {self.name.value} successfully added")
        else:
            print("Wrong format")

    def del_phone(self, phone):

        num = next(filter(lambda x: x.value ==
                   phone.value, self.phone_nums), None)

        if num:
            print(f"Phone {num.value} removed")
            self.phone_nums.remove(num)

        else:
            print("Number not registered")

    def change_phone(self, ph1, ph2):

        new_num_check = next(
            filter(lambda x: x.value == ph2.value, self.phone_nums), None)
        old_num = next(filter(lambda x: x.value ==
                       ph1.value, self.phone_nums), None)

        if not new_num_check and old_num:
            self.phone_nums.append(ph2)
            self.phone_nums.remove(old_num)
            print(f"Number successfully changed to {ph2.value}")

        else:
            print("Number not registered or a new number already exists")

    def days_to_birthday(self):

        if self.birthday:
            cur_day = datetime.today().date()
            cur_bd_year = self.birthday.value.replace(year=cur_day.year)

            if cur_day > cur_bd_year:
                cur_bd_year = cur_bd_year.replace(year=cur_day.year+1)

            days_left = (cur_bd_year - cur_day).days

            print(f"{days_left} days to your next birthday")
            return (cur_bd_year - cur_day).days
        else:
            print("Sorry we don't know your birthday")

        def __getstate__(self):
            attributes = self.__dict__.copy()
            return attributes

        def __setstate__(self, value):
            self.__dict__ = value


if __name__ == "__main__":

    Book1 = AddressBook()

    name1 = Name("Dasha")
    name2 = Name("Masha")
    name3 = Name("Sasha")
    name4 = Name("Pasha")
    name5 = Name("Kasha")
    name6 = Name("Bob")
    name7 = Name("Rob")

    p1 = Phone("0969459910")
    p2 = Phone("694510")
    p3 = Phone("+380969459910")
    p4 = Phone("0969459910")
    p5 = Phone("0969459910")
    p6 = Phone("0969459911")
    p7 = Phone("0fmglr459910")
    p8 = Phone("67583786994")

    bd1 = Birthday("28.12.1995")
    bd2 = Birthday("28.11.1985")
    bd3 = Birthday("28/11/1985")
    bd4 = Birthday("31/02/1985")

    rec1 = Record(name1, [p1, p2, p3],  bd1)

    rec2 = Record(name2, [p2], bd4,)
    rec3 = Record(name3, birthday=bd3)
    rec4 = Record(name4, phones=[p4])
    rec5 = Record(name5, phones=[p7])
    rec6 = Record(name6, [p2], bd2)
    rec7 = Record(name7, [p2], bd2, )
    rec8 = Record(name1, [p2, p1, p3], bd4)

    rec1.add_phone(p8)
    rec1.add_phone(p8)

    rec1.change_phone(p8, p6)
    rec1.change_phone(p3, p6)
    rec1.add_phone(p2)
    rec1.del_phone(p4)
    rec1.del_phone(p1)

    print(rec1.phone_nums)
    print(f"\n-----------------------\n")

    Book1.add_record(rec1)
    Book1.add_record(rec2)
    Book1.add_record(rec3)
    Book1.add_record(rec4)
    Book1.add_record(rec5)
    Book1.add_record(rec6)
    Book1.add_record(rec7)
    Book1.add_record(rec1)

    print(rec1)
    print(rec2)
    print(Book1.items())

    print(f"\n-----------------------\n")

    rec1.days_to_birthday()
    rec2.days_to_birthday()
    rec3.days_to_birthday()

    print(f"\n-----------------------\n")
    Book1.iterator(4)


print(f"\n-----------------------\n")


Book1.save_to_file("check.bin")

Book1 = Book1.open_instance("check.bin")

print(Book1.data["Bob"].birthday)

print(Book1.quick_search("asha"))
print(Book1.quick_search("Masha"))
print(Book1.quick_search("096"))
print(Book1.quick_search("ob"))
