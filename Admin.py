import json


########## CLASS BOOK #####################################################################

class Book():
    def __init__(self):
        self.id = int(),
        self.name = str(),
        self.author = str(),
        self.copies = int(),
        self.lended_to = list()

    def add_book(self):
        self.name = str(input("Enter the Book Title: ")).lower()
        self.author = str(input("Enter the Author Name: ")).lower()
        self.copies = is_valid_copies(input("Enter the no of Copies: "))
        books = file_to_data('books')
        flag = 0
        for i in books:
            if i['name'] == self.name and i['author'] == self.author:
                flag += 1
        if flag == 0:
            add_book_to_data(self)
        else:
            print("Book already present, Try increasing the no of copies!")

    def show_book_details(self):
        print(self.id)
        print(self.name)
        print(self.author)
        print(self.copies)
        print(self.lended_to)

    def modify_book(self):
        books = file_to_data('books')
        flag = 0
        for i in books:
            if i["id"] == self.id:
                flag += 1
        if flag == 1:
            while (True):
                ch = is_valid_choice(input("1.Name\n2.Author\n3.No of Copies\n4.Previous Menu\n5.Exit\n"))
                if ch == 1:
                    new = str(input("Enter the New Book Name: ")).lower()
                    self.name = new
                    modify_book_in_data(self)
                elif ch == 2:
                    new = str(input("Enter the New Author Name: ")).lower()
                    self.author = new
                    modify_book_in_data(self)
                elif ch == 3:
                    new = is_valid_copies(input("Enter the Extra No. of Copies: "))
                    self.copies += new
                    modify_book_in_data(self)
                elif ch == 4:
                    book()
                elif ch == 5:
                    exit()
                else:
                    print("Invalid Input ")
                    self.modify_book()
        else:
            print("The Id you entered doesn't belong to any book in library!")
            return 0

    def delete_book(self):
        delete_book_from_data(self)


###########################################################################################


##########STUDENT CLASS####################################################################

class Student():
    def __init__(self):
        self.id = int(),
        self.sic = str(),
        self.name = str(),
        self.phone = str(),
        self.email = str(),
        self.books_issued = list()

    def add_student(self):
        students = file_to_data('students')
        sic = input("Enter the Student's SIC: ")
        sic = is_valid_sic(sic)
        flag=0
        for i in students:
            if i['sic'] == sic:
                flag += 1
        if flag == 0:
            self.sic = sic
            self.name = input("Enter the Student's Name: ")
            phone = input("Enter the Student's Phone No.: ")
            phone = is_valid_phone(phone)
            self.phone = phone
            email = input("Enter the Student's Email Id.: ")
            email = is_valid_email(email)
            self.email = email
            self.books_issued = []
            add_student_to_data(self)
        else:
            print("Student already present!!")

    def show_student_details(self):
        print(self.id)
        print(self.sic)
        print(self.name)
        print(self.phone)
        print(self.email)
        print(self.books_issued)

    def modify_student(self):
        while (True):
            ch = is_valid_choice(input(
                "Opt for the option you want to modify:\n1.SIC \n2.Name \n3.Phone No.\n4.Email Id.\n5.Previous Menu\n6.Exit\n"))
            if ch == 1:
                sic = input("Enter the New Student's SIC: ")
                sic = is_valid_sic(sic)
                self.sic = sic
                modify_student_in_data(self)
                student()
            elif ch == 2:
                self.name = input("Enter the Student's New Name: ")
                modify_student_in_data(self)
            elif ch == 3:
                phone = input("Enter Student's new phone no.: ")
                phone = is_valid_phone(phone)
                self.phone = phone
                modify_student_in_data(self)
            elif ch == 4:
                email = str(input("Enter the New Student's Email Id.: ")).lower()
                email = is_valid_email(email)
                self.email = email
                modify_student_in_data(self)
            elif ch == 5:
                student()
            elif ch == 6:
                exit()
            else:
                print("Invalid Input, Try again: ")
                self.modify_student()


    def delete_student(self):
        delete_student_from_data(self)


###########################################################################################

