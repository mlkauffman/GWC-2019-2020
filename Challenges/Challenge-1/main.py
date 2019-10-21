import copy

def run(books):
    
    """
    Your code goes between the two comment blocks.
    Do not edit anything outside of this section.
    
    As shown above you will recieve a variable called
    books. That variable will contain a list of  10 
    random book titles. Your job is to sort that list
    and ensure that the titles are properly capitalized.
    At the end of your code, the books variable should
    contain your final list. Use the Run command to test
    your code using the sample book list below.
    Submit your final result using the Challenge 1 Submit
    command.
    """
    
    #Your code goes here
    
    """
    Do not code past this point.
    """
    
    
    return books

if __name__== "__main__":
    books = [
        'the great gatsby', 
        'TO KILL A MOCKINGBIRD', 
        'ROMEO and juliet', 
        'Macbeth',
        '1984',
        'Frankenstein',
        'Brave New World',
        'Pride AND PREJUDICE',
        'bEOWULF',
        'jANE eyre']
        
    books = run(books)
    print("Your final list:")
    print(books)