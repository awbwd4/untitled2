class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("name: ", self.name)
        print("phone_number: ",self.phone_number)
        print("e_mail: ",self.e_mail)
        print("addr: ",self.addr)



def set_contact():
    name = input("Name: ")
    phone_number = input("phone number: ")
    e_mail = input("E-mail: ")
    addr = input("addr: ")
    # print(name, phone_number, e_mail, addr)
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def run_1():
    set_contact()

def print_menu():
    print("1 연락처 입력")
    print("2 연락처 출력")
    print("3 연락처 삭제")
    print("4 종료")
    menu = input("메뉴선택 : ")
    return int(menu)
    # return menu

def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        if menu == 2:
            print_contact(contact_list)
        if menu == 3:
            name = input("삭제 대상 : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            break

if __name__=="__main__":
    run()