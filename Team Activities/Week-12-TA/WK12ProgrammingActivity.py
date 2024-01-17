'''
Week 12 Team Activity: Books in the Scriptures
Nicholas Wilkins
11/28/2023
'''
# Set the variables for longest book length and its name
longest_book = -999999
longest_book_name = None

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

        # Print the information for each volume and book
        print(f'Volume: {scripture}, Book: {book}, Chapters: {chapters}')

        # Find the book with the largest number of chapters in the scriptures
        if chapters > longest_book:
            longest_book = chapters
            longest_book_name = book
    
    # Output the result
    print(f'\nThe book with the longest number of chapters is {longest_book_name}, which has {longest_book} chapters!\n')

