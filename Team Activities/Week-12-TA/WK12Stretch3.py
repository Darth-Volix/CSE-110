'''
Week 12 Team Activity: Books in the Scriptures
Nicholas Wilkins
11/28/2023
'''
# This version accomplishes stretch challenge 3

# Set the variables for longest book length and its name
longest_book = -999999
longest_book_name = None

# Program asks for user to indicate which book of scripture they would like the information from 
user_request = input('\nWhich volume of scripture would you like the information from?\n\nOptions:\n1. Old Testament\n2. New Testament\n3. Book of Mormon\n4. Doctrine and Covenants\n5. Pearl of Great Price\n\nEnter Volume Name: ')
print()

# Open the file with the data that is needed
with open('books_and_chapters.txt') as file_var:
    # Begin stripping whitespace and splitting line into parts
    for line in file_var:
        remove_whtspc = line.strip()
        split_info = remove_whtspc.split(':')

        # Assign variables to each piece of information in the newly split line
        book = split_info[0]
        chapters = int(split_info[1])
        scripture = split_info[2]

        # Print all information on the user's requested volume
        if scripture.lower() == user_request.lower():
            print(f'Volume: {scripture}, Book: {book}, Chapters: {chapters}')

        # Find the book with the largest number of chapters in the scriptures
        if scripture.lower() == user_request.lower() and chapters > longest_book:
            longest_book = chapters
            longest_book_name = book
    
    # Output the result
    print(f'\nThe book with the longest number of chapters in the {user_request} is {longest_book_name}, which has {longest_book} chapters!\n')