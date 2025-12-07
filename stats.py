# Bookbot -- stats.py - Analyze text versions of books and provide statistical information.

def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def character_counts(book_text):
    char_counts = {}
    
    for char in book_text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    return char_counts