def file_to_data(key):
    if key == 'books':
        f = open('books.json', 'r')
        books = json.load(f)
        f.close()
        return books
    elif key == 'students':
        f = open('students.json', 'r')
        students = json.load(f)
        f.close()
        return students
    elif key == 'admins':
        f = open('admins.json', 'r')
        admins = json.load(f)
        f.close()
        return admins
    else:
        print("Invalid Key")


##########PRESENT DATA ON SCREEN###########################################################

def show_all_students():
    students = file_to_data('students')
    s = json.dumps(students, indent=2)
    print(s)


def show_all_books():
    books = file_to_data('books')
    s = json.dumps(books, indent=2)
    print(s)


def book_lended_to(bid):
    books = file_to_data('books')
    ch = 0
    for i in books:
        if i["id"] == bid:
            ch = 1
    if ch == 1:
        students = file_to_data('students')
        if len(books[bid - 1]["lended_to"])>0:
            for i in books[bid - 1]["lended_to"]:
                for j in students:
                    if i["sic"] == j["sic"]:
                        stud = dict_to_student(j)
                        stud.show_student_details()
                    else:
                        continue
        else:
            print("This book hasn't been issued by any student yet!")
    else:
        print("The Book Id you entered doesn't belong to a valid Book in Library")



##########################################################################################

##########ADD/DELETE/MODIFY DATA IN DATABASE###############################################

def modify_student_in_data(objct):
    students = file_to_data('students')
    d = student_to_dict(objct)
    students[objct.id - 1] = d
    f = open('students.json', 'w')
    json.dump(students, f, indent=2)
    f.close()
    print("Student's details successfully modified in Database!")
    return 0


def modify_book_in_data(objct):
    books = file_to_data('books')
    d = book_to_dict(objct)
    books[objct.id - 1] = d
    f = open('books.json', 'w')
    json.dump(books, f, indent=2)
    f.close()
    print("Book's details successfully modified in Database!")
    return 0


def add_book_to_data(objct):
    books = file_to_data('books')
    objct.id = len(books) + 1
    d = book_to_dict(objct)
    books.append(d)
    f = open('books.json', 'w')
    json.dump(books, f, indent=2)
    f.close()
    print("Book successfully added to Database!")
    return 0


def add_student_to_data(objct):
    students = file_to_data('students')
    objct.id = len(students) + 1
    d = student_to_dict(objct)
    students.append(d)
    f = open('students.json', 'w')
    json.dump(students, f, indent=2)
    f.close()
    print("Student successfully added to Database!")
    return 0


def delete_book_from_data(objct):
    books = file_to_data('books')
    if len(books) > 0:
        books.pop(objct.id - 1)
        for i in range(objct.id - 1, len(books)):
            books[i]['id'] -= 1
        f = open('books.json', 'w')
        json.dump(books, f, indent=2)
        f.close()
        print("Book successfully deleted from Database!")
        return 0
    else:
        print("No Books in Library!")


def delete_student_from_data(objct):
    students = file_to_data('students')
    if len(students) > 0:
        students.pop(objct.id - 1)
        for i in range(objct.id - 1, len(students)):
            students[i]['id'] -= 1
        f = open('students.json', 'w')
        json.dump(students, f, indent=2)
        f.close()
        print("Student successfully deleted from Database!")
        return 0
    else:
        print("No Students in Library!")




##########################################################################################

##########Convert OBJECT<--->DICTIONARY###################################################

def book_to_dict(objct):
    d = {
        'id': int(objct.id),
        'name': str(objct.name),
        'author': str(objct.author),
        'copies': int(objct.copies),
        'lended_to': list(objct.lended_to)
    }
    return d


def student_to_dict(objct):
    d = {
        'id': int(objct.id),
        'sic': str(objct.sic),
        'name': str(objct.name),
        'phone': str(objct.phone),
        'email': str(objct.email),
        'books_issued': list(objct.books_issued)
    }
    return d


def dict_to_book(d):
    ob = Book()
    ob.id = int(d['id'])
    ob.name = str(d['name'])
    ob.author = str(d['author'])
    ob.copies = int(d['copies'])
    ob.lended_to = list(d['lended_to'])
    return ob


