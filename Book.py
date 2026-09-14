class Book:
    def __init__ (self, title, author):
        self.author = author
        self.title = title
        self.history = []
        self.borrowed = False
        
    def __str__(self):
        summ = f"Title: {self.title}\nAuthor: {self.author}"
        if self.borrowed:
            status = f"Current Status: Borrowed"    
        else:
            status = f"Current Status: Available"
        return summ +'\n'+ status +'\n' 
         
    def borrow(self):
        if self.borrowed: 
            return False
        else:
            self.borrowed = True
            return True
        
    def return_book(self):
        if self.borrowed: 
            self.borrowed = False   
            return True
        else: 
            return False
                
book_one = Book('Wealth of nations', 'Adam Smith')
book_two = Book('The Forms', 'Plato')


neo = book_two.borrow()
neo = book_one.borrow()
neo = book_two.return_book()
print(book_two)
print(book_one)
