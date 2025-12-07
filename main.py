# Bookbot -- main.py - Analyize text versions of books and provide information (entry point).
from stats import book_word_count, character_counts, sorted_character_counts    

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

    
def main():
    # Get book properties
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    char_counts = character_counts(book_text)
    sorted_char_counts = sorted_character_counts(char_counts)
    
    # Print out report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in sorted_char_counts:
        print(f'{char_count["char"]}: {char_count["num"]}')
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
    