def dict_to_student(d):
    ob = Student()
    ob.id = int(d['id'])
    ob.sic = str(d['sic'])
    ob.name = str(d['name'])
    ob.phone = str(d['phone'])
    ob.email = str(d['email'])
    ob.books_issued = list(d['books_issued'])
    return ob


###########################################################################################

##########Issue Book Function##############################################################

def issue_book(sid):
    students = file_to_data('students')
    bid = is_valid_index(input("Enter the index of the Book to be issued: "))
    books = file_to_data('books')
    z=0
    for i in books:
        if i["id"]==bid:
            z+=1
    if z==1:
        b = dict_to_book(books[bid - 1])
        s = dict_to_student(students[sid - 1])
        # Conditions for book issue
        if b.copies > 0:
            nobi = len(s.books_issued)
            if nobi <= 1:
                flag = 0
                for i in s.books_issued:
                    if int(i['id']) != int(b.id):
                        flag += 1
                # Issue book here
                if flag == nobi:
                    bidict = {"id": b.id, "name": b.name, "author": b.author}
                    l2dict = {"sic": s.sic}
                    b.copies = int(b.copies) - 1
                    b.lended_to.append(l2dict)
                    s.books_issued.append(bidict)
                    print("Book '%s' is successfully issued to SIC~'%s' Name~'%s'." %(str(b.name).capitalize(),s.sic,s.name))

                    # Adding to database
                    b_dict = book_to_dict(b)
                    s_dict = student_to_dict(s)
                    books[bid - 1] = b_dict
                    students[sid - 1] = s_dict
                    f1 = open('books.json', 'w')
                    f2 = open('students.json', 'w')
                    json.dump(books, f1, indent=2)
                    json.dump(students, f2, indent=2)
                    f1.close()
                    f2.close()
                else:
                    print("You have already issued this book!")
            else:
                print("More than two books can't be issued!")
        else:
            print("This Book isn't available anymore, Sorry!")
    else:
        print("The Book Id you entered doesn't belong to a valid Book in Library")





###########################################################################################


##########Return Book Function#############################################################

def return_book(sid):
    students=file_to_data('students')
    books = file_to_data('books')
    s = dict_to_student(students[sid - 1])
    for i in range(0, len(s.books_issued)):
        print("%s for %s" % (i + 1, s.books_issued[i]))
    if len(s.books_issued)>0:
        choice = is_valid_choice(input("Enter your choice: "))
    else:
        choice=0
    if choice <= len(s.books_issued) and choice!=0:
        flag = 0
        for i in books:
            if int(s.books_issued[choice - 1]["id"]) == int(i["id"]) and str(s.books_issued[choice - 1]["name"]) == str(i["name"]) and str(s.books_issued[choice - 1]["author"]) == str(i["author"]):
                bid = int(i["id"])
                flag+=1
        if flag == 1:
            b = dict_to_book(books[bid - 1])
            for j in b.lended_to:
                if str(j["sic"]) == str(s.sic):
                    choice2 = b.lended_to.index(j) + 1
            b.copies = int(b.copies)
            b.copies += 1
            s.books_issued.pop(choice - 1)
            b.lended_to.pop(choice2 - 1)
            b_dict = book_to_dict(b)
            s_dict = student_to_dict(s)
            print("Book '%s' is returned successfully by SIC~'%s' Name~'%s'."%(str(b.name).capitalize(),s.sic,s.name))
            books[bid - 1] = b_dict
            students[sid - 1] = s_dict
            f1 = open('books.json', 'w')
            f2 = open('students.json', 'w')
            json.dump(books, f1, indent=2)
            json.dump(students, f2, indent=2)
            f1.close()
            f2.close()

        else:
            print("Returned book isn't in Library, Registering new book!")
            b_issued = s.books_issued[choice - 1]
            b = Book()
            b.id = len(books) + 1
            b.name = b_issued["name"]
            b.author = b_issued["author"]
            b.copies = 1
            b.lended_to = []
            s.books_issued.pop(choice - 1)
            # Adding file to database
            b_dict = book_to_dict(b)
            books.append(b_dict)
            print("Book '%s' successfully returned by SIC~'%s' Name~'%s'."%(str(b.name).capitalize(),s.sic,s.name))
            s_dict = student_to_dict(s)
            students[sid - 1] = s_dict
            f1 = open('books.json', 'w')
            f2 = open('students.json', 'w')
            json.dump(books, f1, indent=2)
            json.dump(students, f2, indent=2)
            f1.close()
            f2.close()
    elif choice==0:
        print("This Student hasn't issued any book yet!")
    else:
        print("Invalid Choice, Try Again!")


