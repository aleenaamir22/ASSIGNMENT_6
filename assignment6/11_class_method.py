#11.class method
#Assignment
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:#class
    total_books=0 #class variable
    
    @classmethod #class method
    def increment_book_count(cls): #method
        cls.total_books +=1 #increament method

#creating object:
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
#printing
print(Book.total_books)
        
#output
# 7        