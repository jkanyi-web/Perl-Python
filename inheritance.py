# library management system
# parent class

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    
  def display(self):
    return self.title + " by " + self.author
  
# child class
class LibraryBook(Book):
  def __init__(self, title, author, isbn, copies_available):
    super().__init__(title, author)
    self.isbn = isbn
    self.copies_available = copies_available
    
  def borrow_book(self):
    if self.copies_available > 0:
      self.copies_available -= 1
      return f"{self.title} borrowed successfully. {self.copies_available} copies left"
    else:
      return f"Sorry, no copies of {self.title} left"
    
  def return_book(self):
    self.copies_available += 1
    return f"{self.title} returned successfully. {self.copies_available} copies available"
  
book1 = LibraryBook("The Alchemist", "Paulo Coelho", "978-0062315007", 5)
print(book1.display())
print(book1.borrow_book())
print(book1.return_book())
