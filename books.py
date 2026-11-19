import json


def display_books(books):
    print("\nYour books:")

    if not books:
        print("No books found.")
        return

    for book in books:
        print(book)


def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []