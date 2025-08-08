class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  
  def get_info(self):
    return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
  def __init__(self, title, author, file_size):
    self.file_size = file_size
    super().__init__(title, author,)
  
  def get_info(self):
    return f"{super().get_info()}, File size: {self.file_size} kb"

class PrintBook(Book):
  def __init__(self, title, author, page_count):
    self.page_count = page_count
    super().__init__(title, author)
  
  def get_info(self):
    return f"{super().get_info()}, Pages: {self.page_count}"

class Library:
  def __init__(self, title):
    self.books = []
    self.title = title
  
  def add_book(self, book):
    if isinstance(book, Book):
     self.books.append(Book)
    else:
      raise TypeError("Only instances of Book or subclasses can be added")
  
  def list_books(self):
    if not self.books:
      print("Library has no books.")
    else:
      for idx, book in enumerate(self.books, start=1):
        print(f"{idx}. {book.get_info(self)}")
