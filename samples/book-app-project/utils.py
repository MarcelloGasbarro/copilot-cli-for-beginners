def print_menu():
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option (1-5): ").strip()

        if not choice:
            print("Please enter a number from 1 to 5.")
            continue

        if not choice.isdigit():
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        return choice


def get_book_details():
    """Collect a book's title, author, and publication year from user input.

    This function prompts the user for each field, validates the values,
    and keeps asking until a valid title and author are entered.

    Parameters:
        None. The function reads all values directly from standard input.

    Returns:
        tuple: A three-item tuple containing:
            - title (str): The entered book title.
            - author (str): The entered author name.
            - year (int): The publication year as an integer, or 0 if the
              input is empty or invalid.
    """
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("Book title cannot be empty. Please try again.")

    while True:
        author = input("Enter author: ").strip()
        if author:
            break
        print("Author cannot be empty. Please try again.")

    while True:
        year_input = input("Enter publication year: ").strip()
        if not year_input:
            print("Publication year cannot be empty. Defaulting to 0.")
            year = 0
            break

        try:
            year = int(year_input)
            break
        except ValueError:
            print("Invalid year. Defaulting to 0.")
            year = 0
            break

    return title, author, year


def print_books(books):
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")
