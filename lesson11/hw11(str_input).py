from collections import UserDict
from datetime import datetime
import re


def arg_check(arg):

    date_form = re.sub("[- //]", ".", arg)
    
    try:
        data = datetime.strptime(date_form, "%d.%m.%Y")
        return data
    
    except ValueError:
        pass
    
    # phone light check
    test1 = 20 > len(arg) >= 10
    test2 = next(filter(lambda x: x.isalpha() or x in [".", ",","="], arg), False)
    
    if test1 and (not test2):
        return "phone"
    else:
        return "other"


class AddressBook(UserDict):

    def __init__(self):
        
        super().__init__()
        self.max_number = 0
        self.current_records = 0

    def __next__(self):

        if len(self.data.items()) > self.current_records:
            display_piece = list(self.data.items())[self.current_records:self.current_records + self.max_number]
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
        self.__value = value
    
    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
    
        if arg_check(value) == "phone":
            self.__value = value
        
        else:
            print("Wrong number format")


class Birthday(Field):

    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        if arg_check(value) == "birthday":
            self.__value = value

        else:
            print("Wrong birthday format")

class Record:

    def __init__(self, name, *args):

        self.name = Name(name)
        self.phone_nums = []
        self.birthday = None

        if args:
            for arg in args:
                if arg_check(arg) == "phone":
                    self.phone_nums.append(Phone(arg))
                elif isinstance(arg_check(arg), datetime):
                    if self.birthday:
                        raise ValueError("Several dates in one record")
                    else:
                        self.birthday = Birthday(arg_check(arg).date())
                else:
                    print(type(arg))
                    print(f"{arg} is not a correct value, please check your data")
                    raise ValueError("Incorrect data type")

    def __repr__(self):
        return f"{self.name}: {self.phone_nums}, {self.birthday}"

    def add_phone(self, value):

        num = next(filter(lambda x: x.value == value, self.phone_nums), None)

        if num:
            print("Number already registered")
        else:
            if arg_check(value) == "phone":
                self.phone_nums.append(Phone(value))
                print(f"Phone {value} for {self.name.value} successfully added")
            else:
                print("Wrong phone format")

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
            old_num.value = value2
            if old_num.value == value2:
                print(f"Number successfully changed to {value2}")

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


if __name__ == "__main__":

    Book1 = AddressBook()
    rec1 = Record("Dasha", "0969459910", "30.03.1995", "0969409910")

    rec2 = Record("Masha", "12/12/1995")
    rec3 = Record("Bob", "0669459910")
    rec4 = Record("Pasha", "0576783827")
    rec5 = Record("Sasha", "0669459910")
    rec6 = Record("Rob", "04567838747")
    rec7 = Record("Peter", "0586843675")

    rec1.add_phone("67583786994")
    rec1.add_phone("67583786994")

    rec1.change_phone("67583786994", "09674736465")
    rec1.change_phone("8965978576", "0kfkld09589697504")
    rec1.add_phone("000")
    rec1.change_phone("09674736465", "000")
    rec1.del_phone("00000")
    rec1.del_phone("000")

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
    Book1.iterator(2)
    Book1.iterator(2)
    Book1.iterator(3)
