from collections import UserDict


class AddressBook(UserDict):
    
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record
        #book.append({record.name.value: record})

class Record:

    def __init__(self, name, phone = None):
        self.name = name
        self.phones = []
        if phone != None:
            self.phones.append(phone)

    def change(self, phone1, phone2):
        for i in self.phones:
            if i.value == phone1:
                i.value = phone2
                return f'Number {phone1} from {self.name}`s list changed to {phone2}'
        return f'Number {phone1} is not exist in {self.name} list'
    
    def delete(self, phone1):
        for i in self.phones:
            if i.value == phone1:
                self.phones.remove(i)
                return f'Number {phone1} deleted from {self.name}`s number list'
        return f'Number {phone1} is not exist in {self.name} list'

    def add_number(self, phone):
        for i in self.phones:
            if i.value == phone.value:
                return f'This number is already in datebase'
        self.phones.append(phone)

    def __str__(self) -> str:
        self.phones_show = None
        if len(self.phones) == 0:
            self.phones_show = 'not exist in this date base'
        elif len(self.phones) == 1:
            self.phones_show = str(self.phones[0])
        elif len (self.phones) > 1:
            self.phones_show = [*self.phones]
        return f'{self.name.value} phone(s) is {self.phones_show}'
    

class Field:
    pass

class Name(Field):
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f'{self.value}'

class Phone(Field):
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f'{self.value}'



phone_book = AddressBook()

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except TypeError:
            return 'Try to type command again'
        except IndexError:
            return 'Try to type command again!'
        except KeyError:
            return 'Try to type command again!!'
    return wrapper

def exit(*args):
    return "Good bye!"

@input_error
def add_contact(*args):
    #print(phone_book, 'before')
    for k, v in phone_book.items():
        if k == args[0]:
            return f'{args[0]} is already in list'
    name = Name(args[0])
    if len(args) != 1:
        phone = Phone(args[1])
    if len(args) == 1:
        rec = Record(name)
    else:
        rec = Record(name, phone)
    phone_book.add_record(rec)
    #print(phone_book, 'after')
    return f'Contact {name.value} added successfuly'

@input_error
def add_number(*args):
    rec = phone_book[args[0]]
    #print(rec)
    new_number = Phone(args[1])
    #print(rec.phones)
    if rec.add_number(new_number) == None:
        return f'Number {new_number.value} added to {rec.name}`s list of numbers successfuly'
    else:
        return rec.add_number(new_number)

@input_error
def change(*args): # Для change потрібно ввести Ім'я, Старий номер і Новий номер
    #print(phone_book, 'before')
    for k, v in phone_book.items():
        if k == args[0]:
            rec = phone_book[args[0]]
            return rec.change(args[1], args[2])
    return f'{args[0]} isn`t exist in list of names'

@input_error
def delete(*args): # Для delete потрібно ввести Ім'я та Номер
    for k, v in phone_book.items():
        if k == args[0]:
            rec = phone_book[args[0]]
            return rec.delete(args[1])
    return f'{args[0]} isn`t exist in list of names'

@input_error
def phone(*args):
    rec = phone_book[args[0]]
    return rec

@input_error
def show_all(*args):
    for k, v in phone_book.items():
        print(v)
    return "The list of all names and numbers showed"
    

COMMANDS = {
            exit:["good bye", "close", "exit", "."], 
            add_contact:["add contact"], 
            add_number:["add number"], 
            show_all:["show all"], 
            phone:["phone"], 
            change:["change", "change phone"], 
            delete:["delete"]
            }


def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    return 'continue', user_input


@input_error
def main():
    while True:
        user_input = input(">>>")
        result, data = parse_command(user_input)
        if result == 'continue':
            continue
        print(result(*data))
        if result is exit:
            break


if __name__ == "__main__":
    main()