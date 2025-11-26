from library_manager import LibrarySystem
from book import BookItem

system = LibrarySystem()

def main_menu():
    while True:
        print("\n============== LIBRARY CONTROL ==============")
        print("1) Add New Book")
        print("2) Borrow Book")
        print("3) Submit Book")
        print("4) Show All Books")
        print("5) Search by Title")
        print("6) Stop Program")

        opt = input("Choose option: ").strip()

        if opt == "1":
            t = input("Book Title: ")
            w = input("Author Name: ")
            c = input("Book Code: ")
            new_b = BookItem(t, w, c)
            system.insert_book(new_b)
            print("Book saved successfully.")

        elif opt == "2":
            code = input("Enter Book Code to borrow: ")
            item = system.find_code(code)
            if item:
                if item.state == "free":
                    item.state = "taken"
                    system.write_file()
                    print("Book issued.")
                else:
                    print("This book is already borrowed.")
            else:
                print("No such book in records.")

        elif opt == "3":
            code = input("Enter Book Code to return: ")
            item = system.find_code(code)
            if item:
                if item.state == "taken":
                    item.state = "free"
                    system.write_file()
                    print("Book returned.")
                else:
                    print("This book was not borrowed.")
            else:
                print("Invalid book code.")

        elif opt == "4":
            system.show_all()

        elif opt == "5":
            key = input("Enter title to search: ")
            result = system.find_title(key)
            for b in result:
                print(f"{b.title} | {b.writer} | {b.code} | {b.state}")

        elif opt == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice, try again.")

main_menu()