##########################################################################################

########## CHECK VALIDITY OF SIC/PHONE/EMAIL ###############################################


def is_valid_sic(sic):
    while True:
        c = 0
        for i in sic:
            if i >= '0' and i <= '9' and sic[0] != '0':
                c += 1
        if c == 9:
            check=True
        else:
            check=False
        if check==True:
            return str(sic)
        else:
            sic = str(input("Enter valid SIC No."))

def is_valid_phone(phone):
    while True:
        c = 0
        for i in phone:
            if i >= '0' and i <= '9' and phone[0] != '0':
                c += 1
        if c == 10:
            check=True
        else:
            check=False
        if check==True:
            return str(phone)
        else:
            phone = str(input("Enter valid Phone no.: "))

def is_valid_email(email):
    while True:
        at = 0
        al = 0
        dig=0
        dot= 0
        alpha=[]
        for i in email:
            if i == '@':
                at+=1
            elif i.isalpha():
                al+=1
                alpha.append(i)
            elif i.isnumeric():
                dig+=1
            elif i=='.':
                dot+=1
            s=str(alpha)
        if (at+al+dig+dot) == len(email) and at == 1 and dot == 1 and s.islower():
            check = True
        else:
            check = False

        if check:
            return str(email)
        else:
            email = input("Enter valid Email Id.: ")


def is_valid_password(p):
    while True:
        salpha = 0
        calpha = 0
        dig = 0
        schar = 0
        other = 0
        if len(p) >= 6 and len(p) <= 12:
            for i in p:
                if i >= 'a' and i <= 'z':
                    salpha += 1
                elif i >= 'A' and i <= 'Z':
                    calpha += 1
                elif i >= '0' and i <= '9':
                    dig += 1
                elif i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '&':
                    schar += 1
                else:
                    other += 1
            if salpha >= 1 and calpha >= 1 and dig >= 1 and schar >= 1 and other == 0:
                return str(p)
            else:
                if salpha < 1:
                    print("Enter atleast 1 lower case character!")
                    p = input("Enter valid password: ")
                elif calpha < 1:
                    print("Enter atleast 1 upper case character!")
                    p = input("Enter valid password: ")
                elif dig < 1:
                    print("Enter atleast 1 digit!")
                    p = input("Enter valid password: ")
                elif schar < 1:
                    print("Enter atleast 1 special character from (!,@,#,$,%,&)!")
                    p = input("Enter valid password: ")
                elif other > 0:
                    print(
                        "Entered password contains character which can't be used!\nOnly Upper Case, Lower Case, Digit and special character(!,@,#,$,%,&) can be used.")
                    p = input("Enter valid password: ")
                else:
                    print("Invalid password Try again:")
                    p = input("Enter valid password: ")
        elif len(p) < 6:
            print("Password is too small!!")
            p = input("Enter valid password: ")
        else:
            print("Password is too big!!")
            p = input("Enter valid password: ")


def is_valid_username(u):
    admins=file_to_data('admins')
    while True:
        c = 0
        for i in u:
            if i.isalnum() == True or i == '_':
                c += 1
        flag=0
        for i in admins:
            if str(i[0])==str(u):
                flag+=1
        if c == len(u):
            if flag==0:
                return str(u)
            else:
                print("This UserName is already taken!")
                u=input("Try again-> ")
        else:
            u = input("Enter valid UserName containing alphanumeric values and underscore only! : ")

