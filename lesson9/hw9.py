def input_error(func):
    def inner(*args, **kwargs):
        
        try:
            func(*args, **kwargs)
        except KeyError:
            print("Choose a correct command, please")
        except ValueError:
            print("Please enter correct number")
        except IndexError:
            print("Give me name and phone please")

    return inner

user_dict = {}

def phone_condition(data):
    
    test1 = 20 > len(data) >= 10
    test2 = next(filter(lambda x: x.isalpha(), data), False)
    
    if test1 and (not test2):
        return data        
    else:
        raise ValueError

def hello(text):
    print("How can I help you?")

def add(text, info_dict=user_dict):
    
    words = text[4:].split()
    phone = phone_condition(words.pop())
    name = " ".join(words)

    if name and not info_dict.get(name):
        info_dict[name] = phone
        print(f"{name} with phone {phone} added to database")
    
    elif info_dict.get(name):
        print("User already exists, please choose another name")

    else:
        raise IndexError

def change(text, info_dict=user_dict):
    words = text[7:].split()
    phone = phone_condition(words.pop())
    name = " ".join(words)


    if info_dict.get(name):
        info_dict[name] = phone
        print(f"Phone number for {name} changed to {phone}")
    
    else:
        print(f"User doesn't exist. Please write 'add ...' to create one")

def phone(text, info_dict=user_dict):

    name = " ".join(text.split()[1:])
    print(info_dict.get(name, "No user registered, enter correct name"))


def show_all(text, info_dict=user_dict):
    if info_dict:
        print(info_dict)
    else:
        print("Database is empty")


def good_bye(text):
    print("Good bye!")


COMMANDS = {"hello": hello, "add ": add, "change ": change,
            "phone ": phone, "show all": show_all, "good bye": good_bye, 
            "exit": good_bye, "close": good_bye}


@input_error
def handler(text):
    command = next(filter(lambda x: text.lower().startswith(x), COMMANDS.keys()), None)
    return COMMANDS[command](text)


def main():

    break_words = ["."]

    while True:

        message = input("Your message: ")

        if message not in break_words:
            handler(message)
        else:
            break

if __name__== "__main__":
    
    main()
