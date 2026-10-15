from books import display_books, save_books, load_books
name = input("enter your name: ")

print(f"welcome {name} to personal book manager!")

number_of_books = int(input("how many books do you want to add? "))

books = load_books()
display_books(books)

for i in range(number_of_books):
    book = input(f"enter the name of a book {i + 1}: ")
    books.append(book)

display_books(books)
save_books(books)