def is_valid_choice(c):
    while True:
        if c.isnumeric()==True:
            return int(c)
        else:
            c=input("Comeon!! Choice is an Integer!")



def is_valid_index(i):
    while True:
        if i.isnumeric()==True:
            return int(i)
        else:
            i=input("Comeon!! Id is an Integer")

def is_valid_copies(c):
    while True:
        if c.isnumeric() == True:
            return int(c)
        else:
            c=(input("Comeon!! No. of copies is an Integer! "))



###########################################################################################


def sic_to_index(sic,key):
    students = file_to_data('students')
    i=0
    for counter in students:
        if counter['sic'] == sic:
            c = int(counter['id'])
            i+=1
    if i>0:
        return c
    else:
        print("The SIC you entered doesn't belong to a valid student")
        if key == 's':
            student()
        elif key == 'l':
            librarian()
        else:
            print("Invalid key")


def main():
    while (True):
        c = is_valid_choice(input("1.Librarian\n2.Admin\n3.Exit\n"))
        if c == 1:
            librarian()
        elif c == 2:
            admin(0)
        elif c == 3:
            exit()
        else:
            print("Invalid Input,Try Again: ")
            main()


def login():
    u = auth_user(input("USERNAME: "))
    p = input("PASSWORD: ")
    if p == u[1]:
        return True
    else:
        return False


def auth_user(username):
    admins = file_to_data('admins')
    while True:
        flag = 0
        for i in admins:
            if i[0] == username:
                flag = 1
                j = i
        if flag == 1 and username!='superuser':
            return j
        else:
            username = input("Enter Valid UserName: ")



def add_admin():
    admins = file_to_data('admins')
    user = auth_user(input("Reverify your Username: "))
    password = input("Reverify your Password: ")
    if password == user[1]:
        if user[2] == 'superuser' and admins.index(user) == 0:
            print("**UserName should be alphanumeric or may contain underscore**")
            print(
                "**Password should contain atleast One Uppercase, One Lowercase,** \n**One Digit and One Special character from(!,@,#,$,%,&)**")
            u = is_valid_username(str(input("USERNAME: ")))
            p = is_valid_password(str(input("PASSWORD: ")))
            n = str(input("Enter the Name of Administrator: ")).lower()
            if n!='superuser':
                newadmin = list()
                newadmin.append(u)
                newadmin.append(p)
                newadmin.append(n)
                admins.append(newadmin)
                f = open('admins.json', 'w')
                json.dump(admins, f, indent=2)
                f.close()
                print("Admin '%s' added successfully!"%(n.upper()))
            else:
                print("This Name 'SUPERUSER' is Reserved! Try Again->")

        else:
            print("Privileges restricted to *SuperUser ONLY!*")
            return 0
    else:
        print("Login Failed, Invalid Credentials!!")
        print("For security reasons you have been redirected to *HomeMenu*")
        print("Please Start Again!!")
        main()


def delete_admin():
    admins=(file_to_data('admins'))
    user=auth_user(input("Reverify your Username: "))
    password=input("Reverify your Password: ")
    if password==user[1]:
        if user[2]=='superuser':
            u=input("Enter the UserName of the Admin to be deleted: ")
            n=input("Enter the Name of the Admin to be deleted: ").lower()
            flag=0
            for i in admins:
                if n==i[2] and u==i[0]:
                    flag+=1
                    j=admins.index(i)
            if flag==1:
                admins.pop(j)
                f = open('admins.json', 'w')
                json.dump(admins, f, indent=2)
                f.close()
                print("Admin '%s' deleted successfully!"%(n.upper()))
            else:
                print("No Admin with such Name and UserName combination found!")
                return 0
        else:
            print("Privileges restricted to *SuperUser ONLY!*")
            return 0
    else:
        print("Login Failed, Invalid Credentials!!")
        print("For security reasons you have been redirected to *HomeMenu*")
        print("Please Start Again!!")
        main()


