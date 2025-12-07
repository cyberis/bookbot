# Bookbot -- main.py - Analyize text versions of books and provide information (entry point).
from stats import book_word_count, character_counts

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    print(f"Found {word_count} total words")
    char_counts = character_counts(book_text)
    print(char_counts)
    
if __name__ == "__main__":
    main()
    
