def print_menu():
    print("Welcome:")
    print("A - add new entry")
    print("P - print all entries")
    print("D - delete one entry")
    print("Q - quit")


def print_people(people):
    name_list = list(people)
    for i in name_list:
        print(f"Surname: {i}, Name: {people[i][0]}, phone number: {people[i][1]}")


def delete_one_entry(people):
    while True:
        surname = input("Write a surname of person you want to delete from address book -> ")
        name_list = list(people)
        if surname in name_list:
            print(f"Deleted: surname: {surname}, Name: {people[surname][0]}, phone number: {people[surname][1]}")
            people.pop(surname)
            break
        else:
            print("There is no with given surname in the address book")
        action = input("Do you want to try again? y/n: ")
        if action == 'n':
            break
    return people


def get_surname(people):
    while True:
        surname = input("Write surname -> ")
        if surname in people:
            print("There already is an entry with given surname")
        else:
            break
    surname = surname.capitalize()
    return surname


def get_name():
    name = input("Write name -> ")
    name = name.capitalize()
    return name


def get_phone_number(people):
    while True:
        phone_number = int(input("Write phone number -> "))
        already_in = 0
        people_list = list(people)
        for x in people_list:
            if people[x][1] == phone_number:
                already_in = 1
                break
        if already_in:
            print("Given phone number belongs to someone else")
        elif len(str(phone_number)) != 9:
            print("Given phone number does not contain 9 digits")
        else:
            break
    return phone_number


def add_new_entry(people):
    surname = get_surname(people)
    name = get_name()
    phone_number = get_phone_number(people)
    people[surname] = [name, phone_number]
    return people


def menu(people):
    while True:
        print_menu()
        match input():
            case 'A':
                people = add_new_entry(people)
            case 'P':
                print_people(people)
            case 'D':
                people = delete_one_entry(people)
            case 'Q':
                break
            case _:
                print("Error, option you chose is not implemented yet")


def main_init(people):
    people["Przybylski"] = ["Martin", 123456789]
    people["Wróblewski"] = ["Jan", 987654321]
    people["Górecki"] = ["Ryszard", 123123123]
    people["Sokołowska"] = ["Amelia", 333444555]
    people["Borkowska"] = ["Paula", 999111222]
    return people


def main():
    people = dict()
    people = main_init(people)
    menu(people)


main()