def admin(key):
    if key == 1:
        k = True
    else:
        k = bool(login())
    if k == True:
        print("Login Successful! ")
        while (True):
            c = is_valid_choice(input(
                "1.Add/Delete/Modify BOOKS\n2.Add/Delete/Modify STUDENTS\n3.List of BOOKS\n4.List of STUDENTS\n5.Add ADMIN\n6.Delete ADMIN\n7.Previous Menu\n8.Exit\n"))
            if c == 1:
                book()
            elif c == 2:
                student()
            elif c == 3:
                show_all_books()
            elif c == 4:
                show_all_students()
            elif c == 5:
                add_admin()
            elif c == 6:
                delete_admin()
            elif c == 7:
                main()
            elif c == 8:
                exit()
            else:
                print("Invalid Input, Try Again: ")
                admin(1)
    elif k == False:
        print("Wrong Password, Try Logging in Again! ")
        main()
    else:
        print("Error")
        exit()


def book():
    while (True):
        c = is_valid_choice(input("1.Add Book\n2.Delete Book\n3.Modify Book\n4.Previous Menu\n5.Exit\n"))
        if c == 1:
            b = Book()
            b.add_book()
        elif c == 2:
            books = file_to_data('books')
            bid = is_valid_index(input("Enter the Id of the Book to be deleted: "))
            f = 0
            for i in books:
                if i['id'] == bid:
                    f = 1
            if f == 1:
                b = dict_to_book(books[bid - 1])
                b.delete_book()
            else:
                print("No Book with such Id present!")
        elif c == 3:
            books = file_to_data('books')
            bid = is_valid_index(input("Enter the Index of the Book to be modified: "))
            f = 0
            for i in books:
                if i['id'] == bid:
                    f = 1
            if f == 1:
                b = dict_to_book(books[bid - 1])
                b.modify_book()
            else:
                print("No Book with such Id present!")
        elif c == 4:
            admin(1)
        elif c == 5:
            exit()
        else:
            print("Invalid Input, Try Again: ")
            book()


def student():
    while (True):
        c = is_valid_choice(input("1.Add Student\n2.Delete Student\n3.Modify Student\n4.Previous Menu\n5.Exit\n"))
        if c == 1:
            s = Student()
            s.add_student()
        elif c == 2:
            students = file_to_data('students')
            sic = is_valid_sic(input("Enter the sic of the Student to be Deleted: "))
            sid = sic_to_index(sic,'s')
            s = dict_to_student(students[sid - 1])
            s.delete_student()

        elif c == 3:
            students = file_to_data('students')
            sic = is_valid_sic(input("Enter the sic of the Student to be Modified: "))
            sid = sic_to_index(sic,'s')
            s = dict_to_student(students[sid - 1])
            s.modify_student()
        elif c == 4:
            admin(1)
        elif c == 5:
            exit()
        else:
            print("Invalid Input, Try Again: ")
            student()


def librarian():
    while True:
        c = is_valid_choice(input("1.List Of Books\n2.Issue Book\n3.Return Book\n4.Books issued to\n5.Book lended to\n6.Previous Menu\n7.Exit\n"))
        if c == 1:
            show_all_books()
        elif c == 2:
            sic = is_valid_sic(input("Enter the SIC of the Student who wants to issue: "))
            sid=sic_to_index(sic,'l')
            issue_book(sid)
        elif c == 3:
            sic = is_valid_sic(input("Enter the SIC of the Student who wants to issue: "))
            sid= sic_to_index(sic,'l')
            return_book(sid)
        elif c == 4:
            sic = is_valid_sic(input("Enter the SIC of the student whose issue list is to be seen: "))
            sid = sic_to_index(sic,'l')
            students = file_to_data('students')
            if len(students[sid - 1]["books_issued"])>0:
                for i in students[sid - 1]["books_issued"]:
                    print(i)
            else:
                print("This Student hasn't issued any Book yet!")
        elif c == 5:
            bid = is_valid_index(input("Enter the ID of the book to see who all have issued it: "))
            book_lended_to(bid)
        elif c == 6:
            main()
        elif c == 7:
            exit()
        else:
            print("Invalid Input, Try Again: ")
            librarian()


if __name__ == "__main__":
    main()
