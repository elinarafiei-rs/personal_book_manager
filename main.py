from books import display_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")

admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("Do you want to open admin mode (yes/no)? ")

if open_admin.lower() == "yes":
    entered_password = input("Enter password : ")
    print("Hello! Admin")
elif open_admin.lower() == "no":
    print("Alright!")
else:
    print("Wrong password!")


print(f"Welcome {name} to Personal Book Manager!")

books = load_books()


number_of_books = int(input("\nHow many books do you want to add? "))

for i in range(number_of_books):
    book = input(f"Enter the name of book {i + 1}: ")
    books.append(book)

save_books(books)

display_books(books)