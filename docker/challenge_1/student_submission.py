def run(books):
    x = 0
    while x < len(books):
        books[x] = books[x].title()
        x = x + 1
        
    books.sort()
    
    return books