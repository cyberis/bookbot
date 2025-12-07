# Bookbot -- main.py - Analyize text versions of books and provide information (entry point).

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def book_word_count(book_text):
    words = book_text.split()
    return len(words)
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    print(f"Found {word_count} total words")
    
if __name__ == "__main__":
    main()
    
