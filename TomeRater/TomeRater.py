class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user's email address has been changed.")

    def __repr__(self):
        count_var = 0
        for x in self.books.items():
            count_var += 1
        return "User {name}, email: {email}, books read: {counted}".format(name=self.name, email=self.email, counted=count_var)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating
    
    def get_average_rating(self):
        total_ratings = 0
        counted_rating = 0
        avg_rating = 0
        for book, rating in self.books.items():
            total_ratings = rating + total_ratings
            counted_rating += 1
        avg_rating = total_ratings/counted_rating
        return avg_rating

    def tell_me_what_you_are(self):
        this = isinstance(self, User)
        return "It is " + str(this) + " that I am an instance of User"


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book's ISBN has been updated to " + str(new_isbn) + ".")

    def add_rating(self, rating):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print("The books are the same.")

    def __hash__(self):
        return hash((self.title, self.isbn))    

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        total_ratings = 0
        counted_rating = 0
        avg_rating = 0
        for rating in self.ratings:
            total_ratings = rating + total_ratings
            counted_rating += 1
        if counted_rating > 0:
            avg_rating = total_ratings/counted_rating
        return avg_rating

    def tell_me_what_you_are(self):
        this = isinstance(self, Book)
        return "It is " + str(this) + " that I am an instance of Book"

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def tell_me_what_you_are(self):
        this = isinstance(self, Fiction)
        return "It is " + str(this) + " that I am an instance of Fiction"

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def tell_me_what_you_are(self):
        this = isinstance(self, NonFiction)
        return "It is " + str(this) + " that I am an instance of NonFiction"

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def tell_me_what_you_are(self):
        this = isinstance(self, TomeRater)
        return "It is " + str(this) + " that I am an instance of TomeRater"

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        newUser = self.users.get(email, None)
        if newUser:
            newUser.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {sentEmail}".format(sentEmail=email))

    def add_book_to_user2(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        newUser = User(name, email)
        self.users[email] = newUser
        if type(user_books) is dict and len(user_books) > 0:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for x in self.books:
            print(x)
    
    def print_users(self):
        for x in self.users:
            print(x)

    def get_most_read_book(self):
        highest_rating_val = 0
        highest_rating_book = ""
        for book, rating in self.books.items():
            if rating > highest_rating_val:
                highest_rating_val = rating
                highest_rating_book = book
        return highest_rating_book

    def highest_rated_book(self):
        highest_avg_val = 0
        highest_avg_book = None
        for book in self.books:
            avg = book.get_average_rating()
            if avg > highest_avg_val:
                highest_avg_val = avg
                highest_avg_book = book
        return highest_avg_book

    def most_positive_user(self):
        highest_positive_rating = 0
        highest_positive_user = None
        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > highest_positive_rating:
                highest_positive_rating = avg
                highest_positive_user = user
        return highest_positive_user













    