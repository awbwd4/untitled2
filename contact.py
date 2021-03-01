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

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name+'\n')
        f.write(contact.phone_number+'\n')
        f.write(contact.e_mail+'\n')
        f.write(contact.addr+'\n')
    f.close()


def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines)/4 #주소록 하나당 4줄이므로 몇개의 주소록이 저장돼있는지 4로 나눠서 확인 가능
    num = int(num) #나눗셈 연산을 하면 num값이 실수형이 됨 -> 정수형으로 바꿔줌

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()




def run():
    contact_list = []
    load_contact(contact_list)
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
            store_contact(contact_list)
            break

if __name__=="__main__":
    run()